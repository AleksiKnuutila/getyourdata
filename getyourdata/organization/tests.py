from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

from organization.models import Organization, AuthenticationField

class OrganizationCreationTests(TestCase):
    def test_organization_with_valid_email_address_can_be_added(self):
        response = self.client.post(
            reverse("organization:new_organization"),
            {"name": "The Organization",
             "email_address": "valid@address.com"},
            follow=True)

        self.assertContains(response, "Organization profile created")

        organization = Organization.objects.all()[0]

        self.assertEquals(organization.name, "The Organization")
        self.assertEquals(organization.email_address, "valid@address.com")

    def test_organization_with_invalid_email_address_cant_be_added(self):
        response = self.client.post(
            reverse("organization:new_organization"),
            {"name": "The Organization",
             "email_address": "notavalidaddrss"},
            follow=True)

        self.assertNotContains(response, "Organization profile created")

        self.assertEquals(Organization.objects.all().count(), 0)

    def test_organization_with_missing_contact_information_cant_be_added(self):
        response = self.client.post(
            reverse("organization:new_organization"),
            {"name": "The Organization"},
            follow=True)

        self.assertContains(
            response, "Organization profile must contain either")
        self.assertEquals(Organization.objects.all().count(), 0)

    def test_organization_with_postal_information_can_be_added(self):
        response = self.client.post(
            reverse("organization:new_organization"),
            {"name": "The Organization",
             "address_line_one": "Fake Street 4",
             "postal_code": "00444",
             "country": "Finland"},
            follow=True)

        self.assertContains(response, "Organization profile created")

        organization = Organization.objects.all()[0]

        self.assertEquals(organization.name, "The Organization")
        self.assertEquals(organization.address_line_one, "Fake Street 4")
        self.assertEquals(organization.postal_code, "00444")
        self.assertEquals(organization.country, "Finland")

    def test_organization_with_missing_postal_information_cant_be_added(self):
        response = self.client.post(
            reverse("organization:new_organization"),
            {"name": "The Organization",
             "address_line_one": "Fake Street 4"},
            follow=True)

        self.assertNotContains(response, "Organization profile created")
        self.assertEquals(Organization.objects.all().count(), 0)

    def test_organization_with_valid_postal_and_email_can_be_added(self):
        response = self.client.post(
            reverse("organization:new_organization"),
            {"name": "The Organization",
             "address_line_one": "Fake Street 4",
             "postal_code": "00444",
             "country": "Finland",
             "email_address": "fake@address.com"},
            follow=True)

        self.assertContains(response, "Organization profile created")

        organization = Organization.objects.all()[0]

        self.assertEquals(organization.name, "The Organization")
        self.assertEquals(organization.address_line_one, "Fake Street 4")
        self.assertEquals(organization.postal_code, "00444")
        self.assertEquals(organization.country, "Finland")
        self.assertEquals(organization.email_address, "fake@address.com")

def create_organization(test_case):
    response = test_case.client.post(
        reverse("organization:new_organization"),
        {"name": "The Organization",
         "email_address": "valid@address.com"},
        follow=True)

    test_case.assertContains(response, "Organization profile created")

class OrganizationListingTests(TestCase):
    def test_no_organizations_listed_when_no_organizations_exists(self):
        response = self.client.get(reverse("organization:list_organizations"))

        self.assertContains(response, "No organizations yet")

    def test_existing_organizations_listed_on_page(self):
        for i in range(0, 5):
            create_organization(self)

        response = self.client.get(reverse("organization:list_organizations"))

        self.assertContains(response, "The Organization", 5)

    def test_only_15_organizations_are_listed_per_page(self):
        for i in range(0, 20):
            create_organization(self)

        response = self.client.get(reverse("organization:list_organizations"))

        self.assertContains(response, "The Organization", 15)

    def test_correct_amount_of_organizations_listed_per_page(self):
        for i in range(0, 25):
            create_organization(self)

        response = self.client.get(reverse("organization:list_organizations"))

        self.assertContains(response, "The Organization", 15)

        response = self.client.get(
            reverse("organization:list_organizations"),
            {"page": 2})

        self.assertContains(response, "The Organization", 10)


class OrganizationListJavascriptTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(OrganizationListJavascriptTests, cls).setUpClass()
        cls.selenium = WebDriver()
        # Prevent tests from failing by making the test wait longer
        # if element isn't immediately available
        cls.selenium.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(OrganizationListJavascriptTests, cls).tearDownClass()

    def setUp(self):
        self.auth_field1 = AuthenticationField.objects.create(
            name="some_number",
            title='Some number')

        # Create three pages worth of organizations
        for i in range(0, 45):
            organization = Organization.objects.create(
                name='Organization %d' % i,
                email_address='fake@address.com',
                address_line_one='Address one',
                address_line_two='Address two',
                postal_code='00000',
                country='Finland'
                )

            organization.authentication_fields.add(self.auth_field1)

    def test_cant_create_request_with_no_selected_organizations(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url,
                      reverse("organization:list_organizations")))

        self.assertEquals(
            self.selenium.find_element_by_id("create-request").is_enabled(),
            False)

        self.assertIn("0 organizations selected", self.selenium.page_source)

    def test_select_single_organization_for_request(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url,
                      reverse("organization:list_organizations")))

        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        self.assertIn("1 organization selected", self.selenium.page_source)

        self.selenium.find_element_by_id("create-request").click()

        self.assertIn("Request your data from Organization 0", self.selenium.page_source)


    def test_select_multiple_organizations_for_request(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url,
                      reverse("organization:list_organizations")))

        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
        self.assertIn("2 organizations selected", self.selenium.page_source)

        self.selenium.find_element_by_id("create-request").click()

        self.assertIn("Request your data from multiple organizations", self.selenium.page_source)

    def test_can_change_page_to_display_different_organizations(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url,
                      reverse("organization:list_organizations")))

        self.selenium.find_element_by_id("page-2").click()

        self.assertIn("Organization 15", self.selenium.page_source)
        self.assertNotIn("Organization 0", self.selenium.page_source)

        self.selenium.find_element_by_id("page-1").click()

        self.assertIn("Organization 0", self.selenium.page_source)
        self.assertNotIn("Organization 15", self.selenium.page_source)

    def test_user_can_select_multiple_organizations_from_different_pages(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url,
                      reverse("organization:list_organizations")))

        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
        self.assertIn("2 organizations selected", self.selenium.page_source)

        self.selenium.find_element_by_id("page-2").click()

        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
        self.assertIn("4 organizations selected", self.selenium.page_source)

        self.selenium.find_element_by_id("page-3").click()

        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        self.selenium.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()
        self.assertIn("6 organizations selected", self.selenium.page_source)
