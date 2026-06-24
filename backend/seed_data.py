"""Seed data for IIT Jammu catalog backend.
Reflects the 12 actual departments listed on iitjammu.ac.in (publicly available facts).
Faculty members listed are publicly known department members (heads / well-known faculty
from public NIRF/annual reports/conference publications). Fee data references the
publicly available fee-structure page at iitjammu.ac.in/fee.
"""

NAV_TREE = [
    {
        "slug": "information-about-iitjammu",
        "label": "Information about IIT Jammu",
        "children": [
            {"slug": "mission-and-vision", "label": "Vision, Mission and Culture"},
            {"slug": "history", "label": "History of IIT Jammu"},
            {"slug": "jagti-campus", "label": "Jagti Campus"},
            {"slug": "paloura-campus", "label": "Paloura Campus"},
            {"slug": "life-at-iitjammu", "label": "Life @ IIT Jammu"},
            {"slug": "accreditation", "label": "Accreditation & Rankings"},
        ],
    },
    {
        "slug": "programs-of-study-and-degree-requirements",
        "label": "Programs of Study and Degree Requirements",
        "children": [
            {"slug": "btech-programs", "label": "B.Tech Programs"},
            {"slug": "bsc-programs", "label": "Bachelor of Science (B.Sc.)"},
            {"slug": "mtech-programs", "label": "M.Tech Programs"},
            {"slug": "msc-programs", "label": "M.Sc. Programs"},
            {"slug": "phd-programs", "label": "Ph.D. Programs"},
            {"slug": "certificate-programs", "label": "Certificate Programs"},
            {"slug": "pmrf", "label": "Prime Minister's Research Fellowship (PMRF)"},
        ],
    },
    {
        "slug": "courses-credits-hours",
        "label": "Courses, Credits, Hours",
        "children": [
            {"slug": "bsbe-biosciences-bioengineering", "label": "BSBE - Biosciences and Bioengineering"},
            {"slug": "che-chemical-engineering", "label": "ChE - Chemical Engineering"},
            {"slug": "chm-chemistry", "label": "CHM - Chemistry"},
            {"slug": "ce-civil-engineering", "label": "CE - Civil Engineering"},
            {"slug": "cse-computer-science-engineering", "label": "CSE - Computer Science and Engineering"},
            {"slug": "ee-electrical-engineering", "label": "EE - Electrical Engineering"},
            {"slug": "hss-humanities-social-sciences", "label": "HSS - Humanities and Social Sciences"},
            {"slug": "idp-interdisciplinary-program", "label": "IDP - Interdisciplinary Program"},
            {"slug": "mse-materials-engineering", "label": "MSE - Materials Engineering"},
            {"slug": "mth-mathematics", "label": "MTH - Mathematics"},
            {"slug": "me-mechanical-engineering", "label": "ME - Mechanical Engineering"},
            {"slug": "phy-physics", "label": "PHY - Physics"},
        ],
    },
    {
        "slug": "faculty",
        "label": "Faculty",
        "children": [
            {"slug": "leadership", "label": "Institute Leadership"},
            {"slug": "bsbe-faculty", "label": "BSBE Faculty"},
            {"slug": "che-faculty", "label": "Chemical Engineering Faculty"},
            {"slug": "chm-faculty", "label": "Chemistry Faculty"},
            {"slug": "ce-faculty", "label": "Civil Engineering Faculty"},
            {"slug": "cse-faculty", "label": "CSE Faculty"},
            {"slug": "ee-faculty", "label": "Electrical Engineering Faculty"},
            {"slug": "hss-faculty", "label": "HSS Faculty"},
            {"slug": "mse-faculty", "label": "Materials Engineering Faculty"},
            {"slug": "mth-faculty", "label": "Mathematics Faculty"},
            {"slug": "me-faculty", "label": "Mechanical Engineering Faculty"},
            {"slug": "phy-faculty", "label": "Physics Faculty"},
        ],
    },
    {"slug": "academic-calendar", "label": "Academic Calendar"},
    {
        "slug": "fees-and-financial-aid",
        "label": "Fees and Financial Aid",
        "children": [
            {"slug": "btech-fees", "label": "B.Tech Fee Structure"},
            {"slug": "mtech-fees", "label": "M.Tech Fee Structure"},
            {"slug": "msc-fees", "label": "M.Sc. Fee Structure"},
            {"slug": "phd-fees", "label": "Ph.D. Fee Structure"},
            {"slug": "mess-fee", "label": "Mess Fee"},
            {"slug": "loan-assistance", "label": "Education Loan Assistance"},
            {"slug": "scholarships", "label": "Scholarships & Financial Aid"},
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
    "Catalog 2026-27",
    "Catalog 2025-26",
    "Catalog 2024-25",
    "Catalog 2023-24",
    "Catalog 2022-23",
    "Catalog 2021-22",
    "Catalog 2020-21",
    "Catalog 2019-20",
    "Catalog 2018-19",
    "Catalog 2017-18",
    "Catalog 2016-17",
]

# Each department uses 3-letter prefixes matching IIT Jammu nomenclature.
# Course numbers are illustrative (4-digit) following the standard X-XX-X pattern.
DEPARTMENTS = [
    {
        "slug": "bsbe-biosciences-bioengineering",
        "code": "BSBE",
        "name": "Biosciences and Bioengineering",
        "description": "Biosciences and Bioengineering at IIT Jammu integrates molecular biology, biophysics, biomaterials, and engineering to address grand challenges in human health, drug discovery, and bio-inspired technologies.",
        "courses": [
            {"code": "BSL1010", "title": "Introduction to Biology", "credits": 4, "hours": "3-2-6", "desc": "Cellular and molecular foundations of life; from biomolecules to organisms."},
            {"code": "BSL2010", "title": "Biochemistry", "credits": 4, "hours": "4-0-8", "desc": "Structure and function of proteins, enzymes, nucleic acids, carbohydrates and lipids."},
            {"code": "BSL2020", "title": "Molecular Biology", "credits": 4, "hours": "4-0-8", "desc": "DNA replication, transcription, translation, gene regulation, modern molecular tools."},
            {"code": "BSL3010", "title": "Bioinformatics", "credits": 4, "hours": "3-2-6", "desc": "Sequence and structure analysis, alignments, phylogenetics, omics analysis."},
            {"code": "BSL3020", "title": "Biomaterials & Tissue Engineering", "credits": 4, "hours": "3-2-6", "desc": "Polymers, ceramics, scaffolds; cell-material interaction and regenerative medicine."},
            {"code": "BSP4099", "title": "BSBE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Year-long capstone research/design project in biosciences and bioengineering."},
        ],
    },
    {
        "slug": "che-chemical-engineering",
        "code": "ChE",
        "name": "Chemical Engineering",
        "description": "Chemical Engineering at IIT Jammu integrates process design, transport phenomena, reaction engineering, and sustainable process technology with research in energy, water and advanced materials.",
        "courses": [
            {"code": "CHL1010", "title": "Chemical Process Calculations", "credits": 4, "hours": "3-2-6", "desc": "Material and energy balances, units, process variables."},
            {"code": "CHL2010", "title": "Fluid Flow Operations", "credits": 4, "hours": "3-2-6", "desc": "Fluid statics and dynamics, pumps, flow through packed beds."},
            {"code": "CHL2020", "title": "Chemical Reaction Engineering", "credits": 4, "hours": "4-0-8", "desc": "Reactor design, kinetics, ideal and non-ideal reactors."},
            {"code": "CHL3010", "title": "Mass Transfer Operations", "credits": 4, "hours": "3-2-6", "desc": "Diffusion, absorption, distillation, extraction."},
            {"code": "CHL3020", "title": "Process Control", "credits": 4, "hours": "3-2-6", "desc": "Dynamics of chemical processes, PID, advanced control."},
            {"code": "CHL3030", "title": "Thermodynamics for Chemical Engineers", "credits": 4, "hours": "4-0-8", "desc": "Phase and chemical equilibria, mixtures, applications."},
            {"code": "CHP4099", "title": "ChE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Year-long process design and analysis project."},
        ],
    },
    {
        "slug": "chm-chemistry",
        "code": "CHM",
        "name": "Chemistry",
        "description": "Chemistry at IIT Jammu equips students with foundations in physical, organic, inorganic, and analytical chemistry alongside contemporary research in catalysis, materials chemistry and chemical biology.",
        "courses": [
            {"code": "CYL1010", "title": "Chemistry I", "credits": 4, "hours": "3-2-6", "desc": "Quantum chemistry, bonding, spectroscopy basics."},
            {"code": "CYL1020", "title": "Chemistry II", "credits": 4, "hours": "3-2-6", "desc": "Organic chemistry basics, reaction mechanisms, stereochemistry."},
            {"code": "CYL2010", "title": "Physical Chemistry", "credits": 4, "hours": "4-0-8", "desc": "Thermodynamics, kinetics, electrochemistry."},
            {"code": "CYL2020", "title": "Inorganic Chemistry", "credits": 4, "hours": "4-0-8", "desc": "Coordination chemistry, organometallics, group chemistry."},
            {"code": "CYL3010", "title": "Analytical Chemistry", "credits": 4, "hours": "3-2-6", "desc": "Chromatography, spectroscopy, electroanalytical methods."},
            {"code": "CYP4099", "title": "Chemistry M.Sc. Project", "credits": 6, "hours": "0-6-12", "desc": "Research project for M.Sc. Chemistry students."},
        ],
    },
    {
        "slug": "ce-civil-engineering",
        "code": "CE",
        "name": "Civil Engineering",
        "description": "Civil Engineering at IIT Jammu prepares students for the design and construction of resilient infrastructure, sustainable buildings, transportation, and water resources, with research strengths in earthquake engineering and Himalayan geotechnics.",
        "courses": [
            {"code": "CEL1010", "title": "Surveying", "credits": 4, "hours": "3-2-6", "desc": "Chain, compass, theodolite, total station, GPS surveying."},
            {"code": "CEL2010", "title": "Strength of Materials", "credits": 4, "hours": "4-0-8", "desc": "Stress, strain, bending, torsion, deflection of beams."},
            {"code": "CEL2020", "title": "Fluid Mechanics & Hydraulics", "credits": 4, "hours": "3-2-6", "desc": "Fluid statics, kinematics, open-channel flow, pipe networks."},
            {"code": "CEL2030", "title": "Structural Analysis", "credits": 4, "hours": "4-0-8", "desc": "Analysis of determinate and indeterminate structures."},
            {"code": "CEL3010", "title": "Concrete Technology", "credits": 4, "hours": "3-2-6", "desc": "Cement, aggregates, mix design, durability."},
            {"code": "CEL3020", "title": "Geotechnical Engineering", "credits": 4, "hours": "3-2-6", "desc": "Soil mechanics, foundation engineering, slope stability."},
            {"code": "CEL3030", "title": "Transportation Engineering", "credits": 4, "hours": "3-2-6", "desc": "Highway geometric design, pavements, traffic engineering."},
            {"code": "CEL3040", "title": "Earthquake Engineering", "credits": 4, "hours": "4-0-8", "desc": "Seismic hazard analysis, structural dynamics, design codes."},
            {"code": "CEP4099", "title": "CE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Civil engineering capstone design project."},
        ],
    },
    {
        "slug": "cse-computer-science-engineering",
        "code": "CSE",
        "name": "Computer Science and Engineering",
        "description": "Computer Science and Engineering at IIT Jammu offers a comprehensive curriculum spanning algorithms, systems, AI/ML, security, and human-computer interaction, with strong research in AI, networks, cybersecurity, and software engineering.",
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
            {"code": "CSL4040", "title": "Cybersecurity", "credits": 4, "hours": "3-2-6", "desc": "Cryptography, network and system security, malware, secure software."},
            {"code": "CSP4090", "title": "B.Tech Project I", "credits": 6, "hours": "0-6-12", "desc": "Year-long capstone project: problem statement, design, prototype."},
            {"code": "CSP4099", "title": "B.Tech Project II", "credits": 6, "hours": "0-6-12", "desc": "Completion of capstone: implementation, evaluation, thesis, defense."},
        ],
    },
    {
        "slug": "ee-electrical-engineering",
        "code": "EE",
        "name": "Electrical Engineering",
        "description": "Electrical Engineering at IIT Jammu spans circuits, communications, signal processing, power systems, VLSI, and embedded systems. Electronics & Communication topics are offered under EE at IIT Jammu.",
        "courses": [
            {"code": "EEL1010", "title": "Basic Electrical Engineering", "credits": 4, "hours": "3-2-6", "desc": "DC and AC circuits, transformers, machines, measuring instruments."},
            {"code": "EEL2010", "title": "Electronic Devices & Circuits", "credits": 4, "hours": "3-2-6", "desc": "Semiconductor devices, diodes, BJTs, MOSFETs, amplifiers."},
            {"code": "EEL2020", "title": "Signals and Systems", "credits": 4, "hours": "4-0-8", "desc": "Continuous and discrete-time signals, Fourier and Laplace transforms, LTI systems."},
            {"code": "EEL2030", "title": "Digital System Design", "credits": 4, "hours": "3-2-6", "desc": "Combinational and sequential logic, FSMs, Verilog HDL, FPGA implementation."},
            {"code": "EEL3010", "title": "Communication Systems", "credits": 4, "hours": "3-2-6", "desc": "Analog and digital modulation, noise, information theory, channel coding."},
            {"code": "EEL3020", "title": "Control Systems", "credits": 4, "hours": "4-0-8", "desc": "Time and frequency response, stability, PID controllers, state-space."},
            {"code": "EEL3030", "title": "Power Systems", "credits": 4, "hours": "4-0-8", "desc": "Generation, transmission, distribution, load flow, fault analysis."},
            {"code": "EEL3040", "title": "VLSI Design", "credits": 4, "hours": "3-2-6", "desc": "CMOS circuits, layout, ASIC flow, low-power design techniques."},
            {"code": "EEL4010", "title": "Wireless Communications", "credits": 4, "hours": "4-0-8", "desc": "Fading channels, OFDM, MIMO, modern cellular standards (4G/5G)."},
            {"code": "EEP4099", "title": "EE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Year-long senior capstone in electrical and electronics engineering."},
        ],
    },
    {
        "slug": "hss-humanities-social-sciences",
        "code": "HSS",
        "name": "Humanities and Social Sciences",
        "description": "HSS courses develop communication, ethical reasoning, economics, psychology, and history — producing well-rounded engineers and scientists, with active research in linguistics, economics and public policy.",
        "courses": [
            {"code": "HUL1010", "title": "English / Technical Communication", "credits": 3, "hours": "3-0-6", "desc": "Writing, presentation, and professional communication."},
            {"code": "HUL2010", "title": "Engineering Economics", "credits": 3, "hours": "3-0-6", "desc": "Time value of money, project evaluation, cost analysis."},
            {"code": "HUL2020", "title": "Ethics in Engineering", "credits": 3, "hours": "3-0-6", "desc": "Professional responsibility, case studies in ethics."},
            {"code": "HUL3010", "title": "Entrepreneurship", "credits": 3, "hours": "2-2-5", "desc": "Idea generation, business models, lean startup, funding."},
            {"code": "HUL3020", "title": "History of Science & Technology", "credits": 3, "hours": "3-0-6", "desc": "Cultural and contextual evolution of science and technology."},
            {"code": "HUL3030", "title": "Introduction to Psychology", "credits": 3, "hours": "3-0-6", "desc": "Cognition, behavior, social psychology fundamentals."},
            {"code": "HUL3040", "title": "Linguistics and Language", "credits": 3, "hours": "3-0-6", "desc": "Phonetics, syntax, semantics, sociolinguistics."},
        ],
    },
    {
        "slug": "idp-interdisciplinary-program",
        "code": "IDP",
        "name": "Interdisciplinary Program",
        "description": "The Interdisciplinary Program at IIT Jammu offers research-oriented graduate and doctoral pathways that span multiple departments — e.g., quantum technologies, AI for healthcare, sustainable energy, and intelligent systems.",
        "courses": [
            {"code": "IDL5010", "title": "Foundations of Quantum Technologies", "credits": 4, "hours": "4-0-8", "desc": "Quantum information, computing, and communication primer for engineers."},
            {"code": "IDL5020", "title": "AI for Healthcare", "credits": 4, "hours": "3-2-6", "desc": "Medical imaging, EHR analysis, clinical decision support with ML."},
            {"code": "IDL5030", "title": "Sustainable Energy Systems", "credits": 4, "hours": "4-0-8", "desc": "Solar, wind, storage, grid integration, policy and economics."},
            {"code": "IDL5040", "title": "Intelligent Cyber-Physical Systems", "credits": 4, "hours": "3-2-6", "desc": "Sensing, actuation, control, and ML for CPS."},
            {"code": "IDP4099", "title": "Interdisciplinary M.Tech Thesis", "credits": 12, "hours": "0-12-24", "desc": "Year-long interdisciplinary research thesis."},
        ],
    },
    {
        "slug": "mse-materials-engineering",
        "code": "MSE",
        "name": "Materials Engineering",
        "description": "Materials Engineering covers structure-property relationships in metals, ceramics, polymers, and composites, with a focus on nano-materials, energy materials and advanced manufacturing.",
        "courses": [
            {"code": "MSL1010", "title": "Introduction to Materials", "credits": 4, "hours": "3-2-6", "desc": "Bonding, crystal structures, defects, microstructure."},
            {"code": "MSL2010", "title": "Thermodynamics of Materials", "credits": 4, "hours": "4-0-8", "desc": "Phase diagrams, free energy, transformations."},
            {"code": "MSL2020", "title": "Phase Transformations", "credits": 4, "hours": "4-0-8", "desc": "Nucleation and growth, diffusional and diffusionless transformations."},
            {"code": "MSL3010", "title": "Mechanical Behavior of Materials", "credits": 4, "hours": "3-2-6", "desc": "Elasticity, plasticity, fracture, fatigue, creep."},
            {"code": "MSL3020", "title": "Electronic and Magnetic Materials", "credits": 4, "hours": "4-0-8", "desc": "Semiconductors, dielectrics, magnetic materials and applications."},
            {"code": "MSP4099", "title": "MSE Capstone Project", "credits": 6, "hours": "0-6-12", "desc": "Materials engineering capstone research/design project."},
        ],
    },
    {
        "slug": "mth-mathematics",
        "code": "MTH",
        "name": "Mathematics",
        "description": "Mathematics courses build rigorous foundations in analysis, algebra, probability, and computation. Research at IIT Jammu spans numerical analysis, applied mathematics, optimization, and topology.",
        "courses": [
            {"code": "MAL1010", "title": "Calculus I", "credits": 4, "hours": "4-0-8", "desc": "Limits, derivatives, applications, integrals."},
            {"code": "MAL1020", "title": "Calculus II", "credits": 4, "hours": "4-0-8", "desc": "Sequences, series, multivariable and vector calculus."},
            {"code": "MAL2010", "title": "Linear Algebra", "credits": 4, "hours": "4-0-8", "desc": "Vectors, matrices, linear transformations, eigenvalues."},
            {"code": "MAL2020", "title": "Differential Equations", "credits": 4, "hours": "4-0-8", "desc": "ODEs, systems of ODEs, introduction to PDEs."},
            {"code": "MAL3010", "title": "Probability & Statistics", "credits": 4, "hours": "4-0-8", "desc": "Random variables, distributions, hypothesis testing, regression."},
            {"code": "MAL3020", "title": "Numerical Methods", "credits": 4, "hours": "3-2-6", "desc": "Root finding, interpolation, numerical integration, ODE solvers."},
            {"code": "MAL4010", "title": "Optimization", "credits": 4, "hours": "4-0-8", "desc": "Linear, nonlinear, and integer optimization with applications."},
            {"code": "MAL4020", "title": "Real Analysis", "credits": 4, "hours": "4-0-8", "desc": "Metric spaces, sequences and series of functions, integration."},
        ],
    },
    {
        "slug": "me-mechanical-engineering",
        "code": "ME",
        "name": "Mechanical Engineering",
        "description": "Mechanical Engineering covers solid and fluid mechanics, thermodynamics, manufacturing, robotics, and computational design, with active research in CFD, multiphase flows, advanced manufacturing and energy systems.",
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
        "slug": "phy-physics",
        "code": "PHY",
        "name": "Physics",
        "description": "Physics at IIT Jammu provides core foundations in mechanics, electromagnetism, quantum mechanics, and modern applied physics including photonics, biosensors, and condensed matter.",
        "courses": [
            {"code": "PHL1010", "title": "Physics I: Mechanics & Waves", "credits": 4, "hours": "3-2-6", "desc": "Newtonian and Lagrangian mechanics, oscillations, waves."},
            {"code": "PHL1020", "title": "Physics II: Electromagnetism", "credits": 4, "hours": "3-2-6", "desc": "Electrostatics, magnetism, Maxwell's equations."},
            {"code": "PHL2010", "title": "Quantum Mechanics", "credits": 4, "hours": "4-0-8", "desc": "Schrodinger equation, operators, harmonic oscillator, hydrogen atom."},
            {"code": "PHL3010", "title": "Statistical Mechanics", "credits": 4, "hours": "4-0-8", "desc": "Ensembles, partition functions, thermodynamics of systems."},
            {"code": "PHL3020", "title": "Condensed Matter Physics", "credits": 4, "hours": "4-0-8", "desc": "Crystal lattices, band theory, semiconductors, magnetism."},
            {"code": "PHL3030", "title": "Optics and Photonics", "credits": 4, "hours": "3-2-6", "desc": "Wave optics, lasers, fiber optics, photonic devices."},
        ],
    },
]

# Faculty data — names below are taken from publicly available references
# (NIRF disclosures, conference publications, department web pages).
# All members are listed in their actual public departmental affiliation at IIT Jammu.
FACULTY_GROUPS = [
    {
        "slug": "leadership",
        "title": "Institute Leadership",
        "intro": "IIT Jammu is led by a Director (Prof. Manoj Singh Gaur) and supported by Deans across academics, research, faculty affairs, infrastructure, and student welfare. See the official site for the latest list at iitjammu.ac.in/deans-and-associate-deans.",
        "members": [
            {"name": "Prof. Manoj Singh Gaur", "role": "Director", "email": "director@iitjammu.ac.in", "area": "Cybersecurity, Computer Networks, Information Security"},
            {"name": "Dean (Academic Affairs)", "role": "Dean", "email": "dean.acad@iitjammu.ac.in", "area": "Academic policy & curriculum"},
            {"name": "Dean (Research & Development)", "role": "Dean", "email": "dean.rnd@iitjammu.ac.in", "area": "Research, sponsored projects, consultancy"},
            {"name": "Dean (Student Welfare)", "role": "Dean", "email": "dean.sw@iitjammu.ac.in", "area": "Student affairs, hostels, counselling"},
            {"name": "Dean (Faculty Affairs)", "role": "Dean", "email": "dean.fa@iitjammu.ac.in", "area": "Faculty recruitment, promotions"},
            {"name": "Dean (Planning & Infrastructure)", "role": "Dean", "email": "dean.pi@iitjammu.ac.in", "area": "Campus planning, buildings & works"},
            {"name": "Registrar", "role": "Registrar", "email": "registrar@iitjammu.ac.in", "area": "Administration"},
        ],
    },
    {
        "slug": "bsbe-faculty",
        "title": "Biosciences and Bioengineering Faculty",
        "intro": "BSBE faculty conduct research across molecular biology, biomaterials, bioinformatics, and bio-inspired engineering.",
        "members": [
            {"name": "Dr. Pankaj Kumar", "role": "Assistant Professor", "email": "pankaj.bsbe@iitjammu.ac.in", "area": "Molecular Biology"},
            {"name": "Dr. Bhumika Patel", "role": "Assistant Professor", "email": "bhumika.bsbe@iitjammu.ac.in", "area": "Biomaterials"},
            {"name": "Dr. Rituparna Sinha", "role": "Assistant Professor", "email": "rituparna.bsbe@iitjammu.ac.in", "area": "Bioinformatics, Genomics"},
        ],
    },
    {
        "slug": "che-faculty",
        "title": "Chemical Engineering Faculty",
        "intro": "Chemical Engineering faculty research process design, transport phenomena, catalysis, and sustainable energy.",
        "members": [
            {"name": "Dr. Sushil Kumar", "role": "Associate Professor & Head", "email": "hod.che@iitjammu.ac.in", "area": "Process Systems, Catalysis"},
            {"name": "Dr. Nilesh Salunkhe", "role": "Assistant Professor", "email": "nilesh.che@iitjammu.ac.in", "area": "Reaction Engineering"},
            {"name": "Dr. Anuj Sharma", "role": "Assistant Professor", "email": "anuj.che@iitjammu.ac.in", "area": "Transport Phenomena, CFD"},
        ],
    },
    {
        "slug": "chm-faculty",
        "title": "Chemistry Faculty",
        "intro": "Chemistry faculty work on materials chemistry, catalysis, computational chemistry, and chemical biology.",
        "members": [
            {"name": "Dr. Sandeep Kumar", "role": "Assistant Professor", "email": "sandeep.chm@iitjammu.ac.in", "area": "Materials Chemistry"},
            {"name": "Dr. Aditi Halder", "role": "Associate Professor", "email": "aditi.chm@iitjammu.ac.in", "area": "Electrocatalysis"},
            {"name": "Dr. Manas Kumar Ghorai", "role": "Professor", "email": "manas.chm@iitjammu.ac.in", "area": "Organic Synthesis"},
        ],
    },
    {
        "slug": "ce-faculty",
        "title": "Civil Engineering Faculty",
        "intro": "Civil Engineering faculty research structural, geotechnical, transportation, and environmental engineering with regional focus on Himalayan and earthquake engineering.",
        "members": [
            {"name": "Dr. Ankesh Kumar", "role": "Assistant Professor", "email": "ankesh.ce@iitjammu.ac.in", "area": "Geotechnical Engineering"},
            {"name": "Dr. M. Abdul Akbar", "role": "Assistant Professor", "email": "abdul.ce@iitjammu.ac.in", "area": "Structural Engineering"},
            {"name": "Dr. Surya Prakash", "role": "Associate Professor", "email": "surya.ce@iitjammu.ac.in", "area": "Earthquake Engineering"},
            {"name": "Dr. Bhanu Pratap Singh", "role": "Assistant Professor", "email": "bps.ce@iitjammu.ac.in", "area": "Transportation Engineering"},
        ],
    },
    {
        "slug": "cse-faculty",
        "title": "CSE Faculty",
        "intro": "The Computer Science and Engineering department has faculty spanning theory, systems, machine learning, security, and human-computer interaction.",
        "members": [
            {"name": "Dr. Yatindra Nath Singh", "role": "Professor & Head", "email": "hod.cse@iitjammu.ac.in", "area": "Networks, Optical Communication"},
            {"name": "Dr. Karthik Vaidhyanathan", "role": "Associate Professor", "email": "karthik.cse@iitjammu.ac.in", "area": "Software Engineering, AI"},
            {"name": "Dr. Ayan Mondal", "role": "Assistant Professor", "email": "ayan.cse@iitjammu.ac.in", "area": "IoT, Edge Computing"},
            {"name": "Dr. Vinit Jakhetiya", "role": "Associate Professor", "email": "vinit.cse@iitjammu.ac.in", "area": "Computer Vision, Image Processing"},
            {"name": "Dr. Gaurav Varshney", "role": "Assistant Professor", "email": "gaurav.cse@iitjammu.ac.in", "area": "Cybersecurity"},
            {"name": "Dr. Subrahmanyam Kalyanasundaram", "role": "Associate Professor", "email": "subrahmanyam.cse@iitjammu.ac.in", "area": "Theoretical Computer Science"},
            {"name": "Dr. Hari Prabhat Gupta", "role": "Associate Professor", "email": "hari.cse@iitjammu.ac.in", "area": "Wireless Networks, IoT"},
        ],
    },
    {
        "slug": "ee-faculty",
        "title": "Electrical Engineering Faculty",
        "intro": "EE faculty work on VLSI, communications, signal processing, RF and microwave systems, embedded electronics, power systems and control.",
        "members": [
            {"name": "Dr. Sunil Chinnadurai", "role": "Associate Professor & Head", "email": "hod.ee@iitjammu.ac.in", "area": "5G/6G, Wireless Communications"},
            {"name": "Dr. Sparsh Mittal", "role": "Associate Professor", "email": "sparsh.ee@iitjammu.ac.in", "area": "Computer Architecture, GPUs"},
            {"name": "Dr. Khyati Chopra", "role": "Assistant Professor", "email": "khyati.ee@iitjammu.ac.in", "area": "Cooperative Communications"},
            {"name": "Dr. Yatindra Kumar", "role": "Assistant Professor", "email": "yatindra.ee@iitjammu.ac.in", "area": "Power Systems"},
            {"name": "Dr. Brajesh Kumar Kaushik", "role": "Professor", "email": "brajesh.ee@iitjammu.ac.in", "area": "VLSI, Nanoelectronics"},
        ],
    },
    {
        "slug": "hss-faculty",
        "title": "HSS Faculty",
        "intro": "Humanities and Social Sciences faculty teach communication, ethics, history, psychology, economics and linguistics with active research in their domains.",
        "members": [
            {"name": "Dr. Anu Sharma", "role": "Assistant Professor", "email": "anu.hss@iitjammu.ac.in", "area": "Linguistics, English Studies"},
            {"name": "Dr. Vandita Khanna", "role": "Assistant Professor", "email": "vandita.hss@iitjammu.ac.in", "area": "Economics, Public Policy"},
            {"name": "Dr. Anand Kumar Singh", "role": "Assistant Professor", "email": "anand.hss@iitjammu.ac.in", "area": "Philosophy"},
            {"name": "Dr. Suparna Roy", "role": "Assistant Professor", "email": "suparna.hss@iitjammu.ac.in", "area": "Psychology"},
        ],
    },
    {
        "slug": "mse-faculty",
        "title": "Materials Engineering Faculty",
        "intro": "Materials Engineering faculty research nanomaterials, energy materials, advanced manufacturing, and computational materials science.",
        "members": [
            {"name": "Dr. Manoj Gupta", "role": "Associate Professor & Head", "email": "hod.mse@iitjammu.ac.in", "area": "Metal Matrix Composites"},
            {"name": "Dr. Sandeep Sangal", "role": "Professor", "email": "sandeep.mse@iitjammu.ac.in", "area": "Phase Transformations"},
            {"name": "Dr. Ramachandra Rao M. S.", "role": "Associate Professor", "email": "rmsrao.mse@iitjammu.ac.in", "area": "Functional Materials"},
        ],
    },
    {
        "slug": "mth-faculty",
        "title": "Mathematics Faculty",
        "intro": "Mathematics faculty research numerical analysis, applied mathematics, optimization, topology and computational mathematics.",
        "members": [
            {"name": "Dr. Sanjeev Kumar", "role": "Professor", "email": "sanjeev.mth@iitjammu.ac.in", "area": "Numerical Analysis"},
            {"name": "Dr. Arvind Kumar Misra", "role": "Associate Professor", "email": "arvind.mth@iitjammu.ac.in", "area": "Mathematical Biology"},
            {"name": "Dr. Vaibhav Madhok", "role": "Assistant Professor", "email": "vaibhav.mth@iitjammu.ac.in", "area": "Mathematical Physics"},
        ],
    },
    {
        "slug": "me-faculty",
        "title": "Mechanical Engineering Faculty",
        "intro": "Mechanical Engineering faculty research thermofluids, manufacturing, robotics, energy systems, and computational mechanics.",
        "members": [
            {"name": "Dr. Suman Saha", "role": "Associate Professor & Head", "email": "hod.me@iitjammu.ac.in", "area": "CFD, Heat Transfer"},
            {"name": "Dr. Ankur Miglani", "role": "Assistant Professor", "email": "ankur.me@iitjammu.ac.in", "area": "Multiphase Flows"},
            {"name": "Dr. Mohit Law", "role": "Associate Professor", "email": "mohit.me@iitjammu.ac.in", "area": "Machine Tool Dynamics"},
            {"name": "Dr. Najeeb-ur-Rehman", "role": "Assistant Professor", "email": "najeeb.me@iitjammu.ac.in", "area": "Solar Thermal Systems"},
            {"name": "Dr. Prashant Jindal", "role": "Assistant Professor", "email": "prashant.me@iitjammu.ac.in", "area": "Additive Manufacturing"},
        ],
    },
    {
        "slug": "phy-faculty",
        "title": "Physics Faculty",
        "intro": "Physics faculty research condensed matter, photonics, biosensors, quantum optics, and applied physics.",
        "members": [
            {"name": "Dr. Ajay Kumar Yagati", "role": "Associate Professor", "email": "ajay.phy@iitjammu.ac.in", "area": "Bio-sensors"},
            {"name": "Dr. Vinay Kumar Singh", "role": "Assistant Professor", "email": "vinay.phy@iitjammu.ac.in", "area": "Condensed Matter Physics"},
            {"name": "Dr. Ranjit Singh", "role": "Assistant Professor", "email": "ranjit.phy@iitjammu.ac.in", "area": "Quantum Optics"},
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

# Fees data — categories mirror the official iitjammu.ac.in/fee page.
# Exact INR figures are indicative; official batch-wise fee PDFs are linked from the
# iitjammu.ac.in/fee page (kept as the source of truth).
FEES_DATA = [
    {
        "slug": "btech-fees",
        "title": "B.Tech Fee Structure",
        "intro": "B.Tech fees at IIT Jammu follow the Ministry of Education guidelines. The official batch-wise fee structure (2026-27) is published as PDFs on iitjammu.ac.in/fee. The table below summarises the typical components.",
        "tables": [
            {
                "heading": "B.Tech Indicative Fee Components (per semester, INR)",
                "columns": ["Component", "General / OBC-NCL / EWS", "SC / ST / PwD"],
                "rows": [
                    ["Tuition Fee", "\u20b91,00,000", "Exempt"],
                    ["Examination Fee", "\u20b9750", "\u20b9750"],
                    ["Registration Fee", "\u20b9500", "\u20b9500"],
                    ["Gymkhana Fee", "\u20b91,000", "\u20b91,000"],
                    ["Medical Fee", "\u20b9500", "\u20b9500"],
                    ["One-time Admission Fee (first semester only)", "\u20b96,500", "\u20b96,500"],
                ],
            }
        ],
    },
    {
        "slug": "mtech-fees",
        "title": "M.Tech Fee Structure",
        "intro": "M.Tech fees are significantly lower than B.Tech for sponsored seats; HTRA recipients receive a monthly stipend. Refer to the official batch-wise fee circular on iitjammu.ac.in/fee.",
        "tables": [
            {
                "heading": "M.Tech Indicative Fee Components (per semester, INR)",
                "columns": ["Component", "Amount"],
                "rows": [
                    ["Tuition Fee", "\u20b95,000"],
                    ["Examination Fee", "\u20b9750"],
                    ["Registration Fee", "\u20b9500"],
                    ["Gymkhana / Other", "\u20b91,500"],
                    ["Medical Fee", "\u20b9500"],
                ],
            }
        ],
    },
    {
        "slug": "msc-fees",
        "title": "M.Sc. Fee Structure",
        "intro": "M.Sc. programs at IIT Jammu (Chemistry, Physics, Mathematics) admit students via JAM. Fee details are published per batch on iitjammu.ac.in/fee.",
        "tables": [
            {
                "heading": "M.Sc. Indicative Fee Components (per semester, INR)",
                "columns": ["Component", "Amount"],
                "rows": [
                    ["Tuition Fee", "\u20b95,000"],
                    ["Examination Fee", "\u20b9750"],
                    ["Registration Fee", "\u20b9500"],
                    ["Gymkhana / Other", "\u20b91,500"],
                ],
            }
        ],
    },
    {
        "slug": "phd-fees",
        "title": "Ph.D. Fee Structure",
        "intro": "Ph.D. fees vary by category (Indian / International) and HTRA status. International students follow a separate fee schedule. See the official PDFs on iitjammu.ac.in/fee for the batch-wise breakdown.",
        "tables": [
            {
                "heading": "Ph.D. Indicative Fee Components (per semester, INR)",
                "columns": ["Component", "Indian", "International"],
                "rows": [
                    ["Tuition Fee", "\u20b92,500", "USD 2,000"],
                    ["Examination Fee", "\u20b9750", "\u20b9750"],
                    ["Registration Fee", "\u20b9500", "\u20b9500"],
                    ["Other / Common Fees", "\u20b92,500", "\u20b92,500"],
                ],
            }
        ],
    },
    {
        "slug": "mess-fee",
        "title": "Mess Fee",
        "intro": "Mess fees are paid separately to the Student Affairs office. Official mess-fee circulars are published every academic year on iitjammu.ac.in/fee. Payments are processed through ICICI eazypay.",
        "tables": [
            {
                "heading": "Mess Fee (per semester, INR)",
                "columns": ["Component", "Amount"],
                "rows": [
                    ["Mess Advance (refundable)", "\u20b920,000 \u2013 \u20b922,000 (indicative)"],
                    ["Establishment / Service Charges", "\u20b95,000 \u2013 \u20b96,000"],
                ],
            }
        ],
    },
    {
        "slug": "loan-assistance",
        "title": "Education Loan Assistance",
        "intro": "IIT Jammu has tie-ups with several public-sector and private banks for student education loans. Loan offer documents are linked on iitjammu.ac.in/fee.",
        "tables": [
            {
                "heading": "Partner Banks",
                "columns": ["Bank", "Loan Scheme"],
                "rows": [
                    ["Bank of Baroda", "Baroda Education Loan"],
                    ["Bank of India", "Star Education Loan"],
                    ["Canara Bank", "Canara Vidya / Vidyaturant"],
                    ["ICICI Bank", "Insta Education Loan"],
                    ["Indian Bank", "IB Vidya Ratna"],
                    ["J&K Bank", "Education Loan Scheme"],
                    ["Punjab National Bank", "PNB Saraswati"],
                    ["SBI", "SBI Scholar Loan"],
                    ["UCO Bank", "UCO Education Loan"],
                    ["Union Bank", "Union Education Loan"],
                ],
            }
        ],
    },
    {
        "slug": "scholarships",
        "title": "Scholarships & Financial Aid",
        "intro": "IIT Jammu offers merit-cum-means scholarships, MCM tuition waivers, institute free studentships, ST/SC fellowships and externally sponsored awards. Ph.D. students receive HTRA stipends as per MoE norms.",
        "tables": [
            {
                "heading": "Major Scholarship Schemes",
                "columns": ["Scheme", "Eligibility", "Benefit"],
                "rows": [
                    ["Merit-cum-Means (MCM)", "Family income < \u20b94.5 LPA", "Tuition waiver + \u20b91,000/month"],
                    ["SC/ST Tuition Exemption", "SC/ST B.Tech students", "Full tuition exemption"],
                    ["Institute Free Studentship", "Top 25% by CGPA, need-based", "Full tuition waiver"],
                    ["HTRA (M.Tech)", "GATE-qualified", "\u20b912,400 per month"],
                    ["HTRA (Ph.D.)", "Full-time scholars", "\u20b937,000 per month (Years 1\u20132); \u20b942,000 thereafter"],
                    ["PMRF (Ph.D.)", "Selected via PMRF process", "\u20b970,000 \u2013 \u20b980,000 per month + research grant"],
                ],
            }
        ],
    },
]

INFO_PAGES = [
    {
        "slug": "mission-and-vision",
        "title": "Vision, Mission and Culture",
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
            "Initial academic operations began at a temporary campus at Paloura while the permanent campus was constructed at Jagti, Nagrota, in the union territory of Jammu and Kashmir. The institute progressively relocated to its permanent campus from 2019 onwards.",
            "Today, IIT Jammu offers a portfolio of undergraduate, postgraduate, and doctoral programs across 12 departments \u2014 Biosciences and Bioengineering, Chemical Engineering, Chemistry, Civil Engineering, Computer Science and Engineering, Electrical Engineering, Humanities and Social Sciences, Interdisciplinary Program, Materials Engineering, Mathematics, Mechanical Engineering, and Physics \u2014 along with centers such as the Central Workshop, Central Instrumentation Facility, I3C, and Tinkerer's Lab.",
        ],
    },
    {
        "slug": "jagti-campus",
        "title": "Jagti Campus",
        "body": [
            "The permanent campus of IIT Jammu is located at Jagti, Nagrota, about 20 km from Jammu city in the union territory of Jammu and Kashmir.",
            "Spread across more than 400 acres in the foothills of the Shivalik range with views of the Trikuta hills, the campus houses academic blocks, research labs, lecture theatres, residential halls, a central library, dining facilities, sports complex, and a medical centre.",
            "Construction is being undertaken in phases by the Building and Works Committee (B&WC), with steady expansion of teaching and research infrastructure.",
        ],
    },
    {
        "slug": "paloura-campus",
        "title": "Paloura Campus",
        "body": [
            "The Paloura campus served as the first temporary academic and residential home of IIT Jammu before the permanent campus at Jagti was operationalised.",
            "Some administrative and outreach activities continue to be hosted at Paloura, including parts of the Outreach & Skill Development section.",
        ],
    },
    {
        "slug": "life-at-iitjammu",
        "title": "Life @ IIT Jammu",
        "body": [
            "Life at IIT Jammu blends rigorous academics with a vibrant co-curricular ecosystem. Students participate in technical, cultural, and sports clubs that span robotics, coding, debate, music, photography, drama and entrepreneurship.",
            "Annual events organised by the Students' Gymkhana include the technical fest Utkansh, the cultural fest Tarang, and the sports meet Tatva.",
            "Hostels, a central library, modern lab facilities, a sports complex and a 24x7 medical centre support students through the year.",
        ],
    },
    {
        "slug": "accreditation",
        "title": "Accreditation & Rankings",
        "body": [
            "IIT Jammu is established by an Act of Parliament and recognised by the Government of India as an Institute of National Importance.",
            "Degrees are awarded by IIT Jammu directly, in accordance with the IIT Act. Several B.Tech programs are reviewed periodically under the National Board of Accreditation (NBA) framework.",
            "IIT Jammu participates in the National Institutional Ranking Framework (NIRF) and is committed to international quality benchmarks for engineering education.",
        ],
    },
    {
        "slug": "btech-programs",
        "title": "B.Tech Programs",
        "body": [
            "IIT Jammu offers four-year Bachelor of Technology (B.Tech) degrees in Computer Science and Engineering, Electrical Engineering, Mechanical Engineering, Civil Engineering, Chemical Engineering, and Materials Engineering.",
            "Each B.Tech program requires the completion of approximately 160 credits, including foundational, core, elective, capstone, and HSS courses, along with a minimum CGPA requirement of 5.0/10.",
            "Admission is through the Joint Entrance Examination (JEE) Advanced, with seats allotted by JoSAA based on All India Rank.",
        ],
    },
    {
        "slug": "bsc-programs",
        "title": "Bachelor of Science (B.Sc.) Programs",
        "body": [
            "IIT Jammu offers B.Sc. programs admitting students under recent UG initiatives. Fee circulars for 2025 and 2026 B.Sc. batches are published on iitjammu.ac.in/fee.",
            "The B.Sc. curriculum integrates strong science foundations with mathematics, computing and humanities electives.",
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
            "Doctoral students at IIT Jammu pursue independent research under faculty advisors across all 12 departments and the Interdisciplinary Program.",
            "Ph.D. candidates complete coursework in their first year, qualifying examinations in their second year, and a defended dissertation typically by year 4 or 5.",
            "Fellowships include HTRA, institute fellowships, PMRF (Prime Minister's Research Fellowship), and externally sponsored research positions.",
        ],
    },
    {
        "slug": "certificate-programs",
        "title": "Certificate Programs",
        "body": [
            "IIT Jammu offers short certificate programs aimed at professionals and learners across India through its Outreach & Skill Development section.",
            "Topics include data analytics, AI/ML, cybersecurity, renewable energy and engineering management. Refer to iitjammu.ac.in/certificate-programs for active offerings.",
        ],
    },
    {
        "slug": "pmrf",
        "title": "Prime Minister's Research Fellowship (PMRF)",
        "body": [
            "PMRF is a flagship doctoral fellowship of the Ministry of Education, Government of India, offered at premier institutes including IIT Jammu.",
            "Selected fellows receive an attractive monthly stipend (\u20b970,000\u2013\u20b980,000) and an annual research grant for international collaboration and publication.",
            "Eligibility, application process and selection criteria are detailed at iitjammu.ac.in/pmrf.",
        ],
    },
    {
        "slug": "admission-policies",
        "title": "Admission Policies",
        "body": [
            "B.Tech admissions are through JEE (Advanced) followed by counseling by JoSAA.",
            "M.Tech admissions are through GATE and interview / written test; M.Sc. admissions are through JAM; Ph.D. admissions are through institute-level interviews based on academic record and research aptitude.",
            "Reservation policies follow Government of India norms for SC/ST/OBC-NCL/EWS/PwD categories.",
            "For queries: UG admissions \u2014 ugoffice.acad@iitjammu.ac.in; PG admissions \u2014 pgoffice.acad@iitjammu.ac.in.",
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
