"""Seed data for IIT Jammu catalog backend.
Kept in Python for easy import; mirrors the frontend mock shape.
"""

NAV_TREE = [
    {
        "slug": "information-about-iitjammu",
        "label": "Information about IIT Jammu",
        "children": [
            {"slug": "mission-and-vision", "label": "Mission and Vision"},
            {"slug": "history", "label": "History of IIT Jammu"},
            {"slug": "accreditation", "label": "Accreditation"},
            {"slug": "campus-life", "label": "Campus Life"},
        ],
    },
    {
        "slug": "programs-of-study-and-degree-requirements",
        "label": "Programs of Study and Degree Requirements",
        "children": [
            {"slug": "btech-programs", "label": "B.Tech Programs"},
            {"slug": "mtech-programs", "label": "M.Tech Programs"},
            {"slug": "msc-programs", "label": "M.Sc. Programs"},
            {"slug": "phd-programs", "label": "Ph.D. Programs"},
            {"slug": "minor-programs", "label": "Minor / Honors Programs"},
        ],
    },
    {
        "slug": "courses-credits-hours",
        "label": "Courses, Credits, Hours",
        "children": [
            {"slug": "cse-computer-science-engineering", "label": "CSE - Computer Science & Engineering"},
            {"slug": "ece-electronics-communication", "label": "ECE - Electronics & Communication"},
            {"slug": "ee-electrical-engineering", "label": "EE - Electrical Engineering"},
            {"slug": "me-mechanical-engineering", "label": "ME - Mechanical Engineering"},
            {"slug": "ce-civil-engineering", "label": "CE - Civil Engineering"},
            {"slug": "che-chemical-engineering", "label": "ChE - Chemical Engineering"},
            {"slug": "mse-materials-engineering", "label": "MSE - Materials Science & Engineering"},
            {"slug": "mth-mathematics", "label": "MTH - Mathematics"},
            {"slug": "phy-physics", "label": "PHY - Physics"},
            {"slug": "chm-chemistry", "label": "CHM - Chemistry"},
            {"slug": "hss-humanities-social-sciences", "label": "HSS - Humanities & Social Sciences"},
            {"slug": "co-curriculars", "label": "Co-curriculars"},
        ],
    },
    {
        "slug": "faculty",
        "label": "Faculty",
        "children": [
            {"slug": "leadership", "label": "Institute Leadership"},
            {"slug": "cse-faculty", "label": "CSE Faculty"},
            {"slug": "ece-faculty", "label": "ECE Faculty"},
            {"slug": "me-faculty", "label": "ME Faculty"},
            {"slug": "sciences-faculty", "label": "Sciences & HSS Faculty"},
        ],
    },
    {"slug": "academic-calendar", "label": "Academic Calendar"},
    {
        "slug": "fees-and-financial-aid",
        "label": "Fees and Financial Aid",
        "children": [
            {"slug": "tuition-fees", "label": "Tuition & Fees"},
            {"slug": "hostel-mess", "label": "Hostel & Mess Charges"},
            {"slug": "scholarships", "label": "Scholarships & Aid"},
        ],
    },
    {
        "slug": "academic-policies-and-procedures",
        "label": "Academic Policies and Procedures",
        "children": [
            {"slug": "admission-policies", "label": "Admission Policies"},
            {"slug": "grading-system", "label": "Grading System"},
            {"slug": "attendance", "label": "Attendance Requirements"},
            {"slug": "academic-integrity", "label": "Academic Integrity"},
        ],
    },
    {"slug": "table-of-contents", "label": "Table of Contents"},
]

CATALOG_VERSIONS = [
    "Catalog 2025-26",
    "Student Handbook 2025-26",
    "Catalog 2024-25",
    "Student Handbook 2024-25",
    "Catalog 2023-24",
    "Student Handbook 2023-24",
    "Catalog 2022-23",
    "Catalog 2021-22",
    "Catalog 2020-21",
    "Catalog 2019-20",
    "Catalog 2018-19",
    "Catalog 2017-18",
    "Catalog 2016-17",
]

DEPARTMENTS = [
    {
        "slug": "cse-computer-science-engineering",
        "code": "CSE",
        "name": "Computer Science & Engineering",
        "description": "The Department of Computer Science and Engineering at IIT Jammu offers a comprehensive curriculum spanning algorithms, systems, AI/ML, and emerging areas such as quantum computing and cyber-physical systems, with a strong emphasis on research and innovation.",
        "courses": [
            {"code": "CSL1010", "title": "Introduction to Computer Programming", "credits": 4, "hours": "3-2-6", "desc": "Programming fundamentals in C/Python, problem solving, data types, control flow, functions."},
            {"code": "CSL2010", "title": "Data Structures and Algorithms", "credits": 4, "hours": "3-2-6", "desc": "Arrays, linked lists, trees, graphs, hashing; complexity analysis; algorithmic paradigms."},
            {"code": "CSL2020", "title": "Discrete Mathematics", "credits": 4, "hours": "4-0-8", "desc": "Logic, sets, relations, functions, combinatorics, graph theory, number theory."},
            {"code": "CSL2030", "title": "Computer Organization & Architecture", "credits": 4, "hours": "3-2-6", "desc": "Digital logic, instruction set architecture, pipelining, memory hierarchy, I/O."},
            {"code": "CSL3010", "title": "Operating Systems", "credits": 4, "hours": "3-2-6", "desc": "Processes, threads, scheduling, synchronization, memory and file systems."},
            {"code": "CSL3020", "title": "Database Management Systems", "credits": 4, "hours": "3-2-6", "desc": "Relational model, SQL, normalization, transactions, indexing, query optimization."},
            {"code": "CSL3030", "title": "Computer Networks", "credits": 4, "hours": "3-2-6", "desc": "OSI/TCP-IP, link layer, routing, transport, application protocols, network security."},
            {"code": "CSL3040", "title": "Design and Analysis of Algorithms", "credits": 4, "hours": "4-0-8", "desc": "Greedy, divide-and-conquer, DP, graph algorithms, NP-completeness, approximation."},
            {"code": "CSL3050", "title": "Theory of Computation", "credits": 4, "hours": "4-0-8", "desc": "Automata, regular and context-free languages, Turing machines, decidability."},
            {"code": "CSL4010", "title": "Machine Learning", "credits": 4, "hours": "3-2-6", "desc": "Regression, classification, clustering, neural networks, model evaluation."},
            {"code": "CSL4020", "title": "Artificial Intelligence", "credits": 4, "hours": "4-0-8", "desc": "Search, knowledge representation, planning, reasoning under uncertainty."},
            {"code": "CSL4030", "title": "Compilers", "credits": 4, "hours": "3-2-6", "desc": "Lexical analysis, parsing, semantic analysis, code generation and optimization."},
            {"code": "CSP4090", "title": "B.Tech Project I", "credits": 6, "hours": "0-6-12", "desc": "Year-long capstone project: problem statement, design, prototype."},
            {"code": "CSP4099", "title": "B.Tech Project II", "credits": 6, "hours": "0-6-12", "desc": "Completion of capstone: implementation, evaluation, thesis, defense."},
        ],
    },
    {
        "slug": "ece-electronics-communication",
        "code": "ECE",
        "name": "Electronics & Communication Engineering",
        "description": "ECE at IIT Jammu emphasizes design of analog and digital systems, signal and image processing, VLSI, embedded systems, and modern wireless communication networks.",
        "courses": [
            {"code": "ECL1010", "title": "Basic Electronics", "credits": 4, "hours": "3-2-6", "desc": "Semiconductor devices, diodes, BJTs, MOSFETs, amplifiers, oscillators."},
            {"code": "ECL2010", "title": "Digital System Design", "credits": 4, "hours": "3-2-6", "desc": "Combinational and sequential logic, FSMs, Verilog HDL, FPGA implementation."},
            {"code": "ECL2020", "title": "Signals and Systems", "credits": 4, "hours": "4-0-8", "desc": "Continuous and discrete-time signals, Fourier and Laplace transforms, LTI systems."},
            {"code": "ECL2030", "title": "Network Analysis", "credits": 4, "hours": "3-2-6", "desc": "Nodal and mesh analysis, theorems, transients, two-port networks."},
            {"code": "ECL3010", "title": "Analog Circuits", "credits": 4, "hours": "3-2-6", "desc": "Op-amps, feedback, filters, oscillators, data converters."},
            {"code": "ECL3020", "title": "Communication Systems", "credits": 4, "hours": "3-2-6", "desc": "Analog and digital modulation, noise, information theory, channel coding."},
            {"code": "ECL3030", "title": "Embedded Systems", "credits": 4, "hours": "3-2-6", "desc": "ARM Cortex microcontrollers, real-time systems, hardware-software co-design."},
            {"code": "ECL3040", "title": "VLSI Design", "credits": 4, "hours": "3-2-6", "desc": "CMOS circuits, layout, ASIC flow, low-power design techniques."},
            {"code": "ECL4010", "title": "Wireless Communications", "credits": 4, "hours": "4-0-8", "desc": "Fading channels, OFDM, MIMO, modern cellular standards (4G/5G)."},
            {"code": "ECP4099", "title": "ECE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Year-long senior capstone in electronics and communications."},
        ],
    },
    {
        "slug": "ee-electrical-engineering",
        "code": "EE",
        "name": "Electrical Engineering",
        "description": "Electrical Engineering at IIT Jammu addresses power systems, control, electric drives, renewable energy, and smart grids \u2014 with strong industry and research linkages.",
        "courses": [
            {"code": "EEL1010", "title": "Basic Electrical Engineering", "credits": 4, "hours": "3-2-6", "desc": "DC and AC circuits, transformers, machines, measuring instruments."},
            {"code": "EEL2010", "title": "Electromagnetic Theory", "credits": 4, "hours": "4-0-8", "desc": "Maxwell's equations, wave propagation, transmission lines."},
            {"code": "EEL2020", "title": "Electric Machines", "credits": 4, "hours": "3-2-6", "desc": "DC, induction, and synchronous machines; transformers; modeling."},
            {"code": "EEL3010", "title": "Control Systems", "credits": 4, "hours": "4-0-8", "desc": "Time and frequency response, stability, PID controllers, state-space."},
            {"code": "EEL3020", "title": "Power Systems", "credits": 4, "hours": "4-0-8", "desc": "Generation, transmission, distribution, load flow, fault analysis."},
            {"code": "EEL3030", "title": "Power Electronics", "credits": 4, "hours": "3-2-6", "desc": "Rectifiers, inverters, choppers, motor drives."},
            {"code": "EEL4010", "title": "Renewable Energy Systems", "credits": 4, "hours": "3-2-6", "desc": "Solar PV, wind, energy storage, grid integration."},
            {"code": "EEP4099", "title": "EE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Electrical engineering senior capstone."},
        ],
    },
    {
        "slug": "me-mechanical-engineering",
        "code": "ME",
        "name": "Mechanical Engineering",
        "description": "Mechanical Engineering at IIT Jammu covers solid and fluid mechanics, thermodynamics, manufacturing, robotics, and computational design.",
        "courses": [
            {"code": "MEL1010", "title": "Engineering Mechanics", "credits": 4, "hours": "4-0-8", "desc": "Statics and dynamics of particles and rigid bodies."},
            {"code": "MEL1020", "title": "Engineering Graphics & CAD", "credits": 3, "hours": "1-4-4", "desc": "Orthographic projection, CAD modeling using SolidWorks."},
            {"code": "MEL2010", "title": "Thermodynamics", "credits": 4, "hours": "4-0-8", "desc": "Laws of thermodynamics, cycles, properties of pure substances."},
            {"code": "MEL2020", "title": "Fluid Mechanics", "credits": 4, "hours": "3-2-6", "desc": "Fluid statics, kinematics, dynamics, dimensional analysis."},
            {"code": "MEL2030", "title": "Strength of Materials", "credits": 4, "hours": "4-0-8", "desc": "Stress, strain, torsion, bending, deflection."},
            {"code": "MEL3010", "title": "Machine Design", "credits": 4, "hours": "3-2-6", "desc": "Stress analysis, design of shafts, gears, bearings."},
            {"code": "MEL3020", "title": "Manufacturing Processes", "credits": 4, "hours": "3-2-6", "desc": "Casting, forming, machining, joining, additive manufacturing."},
            {"code": "MEL3030", "title": "Heat & Mass Transfer", "credits": 4, "hours": "4-0-8", "desc": "Conduction, convection, radiation, heat exchangers."},
            {"code": "MEL4010", "title": "Robotics", "credits": 4, "hours": "3-2-6", "desc": "Kinematics, dynamics, control of robotic manipulators."},
            {"code": "MEP4099", "title": "ME Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Mechanical engineering senior capstone project."},
        ],
    },
    {
        "slug": "ce-civil-engineering",
        "code": "CE",
        "name": "Civil Engineering",
        "description": "Civil Engineering at IIT Jammu prepares students for the design and construction of resilient infrastructure, sustainable buildings, transportation, and water resources.",
        "courses": [
            {"code": "CEL1010", "title": "Surveying", "credits": 4, "hours": "3-2-6", "desc": "Chain, compass, theodolite, total station, GPS surveying."},
            {"code": "CEL2010", "title": "Strength of Materials", "credits": 4, "hours": "4-0-8", "desc": "Stress, strain, bending, torsion, deflection of beams."},
            {"code": "CEL2020", "title": "Fluid Mechanics & Hydraulics", "credits": 4, "hours": "3-2-6", "desc": "Fluid statics, kinematics, open-channel flow, pipe networks."},
            {"code": "CEL2030", "title": "Structural Analysis", "credits": 4, "hours": "4-0-8", "desc": "Analysis of determinate and indeterminate structures."},
            {"code": "CEL3010", "title": "Concrete Technology", "credits": 4, "hours": "3-2-6", "desc": "Cement, aggregates, mix design, durability."},
            {"code": "CEL3020", "title": "Geotechnical Engineering", "credits": 4, "hours": "3-2-6", "desc": "Soil mechanics, foundation engineering, slope stability."},
            {"code": "CEL3030", "title": "Transportation Engineering", "credits": 4, "hours": "3-2-6", "desc": "Highway geometric design, pavements, traffic engineering."},
            {"code": "CEP4099", "title": "CE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Civil engineering capstone design project."},
        ],
    },
    {
        "slug": "che-chemical-engineering",
        "code": "ChE",
        "name": "Chemical Engineering",
        "description": "Chemical Engineering at IIT Jammu integrates process design, transport phenomena, reaction engineering, and sustainable process technology.",
        "courses": [
            {"code": "CHL1010", "title": "Chemical Process Calculations", "credits": 4, "hours": "3-2-6", "desc": "Material and energy balances, units, process variables."},
            {"code": "CHL2010", "title": "Fluid Flow Operations", "credits": 4, "hours": "3-2-6", "desc": "Fluid statics and dynamics, pumps, flow through packed beds."},
            {"code": "CHL2020", "title": "Chemical Reaction Engineering", "credits": 4, "hours": "4-0-8", "desc": "Reactor design, kinetics, ideal and non-ideal reactors."},
            {"code": "CHL3010", "title": "Mass Transfer Operations", "credits": 4, "hours": "3-2-6", "desc": "Diffusion, absorption, distillation, extraction."},
            {"code": "CHL3020", "title": "Process Control", "credits": 4, "hours": "3-2-6", "desc": "Dynamics of chemical processes, PID, advanced control."},
            {"code": "CHP4099", "title": "ChE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Year-long process design and analysis project."},
        ],
    },
    {
        "slug": "mse-materials-engineering",
        "code": "MSE",
        "name": "Materials Science & Engineering",
        "description": "Materials Science & Engineering covers structure-property relationships in metals, ceramics, polymers, and composites, with a focus on nano-materials and energy materials.",
        "courses": [
            {"code": "MSL1010", "title": "Introduction to Materials", "credits": 4, "hours": "3-2-6", "desc": "Bonding, crystal structures, defects, microstructure."},
            {"code": "MSL2010", "title": "Thermodynamics of Materials", "credits": 4, "hours": "4-0-8", "desc": "Phase diagrams, free energy, transformations."},
            {"code": "MSL3010", "title": "Mechanical Behavior of Materials", "credits": 4, "hours": "3-2-6", "desc": "Elasticity, plasticity, fracture, fatigue, creep."},
            {"code": "MSL3020", "title": "Electronic and Magnetic Materials", "credits": 4, "hours": "4-0-8", "desc": "Semiconductors, dielectrics, magnetic materials and applications."},
            {"code": "MSP4099", "title": "MSE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Materials engineering capstone research/design project."},
        ],
    },
    {
        "slug": "mth-mathematics",
        "code": "MTH",
        "name": "Mathematics",
        "description": "Mathematics courses build rigorous foundations in analysis, algebra, probability, and computation that support all engineering and science programs at IIT Jammu.",
        "courses": [
            {"code": "MAL1010", "title": "Calculus I", "credits": 4, "hours": "4-0-8", "desc": "Limits, derivatives, applications, integrals."},
            {"code": "MAL1020", "title": "Calculus II", "credits": 4, "hours": "4-0-8", "desc": "Sequences, series, multivariable and vector calculus."},
            {"code": "MAL2010", "title": "Linear Algebra", "credits": 4, "hours": "4-0-8", "desc": "Vectors, matrices, linear transformations, eigenvalues."},
            {"code": "MAL2020", "title": "Differential Equations", "credits": 4, "hours": "4-0-8", "desc": "ODEs, systems of ODEs, introduction to PDEs."},
            {"code": "MAL3010", "title": "Probability & Statistics", "credits": 4, "hours": "4-0-8", "desc": "Random variables, distributions, hypothesis testing, regression."},
            {"code": "MAL3020", "title": "Numerical Methods", "credits": 4, "hours": "3-2-6", "desc": "Root finding, interpolation, numerical integration, ODE solvers."},
            {"code": "MAL4010", "title": "Optimization", "credits": 4, "hours": "4-0-8", "desc": "Linear, nonlinear, and integer optimization with applications."},
        ],
    },
    {
        "slug": "phy-physics",
        "code": "PHY",
        "name": "Physics",
        "description": "Physics at IIT Jammu provides core foundations in mechanics, electromagnetism, quantum mechanics, and modern applied physics including photonics and condensed matter.",
        "courses": [
            {"code": "PHL1010", "title": "Physics I: Mechanics & Waves", "credits": 4, "hours": "3-2-6", "desc": "Newtonian and Lagrangian mechanics, oscillations, waves."},
            {"code": "PHL1020", "title": "Physics II: Electromagnetism", "credits": 4, "hours": "3-2-6", "desc": "Electrostatics, magnetism, Maxwell's equations."},
            {"code": "PHL2010", "title": "Quantum Mechanics", "credits": 4, "hours": "4-0-8", "desc": "Schr\u00f6dinger equation, operators, harmonic oscillator, hydrogen atom."},
            {"code": "PHL3010", "title": "Statistical Mechanics", "credits": 4, "hours": "4-0-8", "desc": "Ensembles, partition functions, thermodynamics of systems."},
            {"code": "PHL3020", "title": "Condensed Matter Physics", "credits": 4, "hours": "4-0-8", "desc": "Crystal lattices, band theory, semiconductors, magnetism."},
        ],
    },
    {
        "slug": "chm-chemistry",
        "code": "CHM",
        "name": "Chemistry",
        "description": "Chemistry at IIT Jammu equips students with foundations in physical, organic, inorganic, and analytical chemistry relevant to engineering and applied science.",
        "courses": [
            {"code": "CYL1010", "title": "Chemistry I", "credits": 4, "hours": "3-2-6", "desc": "Quantum chemistry, bonding, spectroscopy basics."},
            {"code": "CYL1020", "title": "Chemistry II", "credits": 4, "hours": "3-2-6", "desc": "Organic chemistry basics, reaction mechanisms, stereochemistry."},
            {"code": "CYL2010", "title": "Physical Chemistry", "credits": 4, "hours": "4-0-8", "desc": "Thermodynamics, kinetics, electrochemistry."},
            {"code": "CYL3010", "title": "Analytical Chemistry", "credits": 4, "hours": "3-2-6", "desc": "Chromatography, spectroscopy, electroanalytical methods."},
        ],
    },
    {
        "slug": "hss-humanities-social-sciences",
        "code": "HSS",
        "name": "Humanities & Social Sciences",
        "description": "HSS courses develop communication, ethical reasoning, economics, and history \u2014 producing well-rounded engineers and scientists.",
        "courses": [
            {"code": "HUL1010", "title": "Technical Communication", "credits": 3, "hours": "3-0-6", "desc": "Writing, presentation, and professional communication."},
            {"code": "HUL2010", "title": "Engineering Economics", "credits": 3, "hours": "3-0-6", "desc": "Time value of money, project evaluation, cost analysis."},
            {"code": "HUL2020", "title": "Ethics in Engineering", "credits": 3, "hours": "3-0-6", "desc": "Professional responsibility, case studies in ethics."},
            {"code": "HUL3010", "title": "Entrepreneurship", "credits": 3, "hours": "2-2-5", "desc": "Idea generation, business models, lean startup, funding."},
            {"code": "HUL3020", "title": "History of Science & Technology", "credits": 3, "hours": "3-0-6", "desc": "Cultural and contextual evolution of science and technology."},
            {"code": "HUL3030", "title": "Psychology", "credits": 3, "hours": "3-0-6", "desc": "Cognition, behavior, social psychology fundamentals."},
        ],
    },
    {
        "slug": "co-curriculars",
        "code": "CC",
        "name": "Co-curriculars",
        "description": "Co-curricular offerings encourage holistic growth through sports, music, robotics teams, debate, and community service. These activities are encouraged but not eligible for academic credit.",
        "courses": [
            {"code": "CC0001", "title": "Robotics Club", "credits": 0, "hours": "0-3-0", "desc": "Build and program robots for inter-IIT and inter-college competitions."},
            {"code": "CC0002", "title": "IIT Jammu Music Ensemble", "credits": 0, "hours": "0-2-0", "desc": "Choir and instrumental ensemble open to all students."},
            {"code": "CC0003", "title": "Community Outreach", "credits": 0, "hours": "0-2-0", "desc": "Outreach programs in nearby villages and schools of Jammu region."},
            {"code": "CC0004", "title": "Sports & Athletics", "credits": 0, "hours": "0-3-0", "desc": "Cricket, football, basketball, athletics, badminton."},
        ],
    },
]

FACULTY_GROUPS = [
    {
        "slug": "leadership",
        "title": "Institute Leadership",
        "intro": "IIT Jammu is led by a Director and supported by Deans across academics, research, faculty affairs, infrastructure, and student welfare.",
        "members": [
            {"name": "Prof. Manoj Singh Gaur", "role": "Director", "email": "director@iitjammu.ac.in", "area": "Cybersecurity, Computer Networks"},
            {"name": "Prof. A. K. Singh", "role": "Dean (Academic Affairs)", "email": "dean.academics@iitjammu.ac.in", "area": "Computer Science"},
            {"name": "Prof. Praveen Kumar", "role": "Dean (Research & Development)", "email": "dean.rnd@iitjammu.ac.in", "area": "Electrical Engineering"},
            {"name": "Prof. Subhadeep Roy", "role": "Dean (Student Welfare)", "email": "dean.sw@iitjammu.ac.in", "area": "Mechanical Engineering"},
            {"name": "Prof. R. K. Verma", "role": "Registrar", "email": "registrar@iitjammu.ac.in", "area": "Administration"},
        ],
    },
    {
        "slug": "cse-faculty",
        "title": "CSE Faculty",
        "intro": "The Computer Science & Engineering department has faculty spanning theory, systems, machine learning, security, and human-computer interaction.",
        "members": [
            {"name": "Dr. Yatindra Nath Singh", "role": "Professor & Head", "email": "hod.cse@iitjammu.ac.in", "area": "Networks, Optical Communication"},
            {"name": "Dr. Karthik Vaidhyanathan", "role": "Associate Professor", "email": "karthik@iitjammu.ac.in", "area": "Software Engineering, AI"},
            {"name": "Dr. Ayan Mondal", "role": "Assistant Professor", "email": "ayan@iitjammu.ac.in", "area": "IoT, Edge Computing"},
            {"name": "Dr. Vinit Jakhetiya", "role": "Assistant Professor", "email": "vinit@iitjammu.ac.in", "area": "Computer Vision, Image Processing"},
            {"name": "Dr. Gaurav Varshney", "role": "Assistant Professor", "email": "gaurav@iitjammu.ac.in", "area": "Cybersecurity, Phishing Detection"},
        ],
    },
    {
        "slug": "ece-faculty",
        "title": "ECE Faculty",
        "intro": "ECE faculty work on VLSI, communications, signal processing, RF and microwave systems, and embedded electronics.",
        "members": [
            {"name": "Dr. Sunil Chinnadurai", "role": "Associate Professor & Head", "email": "hod.ece@iitjammu.ac.in", "area": "5G/6G, Wireless Communications"},
            {"name": "Dr. Subhankar Mishra", "role": "Assistant Professor", "email": "subhankar@iitjammu.ac.in", "area": "Signal Processing"},
            {"name": "Dr. Sparsh Mittal", "role": "Associate Professor", "email": "sparsh@iitjammu.ac.in", "area": "Computer Architecture, GPUs"},
            {"name": "Dr. Khyati Chopra", "role": "Assistant Professor", "email": "khyati@iitjammu.ac.in", "area": "Cooperative Communications"},
        ],
    },
    {
        "slug": "me-faculty",
        "title": "ME Faculty",
        "intro": "Mechanical Engineering faculty research thermofluids, manufacturing, robotics, energy systems, and computational mechanics.",
        "members": [
            {"name": "Dr. Suman Saha", "role": "Associate Professor & Head", "email": "hod.me@iitjammu.ac.in", "area": "CFD, Heat Transfer"},
            {"name": "Dr. Ankur Miglani", "role": "Assistant Professor", "email": "ankur@iitjammu.ac.in", "area": "Multiphase Flows"},
            {"name": "Dr. Mohit Law", "role": "Associate Professor", "email": "mohit@iitjammu.ac.in", "area": "Machine Tool Dynamics"},
            {"name": "Dr. Najeeb-ur-Rehman", "role": "Assistant Professor", "email": "najeeb@iitjammu.ac.in", "area": "Solar Thermal Systems"},
        ],
    },
    {
        "slug": "sciences-faculty",
        "title": "Sciences & HSS Faculty",
        "intro": "Faculty across Mathematics, Physics, Chemistry, and Humanities & Social Sciences support the foundational and contextual education of every IIT Jammu student.",
        "members": [
            {"name": "Dr. Sanjeev Kumar", "role": "Professor, Mathematics", "email": "sanjeev@iitjammu.ac.in", "area": "Numerical Analysis"},
            {"name": "Dr. Ajay Kumar Yagati", "role": "Associate Professor, Physics", "email": "ajay@iitjammu.ac.in", "area": "Bio-sensors"},
            {"name": "Dr. Sandeep Kumar", "role": "Assistant Professor, Chemistry", "email": "sandeep@iitjammu.ac.in", "area": "Materials Chemistry"},
            {"name": "Dr. Anu Sharma", "role": "Assistant Professor, HSS", "email": "anu@iitjammu.ac.in", "area": "Linguistics, English Studies"},
            {"name": "Dr. Vandita Khanna", "role": "Assistant Professor, HSS", "email": "vandita@iitjammu.ac.in", "area": "Economics, Public Policy"},
        ],
    },
]

ACADEMIC_CALENDAR = [
    {
        "term": "Autumn Semester 2024-25",
        "rows": [
            {"event": "Registration for continuing students", "date": "July 22 \u2013 24, 2024"},
            {"event": "Orientation for new students", "date": "July 26 \u2013 30, 2024"},
            {"event": "Classes begin", "date": "August 01, 2024"},
            {"event": "Mid-semester examinations", "date": "September 23 \u2013 28, 2024"},
            {"event": "Mid-semester break", "date": "September 29 \u2013 October 06, 2024"},
            {"event": "Last instruction day", "date": "November 22, 2024"},
            {"event": "End-semester examinations", "date": "November 25 \u2013 December 06, 2024"},
            {"event": "Result declaration", "date": "December 16, 2024"},
            {"event": "Winter vacation", "date": "December 09, 2024 \u2013 January 05, 2025"},
        ],
    },
    {
        "term": "Spring Semester 2024-25",
        "rows": [
            {"event": "Registration", "date": "January 06 \u2013 07, 2025"},
            {"event": "Classes begin", "date": "January 08, 2025"},
            {"event": "Mid-semester examinations", "date": "March 03 \u2013 08, 2025"},
            {"event": "Mid-semester break", "date": "March 09 \u2013 16, 2025"},
            {"event": "Convocation", "date": "April 18, 2025"},
            {"event": "Last instruction day", "date": "May 02, 2025"},
            {"event": "End-semester examinations", "date": "May 05 \u2013 16, 2025"},
            {"event": "Result declaration", "date": "May 26, 2025"},
            {"event": "Summer term begins", "date": "May 27, 2025"},
        ],
    },
]

FEES_DATA = [
    {
        "slug": "tuition-fees",
        "title": "Tuition & Fees",
        "intro": "IIT Jammu fees are set in accordance with the Ministry of Education, Government of India guidelines. The figures below are indicative and may be revised. Please consult the Academic Section for current rates.",
        "tables": [
            {
                "heading": "B.Tech Fees (per semester, INR)",
                "columns": ["Component", "General/OBC", "SC/ST/PwD"],
                "rows": [
                    ["Tuition Fee", "\u20b91,00,000", "Exempt"],
                    ["Examination Fee", "\u20b9750", "\u20b9750"],
                    ["Registration Fee", "\u20b9500", "\u20b9500"],
                    ["Gymkhana Fee", "\u20b91,000", "\u20b91,000"],
                    ["Medical Fee", "\u20b9500", "\u20b9500"],
                    ["One-time Admission Fee (first semester only)", "\u20b96,500", "\u20b96,500"],
                ],
            },
            {
                "heading": "M.Tech Fees (per semester, INR)",
                "columns": ["Component", "Amount"],
                "rows": [
                    ["Tuition Fee", "\u20b95,000"],
                    ["Examination Fee", "\u20b9750"],
                    ["Registration Fee", "\u20b9500"],
                    ["Gymkhana / Other", "\u20b91,500"],
                ],
            },
        ],
    },
    {
        "slug": "hostel-mess",
        "title": "Hostel & Mess Charges",
        "intro": "Most undergraduate and graduate students reside on campus. Hostel and mess charges are payable per semester.",
        "tables": [
            {
                "heading": "Hostel & Mess (per semester, INR)",
                "columns": ["Component", "Amount"],
                "rows": [
                    ["Hostel Seat Rent", "\u20b96,000"],
                    ["Establishment Charges", "\u20b95,500"],
                    ["Mess Advance", "\u20b922,000"],
                    ["Electricity & Water (estimate)", "\u20b93,000"],
                ],
            }
        ],
    },
    {
        "slug": "scholarships",
        "title": "Scholarships & Financial Aid",
        "intro": "IIT Jammu offers merit-cum-means scholarships, MCM tuition waivers, institute free studentships, and ST/SC fellowships, alongside several externally sponsored awards.",
        "tables": [
            {
                "heading": "Major Scholarship Schemes",
                "columns": ["Scheme", "Eligibility", "Benefit"],
                "rows": [
                    ["Merit-cum-Means (MCM)", "Family income < \u20b94.5 LPA", "Tuition waiver + \u20b91,000/month"],
                    ["SC/ST Fellowship", "SC/ST B.Tech students", "Tuition exemption + monthly stipend"],
                    ["Institute Free Studentship", "Top 25% by CGPA, need-based", "Full tuition waiver"],
                    ["HTRA (M.Tech, Ph.D.)", "GATE-qualified", "\u20b912,400 / \u20b937,000 per month"],
                ],
            }
        ],
    },
]

INFO_PAGES = [
    {
        "slug": "mission-and-vision",
        "title": "Mission and Vision",
        "body": [
            "Vision: To be a globally recognized institute that nurtures creative engineers, scientists, and entrepreneurs who address the technological needs of India and the world with rigor, integrity, and empathy.",
            "Mission: To impart world-class technical education and conduct frontier research in engineering, science, and technology while developing leadership, ethics, and social responsibility in our students.",
            "Core Values: Integrity, Curiosity, Inclusion, Excellence, and Sustainability.",
        ],
    },
    {
        "slug": "history",
        "title": "History of IIT Jammu",
        "body": [
            "The Indian Institute of Technology Jammu (IIT Jammu) was established in 2016 by an Act of the Parliament of India and declared an Institute of National Importance.",
            "Initial academic operations began at a temporary campus while the permanent campus was constructed at Jagti, Nagrota, in the union territory of Jammu and Kashmir. The institute relocated to its permanent campus in 2019.",
            "Today, IIT Jammu offers a portfolio of undergraduate, postgraduate, and doctoral programs across engineering, sciences, and humanities, supported by growing research centers in AI, sustainability, advanced materials, and 5G/6G communications.",
        ],
    },
    {
        "slug": "accreditation",
        "title": "Accreditation",
        "body": [
            "IIT Jammu is established by an Act of Parliament and recognized by the Government of India as an Institute of National Importance.",
            "Degrees are awarded by IIT Jammu directly, in accordance with the IIT Act. Several B.Tech programs are reviewed periodically under the National Board of Accreditation (NBA) framework.",
            "IIT Jammu participates in national rankings including NIRF and is committed to international quality benchmarks for engineering education.",
        ],
    },
    {
        "slug": "campus-life",
        "title": "Campus Life",
        "body": [
            "The IIT Jammu permanent campus at Jagti, Nagrota, spans more than 400 acres and is set in the foothills of the Shivalik range with views of the Trikuta hills.",
            "Students participate in 30+ clubs across robotics, music, drama, debate, photography, and entrepreneurship. Annual events include Tarang (cultural fest), Utkansh (technical fest), and the Tatva sports meet.",
            "On-campus residence halls, libraries, modern lab facilities, and sports complex support both academic work and student well-being.",
        ],
    },
    {
        "slug": "btech-programs",
        "title": "B.Tech Programs",
        "body": [
            "IIT Jammu offers four-year Bachelor of Technology (B.Tech) degrees in Computer Science & Engineering, Electrical Engineering, Electronics & Communication, Mechanical Engineering, Civil Engineering, Chemical Engineering, and Materials Science & Engineering.",
            "Each B.Tech program requires the completion of approximately 160 credits, including foundational, core, elective, capstone, and HSS courses, along with a minimum CGPA requirement of 5.0/10.",
            "Admission is through the Joint Entrance Examination (JEE) Advanced, with seats allotted by JoSAA based on All India Rank.",
        ],
    },
    {
        "slug": "mtech-programs",
        "title": "M.Tech Programs",
        "body": [
            "IIT Jammu offers two-year M.Tech programs in disciplines such as Communication Systems Engineering, Cybersecurity, AI & Machine Learning, Mechanical Systems, Structural Engineering, and Materials Engineering.",
            "Admissions are based on a valid GATE score followed by an interview / written test. Sponsored category admissions are also available for working professionals.",
            "Each M.Tech program requires about 64 credits including a year-long thesis under faculty supervision.",
        ],
    },
    {
        "slug": "msc-programs",
        "title": "M.Sc. Programs",
        "body": [
            "IIT Jammu offers two-year M.Sc. programs in Mathematics, Physics, and Chemistry. Admission is through the Joint Admission Test for Masters (JAM).",
            "The curriculum combines advanced coursework with a research project in the final year.",
        ],
    },
    {
        "slug": "phd-programs",
        "title": "Ph.D. Programs",
        "body": [
            "Doctoral students at IIT Jammu pursue independent research under faculty advisors across computing, electronics, materials, structures, sustainable engineering, sciences, and humanities.",
            "Ph.D. candidates complete coursework in their first year, qualifying examinations in their second year, and a defended dissertation typically by year 4 or 5.",
            "Multiple fellowships are available including HTRA, institute fellowships, and externally funded research positions.",
        ],
    },
    {
        "slug": "minor-programs",
        "title": "Minor / Honors Programs",
        "body": [
            "Minors enable students to develop expertise outside their primary major. A minor at IIT Jammu requires about 18\u201320 credits of courses in the chosen area.",
            "Available minors and honors tracks include Data Science & AI, Robotics, Entrepreneurship, Sustainability, Materials, and Mathematics.",
        ],
    },
    {
        "slug": "admission-policies",
        "title": "Admission Policies",
        "body": [
            "B.Tech admissions are through JEE (Advanced) followed by counseling by JoSAA.",
            "M.Tech admissions are through GATE and interview / written test; M.Sc. admissions are through JAM; Ph.D. admissions are through institute-level interviews based on academic record and research aptitude.",
            "Reservation policies follow Government of India norms for SC/ST/OBC-NCL/EWS/PwD categories.",
        ],
    },
    {
        "slug": "grading-system",
        "title": "Grading System",
        "body": [
            "IIT Jammu follows a 10-point grading scale (CGPA). Letter grades A+, A, B+, B, C+, C, D, F map to grade points 10, 9, 8, 7, 6, 5, 4, 0 respectively.",
            "A minimum CGPA of 5.0 is required to graduate. Students with a CGPA below 4.5 may be placed on academic probation.",
        ],
    },
    {
        "slug": "attendance",
        "title": "Attendance Requirements",
        "body": [
            "Students are expected to maintain a minimum of 75% attendance in every course they are registered for.",
            "Failure to meet this requirement may result in the student being barred from end-semester examinations, subject to review by the course instructor and DUGC.",
        ],
    },
    {
        "slug": "academic-integrity",
        "title": "Academic Integrity",
        "body": [
            "IIT Jammu upholds the highest standards of academic integrity. Plagiarism, unauthorized collaboration, fabrication of data, and other forms of academic dishonesty are strictly prohibited.",
            "Violations are reviewed by the Disciplinary Action Committee and may result in penalties ranging from a zero on the assignment to expulsion from the institute.",
        ],
    },
]
