import React from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { NAV_TREE } from '../data/mock';

const SectionPage = ({ slug }) => {
  const node = NAV_TREE.find((n) => n.slug === slug);
  if (!node) return null;

  const contentMap = {
    'information-about-gcet': {
      title: 'Information about GCET',
      body: (
        <>
          <p>
            GCET College of Engineering is a premier institute dedicated to producing innovative,
            socially aware, and technically competent engineers. Established in 1984 in V.V. Nagar,
            Gujarat, GCET combines rigorous academics with hands-on, project-based learning.
          </p>
          <p>
            Our undergraduate programs span Computer Science, Information Technology, Electronics,
            Mechanical, Civil, and Electrical engineering. Postgraduate and doctoral programs
            extend research opportunities across all departments.
          </p>
          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Quick Facts
          </h3>
          <table className="catalog-table w-full">
            <tbody>
              <tr>
                <td className="font-semibold">Founded</td>
                <td>1984</td>
              </tr>
              <tr>
                <td className="font-semibold">Location</td>
                <td>V.V. Nagar, Anand, Gujarat, India</td>
              </tr>
              <tr>
                <td className="font-semibold">Affiliation</td>
                <td>Gujarat Technological University (GTU)</td>
              </tr>
              <tr>
                <td className="font-semibold">Accreditation</td>
                <td>NAAC A+, NBA accredited programs</td>
              </tr>
              <tr>
                <td className="font-semibold">Student Body</td>
                <td>~3,200 undergraduate & graduate students</td>
              </tr>
            </tbody>
          </table>
        </>
      ),
    },
    'programs-of-study-and-degree-requirements': {
      title: 'Programs of Study and Degree Requirements',
      body: (
        <>
          <p>
            GCET offers a portfolio of undergraduate (B.Tech), postgraduate (M.Tech) and doctoral
            (Ph.D.) programs. All degrees require successful completion of program-specific core
            courses, electives, capstone experiences, and a minimum cumulative GPA of 6.0/10.
          </p>
          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Degree Requirements at a Glance
          </h3>
          <table className="catalog-table w-full">
            <thead>
              <tr>
                <th>Program</th>
                <th>Duration</th>
                <th>Credits Required</th>
                <th>Capstone</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>B.Tech</td><td>4 years</td><td>160</td><td>Required (Year 4)</td></tr>
              <tr><td>M.Tech</td><td>2 years</td><td>80</td><td>Thesis</td></tr>
              <tr><td>Ph.D.</td><td>3–5 years</td><td>Coursework + Dissertation</td><td>Dissertation</td></tr>
              <tr><td>Minor</td><td>Concurrent</td><td>20</td><td>—</td></tr>
            </tbody>
          </table>
        </>
      ),
    },
    'courses-credits-hours': {
      title: 'Courses, Credits, Hours',
      body: (
        <>
          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-4 mb-2">
            Availability of Offerings
          </h3>
          <p>
            Information in this catalog and semester offerings are subject to change. Please go to
            the{' '}
            <a className="text-[#0a4f8c] underline" href="#registrar">
              Registrar&apos;s webpage
            </a>{' '}
            or the live semester{' '}
            <a className="text-[#0a4f8c] underline" href="#browser">
              course browser
            </a>{' '}
            for up-to-date information including faculty teaching assignments. For more
            information about a specific course, talk to the course instructor listed in the
            current or previous registration booklets. Prerequisites and co-requisites may
            occasionally be waived with permission of the course instructor.
          </p>

          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Course Numbering Nomenclature
          </h3>
          <p>
            Course numbers are composed of an alphabetic prefix and a numeric suffix. The alphabetic
            prefix indicates the primary area of the course, according to the following table.
          </p>
          <table className="catalog-table w-full">
            <thead>
              <tr><th>Alphabetic Prefix</th><th>Primary Area</th></tr>
            </thead>
            <tbody>
              <tr><td>CSE</td><td>Computer Science & Engineering</td></tr>
              <tr><td>IT</td><td>Information Technology</td></tr>
              <tr><td>ECE</td><td>Electronics & Communication</td></tr>
              <tr><td>ME</td><td>Mechanical Engineering</td></tr>
              <tr><td>CE</td><td>Civil Engineering</td></tr>
              <tr><td>EE</td><td>Electrical Engineering</td></tr>
              <tr><td>MTH</td><td>Mathematics</td></tr>
              <tr><td>HSS</td><td>Humanities & Social Sciences</td></tr>
            </tbody>
          </table>

          <p className="mt-4">The first digit of the numeric suffix indicates the nominal level of a course.</p>
          <table className="catalog-table w-full">
            <thead>
              <tr><th>Numeric Suffix</th><th>Level</th></tr>
            </thead>
            <tbody>
              <tr><td>0XXX</td><td>Any</td></tr>
              <tr><td>1XXX</td><td>Introductory</td></tr>
              <tr><td>2XXX</td><td>Intermediate</td></tr>
              <tr><td>3XXX</td><td>Advanced</td></tr>
              <tr><td>4XXX</td><td>Summative / Capstone</td></tr>
            </tbody>
          </table>

          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Hours/Week Nomenclature
          </h3>
          <p>
            At GCET, 1 credit is equal to 3 hours of work per week. The standard calendar is 15
            weeks per semester. To better allow teaching staff, facilities schedulers, and students
            to manage time, the expected hours per week is indicated by a triplet:
            (Contact)–(Non‑Contact)–(Preparation).
          </p>
          <ul className="list-disc pl-6 my-3">
            <li><b>Contact:</b> hours per week in scheduled classes with the instructor.</li>
            <li><b>Non-Contact:</b> hours per week working in scheduled school facilities.</li>
            <li><b>Preparation:</b> hours per week a well-prepared student should spend studying outside class.</li>
          </ul>
          <p>
            For example, HSS1101 Technical Communication is a 3‑0‑6 course — three hours in class
            and six hours of outside-of-class preparation.
          </p>

          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Activities Not Eligible for Credit
          </h3>
          <p>
            Areas of student engagement not eligible for credit include clubs, competition teams,
            community service, and recreation. We encourage students to engage with these as part
            of the broader learning continuum.
          </p>

          <ul className="list-none mt-6 space-y-2">
            {node.children.map((c) => (
              <li key={c.slug}>
                <Link
                  to={`/en/2024-25/catalog/${node.slug}/${c.slug}`}
                  className="text-[#0a4f8c] hover:underline"
                >
                  {c.label}
                </Link>
              </li>
            ))}
          </ul>
        </>
      ),
    },
    'academic-policies-and-procedures': {
      title: 'Academic Policies and Procedures',
      body: (
        <>
          <p>
            Academic policies at GCET are intended to support student learning while ensuring
            integrity, fairness, and consistency across programs. The sections below outline the
            principal regulations governing admissions, grading, attendance, and academic conduct.
          </p>
          <ul className="list-none mt-4 space-y-2">
            {node.children.map((c) => (
              <li key={c.slug}>
                <Link
                  to={`/en/2024-25/catalog/${node.slug}/${c.slug}`}
                  className="text-[#0a4f8c] hover:underline"
                >
                  {c.label}
                </Link>
              </li>
            ))}
          </ul>
        </>
      ),
    },
    'table-of-contents': {
      title: 'Table of Contents',
      body: (
        <ul className="space-y-3">
          {NAV_TREE.map((n) => (
            <li key={n.slug}>
              <Link
                to={`/en/2024-25/catalog/${n.slug}`}
                className="text-[#0a4f8c] font-semibold hover:underline"
              >
                {n.label}
              </Link>
              {n.children && (
                <ul className="list-disc pl-6 mt-1">
                  {n.children.map((c) => (
                    <li key={c.slug}>
                      <Link
                        to={`/en/2024-25/catalog/${n.slug}/${c.slug}`}
                        className="text-[#0a4f8c] hover:underline"
                      >
                        {c.label}
                      </Link>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      ),
    },
  };

  const data = contentMap[slug];

  return (
    <Layout>
      <h1 className="font-serif text-[36px] text-[#0a4f8c] font-semibold mb-4 leading-tight">
        {data.title}
      </h1>
      <div className="text-[15px] leading-7 text-gray-800 space-y-3">{data.body}</div>
    </Layout>
  );
};

export default SectionPage;
