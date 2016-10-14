"""
Organization objects have tags as attributes. This dict translates the tags
into categories and types of organizations. Categories are wider sets that
contain several types.

Source of the categories and tag data: WhatDoTheyKnow.com, mySociety.
"""
organization_categories = {
  'department': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Ministerial departments',
    'organisation_type_singular': 'Ministerial department'
  },
  'non_ministerial_department': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Non-ministerial departments',
    'organisation_type_singular': 'Non-ministerial department'
  },
  'executive_agency': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Executive agencies',
    'organisation_type_singular': 'Executive agency'
  },
  'advisory_committee': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Advisory bodies',
    'organisation_type_singular': 'Advisory body'
  },
  'endpb': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Executive non-departmental public bodies',
    'organisation_type_singular': 'Executive non-departmental public body'
  },
  'other_cg': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Other central government bodies',
    'organisation_type_singular': 'Other central government body'
  },
  'inspectorate': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Inspectorates',
    'organisation_type_singular': 'Inspectorate'
  },
  'regulator': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Regulators',
    'organisation_type_singular': 'Regulator'
  },
  'public_corporation': {
    'organisation_category': 'Central government',
    'organisation_type_plural': 'Public corporations',
    'organisation_type_singular': 'Public corporation'
  },
  'university': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Universities',
    'organisation_type_singular': 'University'
  },
  'university_college': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'University colleges',
    'organisation_type_singular': 'University college'
  },
  'cambridge_college': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Cambridge colleges',
    'organisation_type_singular': 'Cambridge college'
  },
  'durham_college': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Durham colleges',
    'organisation_type_singular': 'Durham college'
  },
  'oxford_college': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Oxford colleges',
    'organisation_type_singular': 'Oxford college'
  },
  'group_of_universities': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Groups of universities',
    'organisation_type_singular': 'Group of universities'
  },
  'university_owned_company': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'University owned companies',
    'organisation_type_singular': 'University owned company'
  },
  'hei': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Higher education institutions',
    'organisation_type_singular': 'Higher education institution'
  },
  'fei': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Further education institutions',
    'organisation_type_singular': 'Further education institution'
  },
  'academies': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Academies',
    'organisation_type_singular': 'Academy'
  },
  'school': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Schools',
    'organisation_type_singular': 'Schools'
  },
  'exam_board': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Exam boards',
    'organisation_type_singular': 'Exam board'
  },
  'research_council': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Research councils',
    'organisation_type_singular': 'Research council'
  },
  'lib_board': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Education and library boards',
    'organisation_type_singular': 'Education and library board'
  },
  'rbc': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Regional Broadband Consortia',
    'organisation_type_singular': 'Regional Broadband Consortium'
  },
  'school_inspectorate': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'School inspectorates',
    'organisation_type_singular': 'School inspectorate'
  },
  'welsh_establishment': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Welsh Establishment',
    'organisation_type_singular': 'Welsh Establishment'
  },
  'all_through': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'All-through school',
    'organisation_type_singular': 'All-through school'
  },
  'free_school': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Free school',
    'organisation_type_singular': 'Free school'
  },
  'academy_trust': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'Academy Trust',
    'organisation_type_singular': 'Academy Trust'
  },
  'utc': {
    'organisation_category': 'Education',
    'organisation_type_plural': 'University Technical Colleges',
    'organisation_type_singular': 'University Technical College'
  },
  'police': {
    'organisation_category': 'Emergency services',
    'organisation_type_plural': 'Policing bodies',
    'organisation_type_singular': 'Policing body'
  },
  'police_force': {
    'organisation_category': 'Emergency services',
    'organisation_type_plural': 'Police forces',
    'organisation_type_singular': 'Police force'
  },
  'police_crime_commissioner': {
    'organisation_category': 'Emergency services',
    'organisation_type_plural': 'Police and Crime Commissioners',
    'organisation_type_singular': 'Police and Crime Commissioner'
  },
  'police_crime_panel': {
    'organisation_category': 'Emergency services',
    'organisation_type_plural': 'Police and Crime Panels',
    'organisation_type_singular': 'Police and Crime Panel'
  },
  'pcsp': {
    'organisation_category': 'Emergency services',
    'organisation_type_plural': 'Policing and community safety partnerships',
    'organisation_type_singular': 'Policing and community safety partnership'
  },
  'fire_service': {
    'organisation_category': 'Emergency services',
    'organisation_type_plural': 'Fire and rescue services',
    'organisation_type_singular': 'Fire and rescue service'
  },
  'adhac': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Agricultural dwelling house advisory, committees',
    'organisation_type_singular': 'Agricultural dwelling house advisory committee'
  },
  'awc': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Agricultural wages committees',
    'organisation_type_singular': 'Agricultural wages committee'
  },
  'ifca': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Inshore fisheries and conservation, authorities',
    'organisation_type_singular': 'Inshore fisheries and conservation authority'
  },
  'idb': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Internal drainage boards',
    'organisation_type_singular': 'Internal drainage board'
  },
  'mcz': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Marine conservation zones',
    'organisation_type_singular': 'Marine conservation zone'
  },
  'npa': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'National park authorities',
    'organisation_type_singular': 'National park authority'
  },
  'rpa': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Regional park authorities',
    'organisation_type_singular': 'Regional park authority'
  },
  'sea_fishery_committee': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Sea fisheries committees',
    'organisation_type_singular': 'Sea fisheries committee'
  },
  'wda': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Waste disposal authorities',
    'organisation_type_singular': 'Waste disposal authority'
  },
  'wma': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Waste management authorities (Northern, Ireland)',
    'organisation_type_singular': 'Waste management authority (Northern Ireland)'
  },
  'watercompanies': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Water companies',
    'organisation_type_singular': 'Water company'
  },
  'zoo': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Zoos',
    'organisation_type_singular': 'Zoo'
  },
  'aonbcb': {
    'organisation_category': 'Environment and agriculture',
    'organisation_type_plural': 'Areas of Outstanding Natural Beauty, Conservation Boards',
    'organisation_type_singular': 'Areas of Outstanding Natural Beauty Conservation Board'
  },
  'association': {
    'organisation_category': 'Groups of public authorities',
    'organisation_type_plural': 'Associations of public authorities',
    'organisation_type_singular': 'Associations of public authority'
  },
  'group_of_universities': {
    'organisation_category': 'Groups of public authorities',
    'organisation_type_plural': 'Groups of universities',
    'organisation_type_singular': 'Group of universities'
  },
  'pbo': {
    'organisation_category': 'Groups of public authorities',
    'organisation_type_plural': 'Professional buying organisations',
    'organisation_type_singular': 'Professional buying organisation'
  },
  'nhs': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'NHS bodies',
    'organisation_type_singular': 'NHS body'
  },
  'nhstrust': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'NHS trusts',
    'organisation_type_singular': 'NHS trust'
  },
  'pct': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Primary care trusts',
    'organisation_type_singular': 'Primary care trust'
  },
  'nhsni': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'NHS in Northern Ireland',
    'organisation_type_singular': 'NHS in Northern Ireland'
  },
  'commissioning_consortium': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'GP commissioning consortia',
    'organisation_type_singular': 'GP commissioning consortium'
  },
  'hscr': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Health / social care',
    'organisation_type_singular': 'Health / social care'
  },
  'his': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Health Informatic Services',
    'organisation_type_singular': 'Health Informatic Service'
  },
  'optician': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Opticians',
    'organisation_type_singular': 'Optician'
  },
  'pharmacy': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Pharmacies',
    'organisation_type_singular': 'Pharmacy'
  },
  'dentist': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'NHS Dentists',
    'organisation_type_singular': 'NHS Dentist'
  },
  'pha': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Port health authorities',
    'organisation_type_singular': 'Port health authority'
  },
  'pho': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Public health observatories',
    'organisation_type_singular': 'Public health observatory'
  },
  'sha': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Strategic health authorities',
    'organisation_type_singular': 'Strategic health authority'
  },
  'specialha': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Special health authorities',
    'organisation_type_singular': 'Special health authority'
  },
  'healthwatch': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Healthwatch organisations',
    'organisation_type_singular': 'Healthwatch organisation'
  },
  'surgery': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'GP Surgery',
    'organisation_type_singular': 'GP Surgery'
  },
  'nhswales': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'NHS in Wales',
    'organisation_type_singular': 'NHS in Wales'
  },
  'nhs_wales_chc': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'Community Health Councils in Wales',
    'organisation_type_singular': 'Community Health Council in Wales'
  },
  'nhs_wales_lhb': {
    'organisation_category': 'Health',
    'organisation_type_plural': 'NHS Wales Local Health Boards',
    'organisation_type_singular': 'NHS Wales Local Health Board'
  },
  'ukparliament': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'UK Parliament',
    'organisation_type_singular': 'UK Parliament'
  },
  'national_parliament_or_assembly': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'National Parliaments and Assemblies',
    'organisation_type_singular': 'National Parliaments and Assembly'
  },
  'court': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Courts',
    'organisation_type_singular': 'Court'
  },
  'coroners_office': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Coroners&#x27; offices',
    'organisation_type_singular': 'Coroners&#x27; office'
  },
  'tribunal': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Tribunals',
    'organisation_type_singular': 'Tribunal'
  },
  'approved_regulator': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Approved regulators of legal services',
    'organisation_type_singular': 'Approved regulator of legal services'
  },
  'prob_board': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Probation boards',
    'organisation_type_singular': 'Probation board'
  },
  'rules_committee': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Rules committees',
    'organisation_type_singular': 'Rules committee'
  },
  'cja': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Community justice authorities',
    'organisation_type_singular': 'Community justice authority'
  },
  'verderers': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Verderers',
    'organisation_type_singular': 'Verderer'
  },
  'CRC': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Community Rehabilitation Companies',
    'organisation_type_singular': 'Community Rehabilitation Company'
  },
  'imb': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Independent monitoring boards (for prisons)',
    'organisation_type_singular': 'Independent monitoring board (for prisons)'
  },
  'scottish_prison_contractor': {
    'organisation_category': 'Law making bodies, the courts and the legal system',
    'organisation_type_plural': 'Contrators Running Scottish Private Prisons',
    'organisation_type_singular': 'Contrator Running Scottish Private Prisons'
  },
  'local_council': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Local councils',
    'organisation_type_singular': 'Local council'
  },
  'parish_council': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Town and Parish councils',
    'organisation_type_singular': 'Town and Parish council'
  },
  'almo': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Housing ALMOs',
    'organisation_type_singular': 'Housing ALMO'
  },
  'assessor': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Assessors for Valuation joint boards (Scotland)',
    'organisation_type_singular': 'Assessor for Valuation joint boards (Scotland)'
  },
  'housing_association': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Housing associations',
    'organisation_type_singular': 'Housing association'
  },
  'joint_committee': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Joint Committees',
    'organisation_type_singular': 'Joint Committee'
  },
  'licensing_board': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Licensing boards (Scotland)',
    'organisation_type_singular': 'Licensing board (Scotland)'
  },
  'lscb': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Local safeguarding children boards',
    'organisation_type_singular': 'Local safeguarding children boards'
  },
  'municipal_bank': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Municipal banks',
    'organisation_type_singular': 'Municipal bank'
  },
  'newdeal': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'New Deal for Communities partnership',
    'organisation_type_singular': 'New Deal for Communities partnership'
  },
  'nsbody': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'North/south bodies',
    'organisation_type_singular': 'North/south body'
  },
  'udc': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Urban Development Company',
    'organisation_type_singular': 'Urban Development Company'
  },
  'vjb': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Valuation joint boards (Scotland)',
    'organisation_type_singular': 'Valuation joint board (Scotland)'
  },
  'companies_owned_by_local_gov': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Companies owned by local government',
    'organisation_type_singular': 'Company owned by local government'
  },
  'bodies_funded_by_local_gov': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Bodies funded by local government',
    'organisation_type_singular': 'Body funded by local government'
  },
  'charter_trustees': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Charter trustees',
    'organisation_type_singular': 'Charter trustee'
  },
  'LEP': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Local Enterprise Partnerships',
    'organisation_type_singular': 'Local Enterprise Partnership'
  },
  'other_lg': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Local government other',
    'organisation_type_singular': 'Local government other'
  },
  'aonbcb': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Areas of Outstanding Natural Beauty Conservation Boards',
    'organisation_type_singular': 'Area of Outstanding Natural Beauty Conservation Boards'
  },
  'combined_authority': {
    'organisation_category': 'Local and regional',
    'organisation_type_plural': 'Combined authorities',
    'organisation_type_singular': 'Combined authory'
  },
  'media': {
    'organisation_category': 'Media and culture',
    'organisation_type_plural': 'Media',
    'organisation_type_singular': 'Media'
  },
  'museum': {
    'organisation_category': 'Media and culture',
    'organisation_type_plural': 'Museums and galleries',
    'organisation_type_singular': 'Museum and gallery'
  },
  'armed_forces': {
    'organisation_category': 'Military and security services',
    'organisation_type_plural': 'Armed Forces',
    'organisation_type_singular': 'Armed Forces'
  },
  'military_college': {
    'organisation_category': 'Military and security services',
    'organisation_type_plural': 'Military colleges',
    'organisation_type_singular': 'Military college'
  },
  'security_services': {
    'organisation_category': 'Military and security services',
    'organisation_type_plural': 'Security services',
    'organisation_type_singular': 'Security service'
  },
  'inns_of_court': {
    'organisation_category': 'Other',
    'organisation_type_plural': 'Inns of court',
    'organisation_type_singular': 'Inn of court'
  },
  'ombudsman': {
    'organisation_category': 'Other',
    'organisation_type_plural': 'Ombudsmen',
    'organisation_type_singular': 'Ombudsmen'
  },
  'professional_body': {
    'organisation_category': 'Other',
    'organisation_type_plural': 'Professional bodies',
    'organisation_type_singular': 'Professional body'
  },
  'publicly_funded_charities': {
    'organisation_category': 'Other',
    'organisation_type_plural': 'Publicly funded charities',
    'organisation_type_singular': 'Publicly funded charity'
  },
  'duchy': {
    'organisation_category': 'Other',
    'organisation_type_plural': 'Royal duchies',
    'organisation_type_singular': 'Royal duchy'
  },
  'foi_voluntary': {
    'organisation_category': 'Other',
    'organisation_type_plural': 'Voluntary',
    'organisation_type_singular': 'Voluntary'
  },
  'sport': {
    'organisation_category': 'Recreation',
    'organisation_type_plural': 'Sport',
    'organisation_type_singular': 'Sport'
  },
  'theatre': {
    'organisation_category': 'Recreation',
    'organisation_type_plural': 'Theatre',
    'organisation_type_singular': 'Theatre'
  },
  'dance': {
    'organisation_category': 'Recreation',
    'organisation_type_plural': 'Dance',
    'organisation_type_singular': 'Dance'
  },
  'airport': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Airport companies',
    'organisation_type_singular': 'Airport company'
  },
  'bus_company': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Bus companies',
    'organisation_type_singular': 'Bus company'
  },
  'public_infrastructure': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Companies controlling national infrastructure',
    'organisation_type_singular': 'Company controlling national infrastructure'
  },
  'navigation_authority': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Navigation authorities',
    'organisation_type_singular': 'Navigation authority'
  },
  'npte': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Passenger transport executives',
    'organisation_type_singular': 'Passenger transport executive'
  },
  'port_authority': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Port authorities',
    'organisation_type_singular': 'Port authority'
  },
  'railways': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Railway companies',
    'organisation_type_singular': 'Railway companie'
  },
  'srp': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Safer Roads Partnership',
    'organisation_type_singular': 'Safer Roads Partnership'
  },
  'toll_company': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Toll companies',
    'organisation_type_singular': 'Toll company'
  },
  'trunk_road_agency': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Trunk road agencies (Wales)',
    'organisation_type_singular': 'Trunk road agency (Wales)'
  },
  'telecom_companies': {
    'organisation_category': 'Transport and infrastructure',
    'organisation_type_plural': 'Telecommunications Company',
    'organisation_type_singular': 'Telecommunications Company'
  }
}
