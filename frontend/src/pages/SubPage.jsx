import React from 'react';
import { useParams, Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { NAV_TREE } from '../data/mock';

const LOREM_MAP = {
  // Information about GCET
  'mission-and-vision': {
    title: 'Mission and Vision',
    body: [
      'Our Mission: To shape engineers who are technically excellent, ethically grounded, and committed to sustainable problem solving for the communities they serve.',
      'Our Vision: To be recognized globally as a leader in undergraduate engineering education — producing graduates who design responsibly, lead inclusively, and innovate boldly.',
      'Core Values: Integrity, Curiosity, Collaboration, Sustainability, and Impact.',
    ],
  },
  history: {
    title: 'History of GCET',
    body: [
      'Founded in 1984, GCET began with a single building and four undergraduate programs, dedicated to bringing modern engineering education to the V.V. Nagar region of Gujarat.',
      'Through the 1990s and 2000s, the institute expanded its computing, electronics, and mechanical departments and established research labs in robotics, embedded systems, and renewable energy.',
      'Today, GCET serves more than 3,000 students across undergraduate, masters, and doctoral programs, with strong industry partnerships across India and abroad.',
    ],
  },
  accreditation: {
    title: 'Accreditation',
    body: [
      'GCET is accredited by the National Assessment and Accreditation Council (NAAC) with an A+ grade.',
      'Several B.Tech programs are accredited by the National Board of Accreditation (NBA), including Computer Science & Engineering, Information Technology, and Electronics & Communication.',
      'The institute is affiliated with Gujarat Technological University (GTU).',
    ],
  },
  'campus-life': {
    title: 'Campus Life',
    body: [
      'Life at GCET extends well beyond the classroom. Students participate in 40+ clubs across robotics, music, drama, debate, photography, and entrepreneurship.',
      'Annual events such as Synapse (technical fest), Pulse (cultural fest), and the GCET Hackathon bring students together across departments and years.',
      'On-campus residence halls, libraries open 24/7 during exam weeks, and modern lab facilities support both academic work and creative exploration.',
    ],
  },
  // Programs
  'btech-programs': {
    title: 'B.Tech Programs',
    body: [
      'GCET offers Bachelor of Technology (B.Tech) degrees across six engineering disciplines. Each B.Tech program requires the completion of 160 credits over four academic years, including foundational, core, elective, capstone, and HSS courses.',
      'Students may choose elective tracks in areas such as Artificial Intelligence, Robotics, Renewable Energy, Sustainable Construction, and Embedded Systems.',
    ],
  },
  'mtech-programs': {
    title: 'M.Tech Programs',
    body: [
      'M.Tech programs at GCET are research-intensive, two-year degrees offered in CSE, ECE, ME, CE, and EE. The curriculum combines advanced coursework with a year-long thesis.',
      'Each program requires 80 credits including 40 credits of thesis research, mentored by faculty.',
    ],
  },
  'phd-programs': {
    title: 'Ph.D. Programs',
    body: [
      'Doctoral students at GCET pursue independent research under faculty advisors, contributing to scholarship across computing, electronics, materials, structures, and sustainable engineering.',
      'Ph.D. candidates complete coursework in their first year, qualifying exams in their second year, and a defended dissertation typically by year 4 or 5.',
    ],
  },
  'minor-programs': {
    title: 'Minor Programs',
    body: [
      'Minors enable students to develop expertise outside their primary major. A minor requires 20 credits and may be added concurrently with a B.Tech degree.',
      'Available minors include Data Science, Robotics, Entrepreneurship, Sustainability, and Mathematics.',
    ],
  },
  // Academic Policies
  'admission-policies': {
    title: 'Admission Policies',
    body: [
      'B.Tech admissions are based on performance in the Gujarat Common Entrance Test (GUJCET) and JEE Main, in accordance with state guidelines.',
      'M.Tech admissions are based on a valid GATE score and an interview. Direct admissions are also available for sponsored candidates.',
      'International applicants are evaluated on equivalent national entrance examinations and English-language proficiency.',
    ],
  },
  'grading-system': {
    title: 'Grading System',
    body: [
      'GCET follows a 10-point grading scale (CGPA). Letter grades (AA, AB, BB, BC, CC, CD, DD, FF) map to grade points from 10 down to 0.',
      'A minimum CGPA of 6.0 is required for graduation. Students with a CGPA below 5.0 are placed on academic probation.',
    ],
  },
  attendance: {
    title: 'Attendance Requirements',
    body: [
      'Students are expected to maintain a minimum of 75% attendance in every course they are registered for.',
      'Failure to meet this requirement may result in the student being barred from end-semester examinations.',
    ],
  },
  'academic-integrity': {
    title: 'Academic Integrity',
    body: [
      'GCET upholds the highest standards of academic integrity. Plagiarism, unauthorized collaboration, fabrication of data, and other forms of academic dishonesty are strictly prohibited.',
      'Violations are reviewed by the Academic Integrity Committee and may result in penalties ranging from a zero on the assignment to expulsion from the institute.',
    ],
  },
};

const SubPage = () => {
  const { section, sub } = useParams();
  const data = LOREM_MAP[sub];
  const parent = NAV_TREE.find((n) => n.slug === section);

  if (!data || !parent) {
    return (
      <Layout>
        <h1 className="font-serif text-[28px] text-[#0a4f8c] mb-4">Page not found</h1>
        <p>The requested page does not exist in this catalog.</p>
      </Layout>
    );
  }

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-4 leading-tight">
        {data.title}
      </h1>
      <div className="text-[15px] leading-7 text-gray-800 space-y-4">
        {data.body.map((p, i) => (
          <p key={i}>{p}</p>
        ))}
      </div>
      <div className="mt-10 border-t border-gray-200 pt-4">
        <h3 className="font-serif text-[#0a4f8c] text-[18px] font-semibold mb-2">
          More in {parent.label}
        </h3>
        <ul className="list-disc pl-6">
          {parent.children
            .filter((c) => c.slug !== sub)
            .map((c) => (
              <li key={c.slug}>
                <Link
                  className="text-[#0a4f8c] hover:underline"
                  to={`/en/2024-25/catalog/${parent.slug}/${c.slug}`}
                >
                  {c.label}
                </Link>
              </li>
            ))}
        </ul>
      </div>
    </Layout>
  );
};

export default SubPage;
