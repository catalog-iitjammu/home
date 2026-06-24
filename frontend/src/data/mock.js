// Mock data for GCET College of Engineering catalog

export const CATALOG_VERSIONS = [
  'Catalog 2025-26',
  'Student Handbook 2025-26',
  'Catalog 2024-25',
  'Student Handbook 2024-25',
  'Catalog 2023-24',
  'Student Handbook 2023-24',
  'Catalog 2022-23',
  'Student Handbook 2022-23',
  'Catalog 2021-22',
  'Student Handbook 2021-22',
  'Catalog 2020-21',
  'Catalog 2019-20',
  'Catalog 2018-19',
  'Catalog 2017-18',
  'Catalog 2016-17',
  'Catalog 2015-16',
];

export const NAV_TREE = [
  {
    slug: 'information-about-gcet',
    label: 'Information about GCET',
    children: [
      { slug: 'mission-and-vision', label: 'Mission and Vision' },
      { slug: 'history', label: 'History of GCET' },
      { slug: 'accreditation', label: 'Accreditation' },
      { slug: 'campus-life', label: 'Campus Life' },
    ],
  },
  {
    slug: 'programs-of-study-and-degree-requirements',
    label: 'Programs of Study and Degree Requirements',
    children: [
      { slug: 'btech-programs', label: 'B.Tech Programs' },
      { slug: 'mtech-programs', label: 'M.Tech Programs' },
      { slug: 'phd-programs', label: 'Ph.D. Programs' },
      { slug: 'minor-programs', label: 'Minor Programs' },
    ],
  },
  {
    slug: 'courses-credits-hours',
    label: 'Courses, Credits, Hours',
    children: [
      { slug: 'cse-computer-science-engineering', label: 'CSE - Computer Science & Engineering' },
      { slug: 'it-information-technology', label: 'IT - Information Technology' },
      { slug: 'ece-electronics-communication', label: 'ECE - Electronics & Communication' },
      { slug: 'me-mechanical-engineering', label: 'ME - Mechanical Engineering' },
      { slug: 'ce-civil-engineering', label: 'CE - Civil Engineering' },
      { slug: 'ee-electrical-engineering', label: 'EE - Electrical Engineering' },
      { slug: 'mth-mathematics', label: 'MTH - Mathematics' },
      { slug: 'hss-humanities-social-sciences', label: 'HSS - Humanities & Social Sciences' },
      { slug: 'co-curriculars', label: 'Co-curriculars' },
    ],
  },
  {
    slug: 'academic-policies-and-procedures',
    label: 'Academic Policies and Procedures',
    children: [
      { slug: 'admission-policies', label: 'Admission Policies' },
      { slug: 'grading-system', label: 'Grading System' },
      { slug: 'attendance', label: 'Attendance Requirements' },
      { slug: 'academic-integrity', label: 'Academic Integrity' },
    ],
  },
  { slug: 'table-of-contents', label: 'Table of Contents' },
];

export const DEPARTMENTS = {
  'cse-computer-science-engineering': {
    code: 'CSE',
    name: 'Computer Science & Engineering',
    description:
      'The Department of Computer Science and Engineering at GCET offers a comprehensive curriculum that blends theoretical foundations with practical applications, preparing students for careers in software development, AI/ML, data science, and research.',
    courses: [
      { code: 'CSE1101', title: 'Introduction to Programming', credits: 4, hours: '3-2-6', desc: 'Fundamentals of programming using Python, including data types, control structures, functions, and basic algorithms.' },
      { code: 'CSE1202', title: 'Data Structures', credits: 4, hours: '3-2-6', desc: 'Linear and non-linear data structures: arrays, linked lists, stacks, queues, trees, and graphs with applications.' },
      { code: 'CSE2103', title: 'Object Oriented Programming', credits: 4, hours: '3-2-6', desc: 'Object-oriented design and programming using Java/C++, encapsulation, inheritance, polymorphism.' },
      { code: 'CSE2204', title: 'Database Management Systems', credits: 4, hours: '3-2-6', desc: 'Relational model, SQL, normalization, transactions, indexing, and query optimization.' },
      { code: 'CSE2305', title: 'Operating Systems', credits: 4, hours: '3-2-6', desc: 'Process management, threads, scheduling, memory management, file systems, and concurrency.' },
      { code: 'CSE3101', title: 'Algorithms Design & Analysis', credits: 4, hours: '4-0-8', desc: 'Greedy, divide-and-conquer, dynamic programming, graph algorithms, and NP-completeness.' },
      { code: 'CSE3202', title: 'Computer Networks', credits: 4, hours: '3-2-6', desc: 'Layered architectures, TCP/IP, routing, congestion control, application protocols.' },
      { code: 'CSE3303', title: 'Machine Learning', credits: 4, hours: '3-2-6', desc: 'Supervised and unsupervised learning, neural networks, regression, classification, clustering.' },
      { code: 'CSE4101', title: 'Capstone Project I', credits: 6, hours: '0-6-12', desc: 'Year-long industry-sponsored capstone project: requirements, design, and prototype.' },
      { code: 'CSE4202', title: 'Capstone Project II', credits: 6, hours: '0-6-12', desc: 'Completion of capstone: implementation, validation, deployment, and presentation.' },
    ],
  },
  'it-information-technology': {
    code: 'IT',
    name: 'Information Technology',
    description:
      'The Information Technology program focuses on the design, development, and management of information systems, cloud infrastructure, web technologies, and cybersecurity.',
    courses: [
      { code: 'IT1101', title: 'IT Fundamentals', credits: 3, hours: '3-0-6', desc: 'Overview of computing, networks, hardware, and information systems.' },
      { code: 'IT2202', title: 'Web Technologies', credits: 4, hours: '3-2-6', desc: 'HTML, CSS, JavaScript, React, Node.js, full-stack web development principles.' },
      { code: 'IT2303', title: 'Cloud Computing', credits: 4, hours: '3-2-6', desc: 'IaaS, PaaS, SaaS, AWS/Azure/GCP fundamentals, containers, and orchestration.' },
      { code: 'IT3101', title: 'Cybersecurity', credits: 4, hours: '3-2-6', desc: 'Cryptography, network security, threat modeling, penetration testing fundamentals.' },
      { code: 'IT3202', title: 'Mobile App Development', credits: 4, hours: '3-2-6', desc: 'Cross-platform mobile development using React Native and Flutter.' },
      { code: 'IT4101', title: 'IT Capstone', credits: 6, hours: '0-6-12', desc: 'Industry-driven IT capstone project across the senior year.' },
    ],
  },
  'ece-electronics-communication': {
    code: 'ECE',
    name: 'Electronics & Communication Engineering',
    description:
      'Electronics & Communication Engineering at GCET emphasizes design of analog and digital systems, signal processing, embedded systems, VLSI, and modern communication networks.',
    courses: [
      { code: 'ECE1101', title: 'Basic Electronics', credits: 4, hours: '3-2-6', desc: 'Semiconductor devices, diodes, BJTs, MOSFETs, amplifiers, oscillators.' },
      { code: 'ECE2202', title: 'Digital System Design', credits: 4, hours: '3-2-6', desc: 'Combinational and sequential logic, FSMs, Verilog HDL, FPGA implementation.' },
      { code: 'ECE2303', title: 'Signals and Systems', credits: 4, hours: '4-0-8', desc: 'Continuous and discrete signals, Fourier and Laplace transforms, LTI systems.' },
      { code: 'ECE3101', title: 'Communication Systems', credits: 4, hours: '3-2-6', desc: 'Analog and digital modulation, noise, information theory, channel coding.' },
      { code: 'ECE3202', title: 'Embedded Systems', credits: 4, hours: '3-2-6', desc: 'Microcontrollers, ARM Cortex, real-time systems, hardware-software co-design.' },
      { code: 'ECE3303', title: 'VLSI Design', credits: 4, hours: '3-2-6', desc: 'CMOS circuit design, layout, ASIC flow, low-power design techniques.' },
      { code: 'ECE4101', title: 'ECE Capstone', credits: 6, hours: '0-6-12', desc: 'Senior capstone in electronics/communication systems.' },
    ],
  },
  'me-mechanical-engineering': {
    code: 'ME',
    name: 'Mechanical Engineering',
    description:
      'Mechanical Engineering at GCET covers mechanics, thermodynamics, manufacturing, robotics, and modern design tools.',
    courses: [
      { code: 'ME1101', title: 'Engineering Mechanics', credits: 4, hours: '4-0-8', desc: 'Statics and dynamics of particles and rigid bodies.' },
      { code: 'ME1202', title: 'Engineering Graphics', credits: 3, hours: '1-4-4', desc: 'Orthographic projections, CAD modeling using SolidWorks.' },
      { code: 'ME2103', title: 'Thermodynamics', credits: 4, hours: '4-0-8', desc: 'Laws of thermodynamics, cycles, properties of pure substances.' },
      { code: 'ME2204', title: 'Fluid Mechanics', credits: 4, hours: '3-2-6', desc: 'Fluid statics, kinematics, dynamics, dimensional analysis.' },
      { code: 'ME3101', title: 'Machine Design', credits: 4, hours: '3-2-6', desc: 'Stress analysis, design of shafts, gears, bearings.' },
      { code: 'ME3202', title: 'Manufacturing Processes', credits: 4, hours: '3-2-6', desc: 'Casting, forming, machining, joining, additive manufacturing.' },
      { code: 'ME4101', title: 'ME Capstone', credits: 6, hours: '0-6-12', desc: 'Mechanical engineering senior capstone project.' },
    ],
  },
  'ce-civil-engineering': {
    code: 'CE',
    name: 'Civil Engineering',
    description:
      'Civil Engineering at GCET prepares students for the design and construction of infrastructure, sustainable buildings, transportation systems, and water resources.',
    courses: [
      { code: 'CE1101', title: 'Surveying', credits: 4, hours: '3-2-6', desc: 'Chain, compass, theodolite, total station, GPS surveying.' },
      { code: 'CE2202', title: 'Strength of Materials', credits: 4, hours: '4-0-8', desc: 'Stress, strain, bending, torsion, deflection of beams.' },
      { code: 'CE2303', title: 'Structural Analysis', credits: 4, hours: '4-0-8', desc: 'Analysis of determinate and indeterminate structures.' },
      { code: 'CE3101', title: 'Concrete Technology', credits: 4, hours: '3-2-6', desc: 'Cement, aggregates, mix design, durability, special concretes.' },
      { code: 'CE3202', title: 'Transportation Engineering', credits: 4, hours: '3-2-6', desc: 'Highway geometric design, pavements, traffic engineering.' },
      { code: 'CE4101', title: 'CE Capstone', credits: 6, hours: '0-6-12', desc: 'Civil engineering capstone design project.' },
    ],
  },
  'ee-electrical-engineering': {
    code: 'EE',
    name: 'Electrical Engineering',
    description:
      'Electrical Engineering focuses on power systems, control, electric machines, renewable energy, and smart grid technologies.',
    courses: [
      { code: 'EE1101', title: 'Circuit Analysis', credits: 4, hours: '3-2-6', desc: 'Nodal/mesh analysis, theorems, transient and steady-state response.' },
      { code: 'EE2202', title: 'Electric Machines', credits: 4, hours: '3-2-6', desc: 'Transformers, DC machines, induction and synchronous machines.' },
      { code: 'EE2303', title: 'Control Systems', credits: 4, hours: '4-0-8', desc: 'Time and frequency response, stability, PID controllers, state-space.' },
      { code: 'EE3101', title: 'Power Systems', credits: 4, hours: '4-0-8', desc: 'Generation, transmission, distribution, load flow, fault analysis.' },
      { code: 'EE3202', title: 'Power Electronics', credits: 4, hours: '3-2-6', desc: 'Rectifiers, inverters, choppers, motor drives.' },
      { code: 'EE4101', title: 'EE Capstone', credits: 6, hours: '0-6-12', desc: 'Electrical engineering senior capstone.' },
    ],
  },
  'mth-mathematics': {
    code: 'MTH',
    name: 'Mathematics',
    description:
      'The Mathematics curriculum supports engineering programs and provides rigorous foundations in analysis, algebra, and applied mathematics.',
    courses: [
      { code: 'MTH1101', title: 'Calculus I', credits: 4, hours: '4-0-8', desc: 'Limits, derivatives, applications, integrals.' },
      { code: 'MTH1202', title: 'Calculus II', credits: 4, hours: '4-0-8', desc: 'Sequences, series, multivariable calculus, vector calculus.' },
      { code: 'MTH2103', title: 'Linear Algebra', credits: 4, hours: '4-0-8', desc: 'Vectors, matrices, linear transformations, eigenvalues.' },
      { code: 'MTH2204', title: 'Differential Equations', credits: 4, hours: '4-0-8', desc: 'ODEs, systems of ODEs, basic PDEs and applications.' },
      { code: 'MTH3101', title: 'Probability & Statistics', credits: 4, hours: '4-0-8', desc: 'Random variables, distributions, hypothesis testing, regression.' },
      { code: 'MTH3202', title: 'Numerical Methods', credits: 4, hours: '3-2-6', desc: 'Root finding, interpolation, numerical integration, ODE solvers.' },
    ],
  },
  'hss-humanities-social-sciences': {
    code: 'HSS',
    name: 'Humanities & Social Sciences',
    description:
      'HSS courses develop communication, ethical reasoning, history, and entrepreneurial thinking — preparing well-rounded engineers.',
    courses: [
      { code: 'HSS1101', title: 'Technical Communication', credits: 3, hours: '3-0-6', desc: 'Writing, presentation, and professional communication skills.' },
      { code: 'HSS2202', title: 'Engineering Economics', credits: 3, hours: '3-0-6', desc: 'Time value of money, project evaluation, cost analysis.' },
      { code: 'HSS2303', title: 'Ethics in Engineering', credits: 3, hours: '3-0-6', desc: 'Professional responsibility, case studies in engineering ethics.' },
      { code: 'HSS3101', title: 'Entrepreneurship', credits: 3, hours: '2-2-5', desc: 'Idea generation, business models, lean startup, funding.' },
      { code: 'HSS3202', title: 'History of Technology', credits: 3, hours: '3-0-6', desc: 'Cultural and contextual evolution of technology.' },
    ],
  },
  'co-curriculars': {
    code: 'CC',
    name: 'Co-curriculars',
    description:
      'Co-curricular offerings encourage holistic growth through sports, music, robotics teams, debate, and community service. These activities are encouraged but not eligible for academic credit.',
    courses: [
      { code: 'CC0001', title: 'Robotics Club', credits: 0, hours: '0-3-0', desc: 'Build and program robots for inter-college competitions.' },
      { code: 'CC0002', title: 'GCET Music Ensemble', credits: 0, hours: '0-2-0', desc: 'Choir and instrumental ensemble open to all students.' },
      { code: 'CC0003', title: 'Community Service', credits: 0, hours: '0-2-0', desc: 'Outreach programs in nearby villages and schools.' },
    ],
  },
};
