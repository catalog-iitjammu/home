import React from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { useCatalog, useYear } from '../context/CatalogContext';

const SectionPage = ({ slug }) => {
  const { navTree } = useCatalog();
  const year = useYear();
  const node = navTree.find((n) => n.slug === slug);
  if (!node) return null;

  const linkBase = `/en/${year}/catalog`;

  const contentMap = {
    'information-about-iitjammu': {
      title: 'Information about IIT Jammu',
      body: (
        <>
          <p>
            The Indian Institute of Technology Jammu (IIT Jammu) is an autonomous Institute of
            National Importance established in 2016 by an Act of the Parliament of India. The
            permanent campus is located at Jagti, Nagrota, in the Union Territory of Jammu and
            Kashmir.
          </p>
          <p>
            IIT Jammu offers a portfolio of undergraduate (B.Tech), postgraduate (M.Tech, M.Sc.),
            and doctoral (Ph.D.) programs across engineering, sciences, and humanities, supported
            by research centers in AI, sustainability, advanced materials, and 5G/6G
            communications.
          </p>
          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Quick Facts
          </h3>
          <table className="catalog-table w-full">
            <tbody>
              <tr><td className="font-semibold">Founded</td><td>2016</td></tr>
              <tr><td className="font-semibold">Status</td><td>Institute of National Importance (by Act of Parliament)</td></tr>
              <tr><td className="font-semibold">Location</td><td>Jagti, Nagrota, Jammu & Kashmir, India</td></tr>
              <tr><td className="font-semibold">Campus Size</td><td>~400 acres in the Shivalik foothills</td></tr>
              <tr><td className="font-semibold">Director</td><td>Prof. Manoj Singh Gaur</td></tr>
              <tr><td className="font-semibold">Student Body</td><td>~1,800 students (B.Tech, M.Tech, M.Sc., Ph.D.)</td></tr>
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
            IIT Jammu offers a portfolio of undergraduate (B.Tech), postgraduate (M.Tech and
            M.Sc.) and doctoral (Ph.D.) programs. All degrees require successful completion of
            program-specific core courses, electives, capstone experiences, and a minimum
            cumulative GPA of 5.0/10.
          </p>
          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Degree Requirements at a Glance
          </h3>
          <table className="catalog-table w-full">
            <thead>
              <tr><th>Program</th><th>Duration</th><th>Credits Required</th><th>Capstone</th></tr>
            </thead>
            <tbody>
              <tr><td>B.Tech</td><td>4 years</td><td>~160</td><td>Required (Year 4)</td></tr>
              <tr><td>M.Tech</td><td>2 years</td><td>~64</td><td>Thesis</td></tr>
              <tr><td>M.Sc.</td><td>2 years</td><td>~60</td><td>Project</td></tr>
              <tr><td>Ph.D.</td><td>3–5 years</td><td>Coursework + Dissertation</td><td>Dissertation</td></tr>
              <tr><td>Minor / Honors</td><td>Concurrent</td><td>18–20</td><td>—</td></tr>
            </tbody>
          </table>
          <ul className="list-none mt-6 space-y-2">
            {node.children.map((c) => (
              <li key={c.slug}>
                <Link className="text-[#0a4f8c] hover:underline" to={`${linkBase}/${node.slug}/${c.slug}`}>
                  {c.label}
                </Link>
              </li>
            ))}
          </ul>
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
            for up-to-date information including faculty teaching assignments.
          </p>

          <h3 className="font-serif text-[#0a4f8c] text-[20px] font-semibold mt-6 mb-2">
            Course Numbering Nomenclature
          </h3>
          <p>
            Course numbers are composed of an alphabetic prefix (3 letters) followed by a 4-digit
            numeric suffix. The alphabetic prefix indicates the primary area of the course.
          </p>
          <table className="catalog-table w-full">
            <thead><tr><th>Alphabetic Prefix</th><th>Primary Area</th></tr></thead>
            <tbody>
              <tr><td>CSL / CSP</td><td>Computer Science & Engineering</td></tr>
              <tr><td>ECL / ECP</td><td>Electronics & Communication</td></tr>
              <tr><td>EEL / EEP</td><td>Electrical Engineering</td></tr>
              <tr><td>MEL / MEP</td><td>Mechanical Engineering</td></tr>
              <tr><td>CEL / CEP</td><td>Civil Engineering</td></tr>
              <tr><td>CHL / CHP</td><td>Chemical Engineering</td></tr>
              <tr><td>MSL / MSP</td><td>Materials Science & Engineering</td></tr>
              <tr><td>MAL</td><td>Mathematics</td></tr>
              <tr><td>PHL</td><td>Physics</td></tr>
              <tr><td>CYL</td><td>Chemistry</td></tr>
              <tr><td>HUL</td><td>Humanities & Social Sciences</td></tr>
            </tbody>
          </table>

          <p className="mt-4">The first digit of the numeric suffix indicates the nominal level of a course.</p>
          <table className="catalog-table w-full">
            <thead><tr><th>Numeric Suffix</th><th>Level</th></tr></thead>
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
            At IIT Jammu, 1 credit is equal to 3 hours of work per week. The standard calendar is
            16 weeks per semester. Hours per week are indicated by the triplet:
            (Contact)–(Non-Contact)–(Preparation).
          </p>
          <ul className="list-disc pl-6 my-3">
            <li><b>Contact:</b> scheduled class hours with the instructor.</li>
            <li><b>Non-Contact:</b> scheduled lab / studio hours.</li>
            <li><b>Preparation:</b> independent study and homework.</li>
          </ul>

          <ul className="list-none mt-6 space-y-2">
            {node.children.map((c) => (
              <li key={c.slug}>
                <Link to={`${linkBase}/${node.slug}/${c.slug}`} className="text-[#0a4f8c] hover:underline">
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
            Academic policies at IIT Jammu are designed to support student learning while ensuring
            integrity, fairness, and consistency across programs.
          </p>
          <ul className="list-none mt-4 space-y-2">
            {node.children.map((c) => (
              <li key={c.slug}>
                <Link to={`${linkBase}/${node.slug}/${c.slug}`} className="text-[#0a4f8c] hover:underline">
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
          {navTree.map((n) => (
            <li key={n.slug}>
              <Link to={`${linkBase}/${n.slug}`} className="text-[#0a4f8c] font-semibold hover:underline">
                {n.label}
              </Link>
              {n.children && (
                <ul className="list-disc pl-6 mt-1">
                  {n.children.map((c) => (
                    <li key={c.slug}>
                      <Link to={`${linkBase}/${n.slug}/${c.slug}`} className="text-[#0a4f8c] hover:underline">
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
  if (!data) return null;

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
