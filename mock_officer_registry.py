# -*- coding: utf-8 -*-
"""
AgriFlow Demo Agriculture Officer Registry
=========================================
IMPORTANT PROTOTYPE NOTICE:
This dataset is strictly for demonstration and testing of AgriFlow (SIH prototype).
These are fictional/demo records and DO NOT represent real government officers,
nor are they sourced from an official government database.
All phone numbers are fictional demo placeholders.
"""

MOCK_OFFICER_REGISTRY = [
    # --- Tamil Nadu ---
    {
        "officer_id": "AGRI-TN-0001",
        "full_name": "Ravi Kumar",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Tamil Nadu",
        "district": "Salem",
        "working_place": "Sankari",
        "mobile": "9876543210",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-TN-0002",
        "full_name": "Priya Devi",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Tamil Nadu",
        "district": "Krishnagiri",
        "working_place": "Hosur",
        "mobile": "9876543211",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-TN-0003",
        "full_name": "Senthil Nathan",
        "designation": "District Agriculture Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Tamil Nadu",
        "district": "Coimbatore",
        "working_place": "Pollachi",
        "mobile": "9876543212",
        "status": "ACTIVE"
    },

    # --- Karnataka ---
    {
        "officer_id": "AGRI-KA-0001",
        "full_name": "Ramesh Gowda",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Karnataka",
        "district": "Mandya",
        "working_place": "Pandavapura",
        "mobile": "9876543213",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-KA-0002",
        "full_name": "Ananya Hegde",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Karnataka",
        "district": "Mysuru",
        "working_place": "Nanjangud",
        "mobile": "9876543214",
        "status": "ACTIVE"
    },

    # --- Kerala ---
    {
        "officer_id": "AGRI-KL-0001",
        "full_name": "Suresh Menon",
        "designation": "Agricultural Field Officer",
        "department": "Department of Agriculture Development & Farmers' Welfare",
        "state": "Kerala",
        "district": "Palakkad",
        "working_place": "Alathur",
        "mobile": "9876543215",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-KL-0002",
        "full_name": "Mini Thomas",
        "designation": "Assistant Director of Agriculture",
        "department": "Department of Agriculture Development & Farmers' Welfare",
        "state": "Kerala",
        "district": "Wayanad",
        "working_place": "Kalpetta",
        "mobile": "9876543216",
        "status": "ACTIVE"
    },

    # --- Andhra Pradesh ---
    {
        "officer_id": "AGRI-AP-0001",
        "full_name": "M. Venkata Rao",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Andhra Pradesh",
        "district": "Guntur",
        "working_place": "Tenali",
        "mobile": "9876543217",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-AP-0002",
        "full_name": "K. Lakshmi Prasanna",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Andhra Pradesh",
        "district": "Krishna",
        "working_place": "Gudivada",
        "mobile": "9876543218",
        "status": "ACTIVE"
    },

    # --- Telangana ---
    {
        "officer_id": "AGRI-TS-0001",
        "full_name": "K. Srinivas Reddy",
        "designation": "Agriculture Extension Officer",
        "department": "Department of Agriculture",
        "state": "Telangana",
        "district": "Warangal",
        "working_place": "Narsampet",
        "mobile": "9876543219",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-TS-0002",
        "full_name": "Swapna Rani",
        "designation": "Mandal Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Telangana",
        "district": "Nizamabad",
        "working_place": "Armoor",
        "mobile": "9876543220",
        "status": "ACTIVE"
    },

    # --- Maharashtra ---
    {
        "officer_id": "AGRI-MH-0001",
        "full_name": "Sachin Patil",
        "designation": "Taluka Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Maharashtra",
        "district": "Nashik",
        "working_place": "Niphad",
        "mobile": "9876543221",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-MH-0002",
        "full_name": "Vandana Deshmukh",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Maharashtra",
        "district": "Pune",
        "working_place": "Baramati",
        "mobile": "9876543222",
        "status": "ACTIVE"
    },

    # --- Gujarat ---
    {
        "officer_id": "AGRI-GJ-0001",
        "full_name": "Bhavesh Patel",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture, Farmers Welfare & Co-operation",
        "state": "Gujarat",
        "district": "Anand",
        "working_place": "Borsad",
        "mobile": "9876543223",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-GJ-0002",
        "full_name": "Chetna Solanki",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture, Farmers Welfare & Co-operation",
        "state": "Gujarat",
        "district": "Rajkot",
        "working_place": "Gondal",
        "mobile": "9876543224",
        "status": "ACTIVE"
    },

    # --- Rajasthan ---
    {
        "officer_id": "AGRI-RJ-0001",
        "full_name": "Mahendra Singh",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Rajasthan",
        "district": "Jaipur",
        "working_place": "Chomu",
        "mobile": "9876543225",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-RJ-0002",
        "full_name": "Sunita Meena",
        "designation": "Agriculture Supervisor",
        "department": "Department of Agriculture",
        "state": "Rajasthan",
        "district": "Alwar",
        "working_place": "Behror",
        "mobile": "9876543226",
        "status": "ACTIVE"
    },

    # --- Punjab ---
    {
        "officer_id": "AGRI-PB-0001",
        "full_name": "Gurpreet Singh",
        "designation": "Agriculture Development Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Punjab",
        "district": "Ludhiana",
        "working_place": "Khanna",
        "mobile": "9876543227",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-PB-0002",
        "full_name": "Harpreet Kaur",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Punjab",
        "district": "Jalandhar",
        "working_place": "Nakodar",
        "mobile": "9876543228",
        "status": "ACTIVE"
    },

    # --- Haryana ---
    {
        "officer_id": "AGRI-HR-0001",
        "full_name": "Vikas Sharma",
        "designation": "Sub Divisional Agriculture Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Haryana",
        "district": "Karnal",
        "working_place": "Nilokheri",
        "mobile": "9876543229",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-HR-0002",
        "full_name": "Ritu Malik",
        "designation": "Agriculture Development Officer",
        "department": "Department of Agriculture & Farmers Welfare",
        "state": "Haryana",
        "district": "Kurukshetra",
        "working_place": "Pehowa",
        "mobile": "9876543230",
        "status": "ACTIVE"
    },

    # --- Uttar Pradesh ---
    {
        "officer_id": "AGRI-UP-0001",
        "full_name": "Amit Tripathi",
        "designation": "Block Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Uttar Pradesh",
        "district": "Varanasi",
        "working_place": "Pindra",
        "mobile": "9876543231",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-UP-0002",
        "full_name": "Pratibha Verma",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Uttar Pradesh",
        "district": "Barabanki",
        "working_place": "Fatehpur",
        "mobile": "9876543232",
        "status": "ACTIVE"
    },

    # --- West Bengal ---
    {
        "officer_id": "AGRI-WB-0001",
        "full_name": "Sourav Mukherjee",
        "designation": "Assistant Director of Agriculture",
        "department": "Department of Agriculture",
        "state": "West Bengal",
        "district": "Hooghly",
        "working_place": "Singur",
        "mobile": "9876543233",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-WB-0002",
        "full_name": "Anindita Das",
        "designation": "Agriculture Development Officer",
        "department": "Department of Agriculture",
        "state": "West Bengal",
        "district": "Nadia",
        "working_place": "Ranaghat",
        "mobile": "9876543234",
        "status": "ACTIVE"
    },

    # --- Odisha ---
    {
        "officer_id": "AGRI-OR-0001",
        "full_name": "Biswajit Nayak",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture & Farmers' Empowerment",
        "state": "Odisha",
        "district": "Cuttack",
        "working_place": "Athagarh",
        "mobile": "9876543235",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-OR-0002",
        "full_name": "Rashmita Mohanty",
        "designation": "Block Agriculture Officer",
        "department": "Department of Agriculture & Farmers' Empowerment",
        "state": "Odisha",
        "district": "Puri",
        "working_place": "Pipili",
        "mobile": "9876543236",
        "status": "ACTIVE"
    },

    # --- Bihar ---
    {
        "officer_id": "AGRI-BR-0001",
        "full_name": "Rajesh Kumar",
        "designation": "Block Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Bihar",
        "district": "Nalanda",
        "working_place": "Biharsharif",
        "mobile": "9876543237",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-BR-0002",
        "full_name": "Rekha Kumari",
        "designation": "Agriculture Coordinator",
        "department": "Department of Agriculture",
        "state": "Bihar",
        "district": "Muzaffarpur",
        "working_place": "Motipur",
        "mobile": "9876543238",
        "status": "ACTIVE"
    },

    # --- Assam ---
    {
        "officer_id": "AGRI-AS-0001",
        "full_name": "Diganta Gogoi",
        "designation": "Agriculture Development Officer",
        "department": "Directorate of Agriculture",
        "state": "Assam",
        "district": "Jorhat",
        "working_place": "Titabor",
        "mobile": "9876543239",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-AS-0002",
        "full_name": "Priyanka Sarma",
        "designation": "Assistant Director of Agriculture",
        "department": "Directorate of Agriculture",
        "state": "Assam",
        "district": "Kamrup",
        "working_place": "Hajo",
        "mobile": "9876543240",
        "status": "ACTIVE"
    },

    # --- Madhya Pradesh ---
    {
        "officer_id": "AGRI-MP-0001",
        "full_name": "Arvind Chouhan",
        "designation": "Rural Agriculture Extension Officer",
        "department": "Farmer Welfare & Agriculture Development",
        "state": "Madhya Pradesh",
        "district": "Indore",
        "working_place": "Sanwer",
        "mobile": "9876543241",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-MP-0002",
        "full_name": "Maya Lodhi",
        "designation": "Senior Agriculture Development Officer",
        "department": "Farmer Welfare & Agriculture Development",
        "state": "Madhya Pradesh",
        "district": "Sehore",
        "working_place": "Ashta",
        "mobile": "9876543242",
        "status": "ACTIVE"
    },

    # --- Chhattisgarh ---
    {
        "officer_id": "AGRI-CG-0001",
        "full_name": "Bhupendra Baghel",
        "designation": "Rural Agriculture Extension Officer",
        "department": "Department of Agriculture Development & Farmer Welfare",
        "state": "Chhattisgarh",
        "district": "Durg",
        "working_place": "Patan",
        "mobile": "9876543243",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-CG-0002",
        "full_name": "Deepa Sahu",
        "designation": "Assistant Director of Agriculture",
        "department": "Department of Agriculture Development & Farmer Welfare",
        "state": "Chhattisgarh",
        "district": "Raipur",
        "working_place": "Abhanpur",
        "mobile": "9876543244",
        "status": "ACTIVE"
    },

    # --- Jharkhand ---
    {
        "officer_id": "AGRI-JH-0001",
        "full_name": "Binod Tirkey",
        "designation": "Block Agriculture Officer",
        "department": "Department of Agriculture, Animal Husbandry & Co-operative",
        "state": "Jharkhand",
        "district": "Ranchi",
        "working_place": "Ormanjhi",
        "mobile": "9876543245",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-JH-0002",
        "full_name": "Renu Devi",
        "designation": "Agriculture Extension Officer",
        "department": "Department of Agriculture, Animal Husbandry & Co-operative",
        "state": "Jharkhand",
        "district": "Hazaribagh",
        "working_place": "Barhi",
        "mobile": "9876543246",
        "status": "ACTIVE"
    },

    # --- Uttarakhand ---
    {
        "officer_id": "AGRI-UK-0001",
        "full_name": "Deepak Rawat",
        "designation": "Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Uttarakhand",
        "district": "Dehradun",
        "working_place": "Vikasnagar",
        "mobile": "9876543247",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-UK-0002",
        "full_name": "Meenakshi Joshi",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Uttarakhand",
        "district": "Udham Singh Nagar",
        "working_place": "Kashipur",
        "mobile": "9876543248",
        "status": "ACTIVE"
    },

    # --- Himachal Pradesh ---
    {
        "officer_id": "AGRI-HP-0001",
        "full_name": "Rohit Thakur",
        "designation": "Agriculture Development Officer",
        "department": "Department of Agriculture",
        "state": "Himachal Pradesh",
        "district": "Shimla",
        "working_place": "Theog",
        "mobile": "9876543249",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-HP-0002",
        "full_name": "Neha Sharma",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture",
        "state": "Himachal Pradesh",
        "district": "Kangra",
        "working_place": "Palampur",
        "mobile": "9876543250",
        "status": "ACTIVE"
    },

    # --- Delhi ---
    {
        "officer_id": "AGRI-DL-0001",
        "full_name": "Arvind Verma",
        "designation": "Agricultural Officer",
        "department": "Development Department (Agriculture Unit)",
        "state": "Delhi",
        "district": "North West Delhi",
        "working_place": "Alipur",
        "mobile": "9876543251",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-DL-0002",
        "full_name": "Kavita Singh",
        "designation": "Extension Specialist",
        "department": "Development Department (Agriculture Unit)",
        "state": "Delhi",
        "district": "South West Delhi",
        "working_place": "Najafgarh",
        "mobile": "9876543252",
        "status": "ACTIVE"
    },

    # --- Jammu & Kashmir ---
    {
        "officer_id": "AGRI-JK-0001",
        "full_name": "Tariq Ahmed Mir",
        "designation": "Agriculture Extension Officer",
        "department": "Department of Agriculture Production & Farmers Welfare",
        "state": "Jammu & Kashmir",
        "district": "Baramulla",
        "working_place": "Sopore",
        "mobile": "9876543253",
        "status": "ACTIVE"
    },
    {
        "officer_id": "AGRI-JK-0002",
        "full_name": "Sunita Rani",
        "designation": "Assistant Agriculture Officer",
        "department": "Department of Agriculture Production & Farmers Welfare",
        "state": "Jammu & Kashmir",
        "district": "Jammu",
        "working_place": "RS Pura",
        "mobile": "9876543254",
        "status": "ACTIVE"
    }
]
