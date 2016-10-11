"""
Organization objects have tags as attributes. This dict translates the tags
into categories and types of organizations. Categories are wider sets that
contain several types.

Source of the categories and tag data: WhatDoTheyKnow.com, mySociety.
"""
organization_categories = {
  'department': {
    'organisation_category': 'Central government',
    'organisation_type': 'Ministerial departments'
  },
  'non_ministerial_department': {
    'organisation_category': 'Central government',
    'organisation_type': 'Non-ministerial departments'
  },
  'executive_agency': {
    'organisation_category': 'Central government',
    'organisation_type': 'Executive agencies'
  },
  'advisory_committee': {
    'organisation_category': 'Central government',
    'organisation_type': 'Advisory bodies'
  },
  'endpb': {
    'organisation_category': 'Central government',
    'organisation_type': 'Executive non-departmental public bodies'
  },
  'other_cg': {
    'organisation_category': 'Central government',
    'organisation_type': 'Other central government bodies'
  },
  'inspectorate': {
    'organisation_category': 'Central government',
    'organisation_type': 'Inspectorates'
  },
  'regulator': {
    'organisation_category': 'Central government',
    'organisation_type': 'Regulators'
  },
  'public_corporation': {
    'organisation_category': 'Central government',
    'organisation_type': 'Public corporations'
  },
  'university': {
    'organisation_category': 'Education',
    'organisation_type': 'Universities'
  },
  'university_college': {
    'organisation_category': 'Education',
    'organisation_type': 'University colleges'
  },
  'cambridge_college': {
    'organisation_category': 'Education',
    'organisation_type': 'Cambridge colleges'
  },
  'durham_college': {
    'organisation_category': 'Education',
    'organisation_type': 'Durham colleges'
  },
  'oxford_college': {
    'organisation_category': 'Education',
    'organisation_type': 'Oxford colleges'
  },
  'group_of_universities': {
    'organisation_category': 'Education',
    'organisation_type': 'Groups of universities'
  },
  'university_owned_company': {
    'organisation_category': 'Education',
    'organisation_type': 'University owned companies'
  },
  'hei': {
    'organisation_category': 'Education',
    'organisation_type': 'Higher education institutions'
  },
  'fei': {
    'organisation_category': 'Education',
    'organisation_type': 'Further education institutions'
  },
  'academies': {
    'organisation_category': 'Education',
    'organisation_type': 'Academies'
  },
  'school': {
    'organisation_category': 'Education',
    'organisation_type': 'Schools'
  },
  'exam_board': {
    'organisation_category': 'Education',
    'organisation_type': 'Exam boards'
  },
  'research_council': {
    'organisation_category': 'Education',
    'organisation_type': 'Research councils'
  },
  'lib_board': {
    'organisation_category': 'Education',
    'organisation_type': 'Education and library boards'
  },
  'rbc': {
    'organisation_category': 'Education',
    'organisation_type': 'Regional Broadband Consortia'
  },
  'school_inspectorate': {
    'organisation_category': 'Education',
    'organisation_type': 'School inspectorates'
  },
  'welsh_establishment': {
    'organisation_category': 'Education',
    'organisation_type': 'Welsh Establishment'
  },
  'all_through': {
    'organisation_category': 'Education',
    'organisation_type': 'All-through school'
  },
  'free_school': {
    'organisation_category': 'Education',
    'organisation_type': 'Free school'
  },
  'academy_trust': {
    'organisation_category': 'Education',
    'organisation_type': 'Academy Trust'
  },
  'utc': {
    'organisation_category': 'Education',
    'organisation_type': 'University Technical Colleges'
  },
  'police': {
    'organisation_category': 'Emergency services',
    'organisation_type': 'Policing bodies'
  },
  'police_force': {
    'organisation_category': 'Emergency services',
    'organisation_type': 'Police forces'
  },
  'police_crime_commissioner': {
    'organisation_category': 'Emergency services',
    'organisation_type': 'Police and Crime Commissioners'
  },
  'police_crime_panel': {
    'organisation_category': 'Emergency services',
    'organisation_type': 'Police and Crime Panels'
  },
  'pcsp': {
    'organisation_category': 'Emergency services',
    'organisation_type': 'Policing and community safety partnerships'
  },
  'fire_service': {
    'organisation_category': 'Emergency services',
    'organisation_type': 'Fire and rescue services'
  },
  'adhac': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Agricultural dwelling house advisory committees'
  },
  'awc': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Agricultural wages committees'
  },
  'ifca': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Inshore fisheries and conservation authorities'
  },
  'idb': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Internal drainage boards'
  },
  'mcz': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Marine conservation zones'
  },
  'npa': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'National park authorities'
  },
  'rpa': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Regional park authorities'
  },
  'sea_fishery_committee': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Sea fisheries committees'
  },
  'wda': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Waste disposal authorities'
  },
  'wma': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Waste management authorities (Northern Ireland)'
  },
  'watercompanies': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Water companies'
  },
  'zoo': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Zoos'
  },
  'aonbcb': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type': 'Areas of Outstanding Natural Beauty Conservation Boards'
  },
  'association': {
    'organisation_category': 'Groups of public authorities',
    'organisation_type': 'Associations of public authorities'
  },
  'group_of_universities': {
    'organisation_category': 'Groups of public authorities',
    'organisation_type': 'Groups of universities'
  },
  'pbo': {
    'organisation_category': 'Groups of public authorities',
    'organisation_type': 'Professional buying organisations'
  },
  'nhs': {
    'organisation_category': 'Health',
    'organisation_type': 'NHS bodies'
  },
  'nhstrust': {
    'organisation_category': 'Health',
    'organisation_type': 'NHS trusts'
  },
  'pct': {
    'organisation_category': 'Health',
    'organisation_type': 'Primary care trusts'
  },
  'nhsni': {
    'organisation_category': 'Health',
    'organisation_type': 'NHS in Northern Ireland'
  },
  'commissioning_consortium': {
    'organisation_category': 'Health',
    'organisation_type': 'GP commissioning consortia'
  },
  'hscr': {
    'organisation_category': 'Health',
    'organisation_type': 'Health / social care'
  },
  'his': {
    'organisation_category': 'Health',
    'organisation_type': 'Health Informatic Services'
  },
  'optician': {
    'organisation_category': 'Health',
    'organisation_type': 'Opticians'
  },
  'pharmacy': {
    'organisation_category': 'Health',
    'organisation_type': 'Pharmacies'
  },
  'dentist': {
    'organisation_category': 'Health',
    'organisation_type': 'NHS Dentists'
  },
  'pha': {
    'organisation_category': 'Health',
    'organisation_type': 'Port health authorities'
  },
  'pho': {
    'organisation_category': 'Health',
    'organisation_type': 'Public health observatories'
  },
  'sha': {
    'organisation_category': 'Health',
    'organisation_type': 'Strategic health authorities'
  },
  'specialha': {
    'organisation_category': 'Health',
    'organisation_type': 'Special health authorities'
  },
  'healthwatch': {
    'organisation_category': 'Health',
    'organisation_type': 'Healthwatch organisations'
  },
  'surgery': {
    'organisation_category': 'Health',
    'organisation_type': 'GP Surgery'
  },
  'nhswales': {
    'organisation_category': 'Health',
    'organisation_type': 'NHS in Wales'
  },
  'nhs_wales_chc': {
    'organisation_category': 'Health',
    'organisation_type': 'Community Health Councils in Wales'
  },
  'nhs_wales_lhb': {
    'organisation_category': 'Health',
    'organisation_type': 'NHS Wales Local Health Boards'
  },
  'ukparliament': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'UK Parliament'
  },
  'national_parliament_or_assembly': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'National Parliaments and Assemblies'
  },
  'court': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Courts'
  },
  'coroners_office': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Coroners&#x27; offices'
  },
  'tribunal': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Tribunals'
  },
  'approved_regulator': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Approved regulators of legal services'
  },
  'prob_board': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Probation boards'
  },
  'rules_committee': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Rules committees'
  },
  'cja': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Community justice authorities'
  },
  'verderers': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Verderers'
  },
  'CRC': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Community Rehabilitation Companies'
  },
  'imb': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Independent monitoring boards (for prisons)'
  },
  'scottish_prison_contractor': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type': 'Contrators Running Scottish Private Prisons'
  },
  'local_council': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Local councils'
  },
  'parish_council': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Town and Parish councils'
  },
  'almo': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Housing ALMOs'
  },
  'assessor': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Assessors for Valuation joint boards (Scotland)'
  },
  'housing_association': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Housing associations'
  },
  'joint_committee': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Joint Committees'
  },
  'licensing_board': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Licensing boards (Scotland)'
  },
  'lscb': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Local safeguarding children boards'
  },
  'municipal_bank': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Municipal banks'
  },
  'newdeal': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'New Deal for Communities partnership'
  },
  'nsbody': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'North/south bodies'
  },
  'udc': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Urban Development Company'
  },
  'vjb': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Valuation joint boards (Scotland)'
  },
  'companies_owned_by_local_gov': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Companies owned by local government'
  },
  'bodies_funded_by_local_gov': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Bodies funded by local government'
  },
  'charter_trustees': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Charter trustees'
  },
  'LEP': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Local Enterprise Partnerships'
  },
  'other_lg': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Local government other'
  },
  'aonbcb': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Areas of Outstanding Natural Beauty Conservation Boards'
  },
  'combined_authority': {
    'organisation_category': 'Local and regional',
    'organisation_type': 'Combined authorities'
  },
  'media': {
    'organisation_category': 'Media and culture',
    'organisation_type': 'Media'
  },
  'museum': {
    'organisation_category': 'Media and culture',
    'organisation_type': 'Museums and galleries'
  },
  'armed_forces': {
    'organisation_category': 'Military and security services',
    'organisation_type': 'Armed Forces'
  },
  'military_college': {
    'organisation_category': 'Military and security services',
    'organisation_type': 'Military colleges'
  },
  'security_services': {
    'organisation_category': 'Military and security services',
    'organisation_type': 'Security services'
  },
  'inns_of_court': {
    'organisation_category': 'Other',
    'organisation_type': 'Inns of court'
  },
  'ombudsman': {
    'organisation_category': 'Other',
    'organisation_type': 'Ombudsmen'
  },
  'professional_body': {
    'organisation_category': 'Other',
    'organisation_type': 'Professional bodies'
  },
  'publicly_funded_charities': {
    'organisation_category': 'Other',
    'organisation_type': 'Publicly funded charities'
  },
  'duchy': {
    'organisation_category': 'Other',
    'organisation_type': 'Royal duchies'
  },
  'foi_voluntary': {
    'organisation_category': 'Other',
    'organisation_type': 'Voluntary'
  },
  'sport': {
    'organisation_category': 'Recreation',
    'organisation_type': 'Sport'
  },
  'theatre': {
    'organisation_category': 'Recreation',
    'organisation_type': 'Theatre'
  },
  'dance': {
    'organisation_category': 'Recreation',
    'organisation_type': 'Dance'
  },
  'airport': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Airport companies'
  },
  'bus_company': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Bus companies'
  },
  'public_infrastructure': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Companies controlling national infrastructure'
  },
  'navigation_authority': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Navigation authorities'
  },
  'npte': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Passenger transport executives'
  },
  'port_authority': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Port authorities'
  },
  'railways': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Railway companies'
  },
  'srp': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Safer Roads Partnership'
  },
  'toll_company': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Toll companies'
  },
  'trunk_road_agency': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Trunk road agencies (Wales)'
  },
  'telecom_companies': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type': 'Telecommunications Company'
  }
}
