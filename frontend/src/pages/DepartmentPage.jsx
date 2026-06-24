import React from 'react';
import { useParams, Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { DEPARTMENTS, NAV_TREE } from '../data/mock';

const DepartmentPage = () => {
  const { dept } = useParams();
  const data = DEPARTMENTS[dept];

  if (!data) {
    return (
      <Layout>
        <h1 className="font-serif text-[28px] text-[#0a4f8c] mb-4">Department not found</h1>
        <p>The requested department does not exist in this catalog.</p>
      </Layout>
    );
  }

  const parent = NAV_TREE.find((n) => n.slug === 'courses-credits-hours');
  const siblings = parent ? parent.children : [];

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-2 leading-tight">
        {data.code} – {data.name}
      </h1>
      <p className="text-[15px] leading-7 text-gray-800 mb-6">{data.description}</p>

      <h2 className="font-serif text-[22px] text-[#0a4f8c] font-semibold mb-3">Course Listings</h2>
      <table className="catalog-table w-full mb-8">
        <thead>
          <tr>
            <th style={{ width: '110px' }}>Code</th>
            <th>Course Title</th>
            <th style={{ width: '90px' }}>Credits</th>
            <th style={{ width: '110px' }}>C‑NC‑P</th>
          </tr>
        </thead>
        <tbody>
          {data.courses.map((c) => (
            <tr key={c.code}>
              <td className="font-semibold text-[#0a4f8c]">{c.code}</td>
              <td>
                <div className="font-semibold">{c.title}</div>
                <div className="text-[13px] text-gray-700">{c.desc}</div>
              </td>
              <td>{c.credits}</td>
              <td>{c.hours}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="mt-8 border-t border-gray-200 pt-4">
        <h3 className="font-serif text-[#0a4f8c] text-[18px] font-semibold mb-2">
          Other Departments in Courses, Credits, Hours
        </h3>
        <ul className="list-disc pl-6">
          {siblings
            .filter((s) => s.slug !== dept)
            .map((s) => (
              <li key={s.slug}>
                <Link
                  className="text-[#0a4f8c] hover:underline"
                  to={`/en/2024-25/catalog/courses-credits-hours/${s.slug}`}
                >
                  {s.label}
                </Link>
              </li>
            ))}
        </ul>
      </div>
    </Layout>
  );
};

export default DepartmentPage;
