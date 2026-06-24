import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { catalogApi } from '../api/client';
import { useCatalog, useYear } from '../context/CatalogContext';

const DepartmentPage = () => {
  const { dept } = useParams();
  const year = useYear();
  const { navTree } = useCatalog();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    setLoading(true);
    setError(null);
    catalogApi
      .getDepartment(dept)
      .then((d) => alive && setData(d))
      .catch((e) => alive && setError(e))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [dept]);

  if (loading) {
    return (
      <Layout>
        <p className="text-gray-500">Loading department…</p>
      </Layout>
    );
  }

  if (error || !data) {
    return (
      <Layout>
        <h1 className="font-serif text-[28px] text-[#0a4f8c] mb-4">Department not found</h1>
        <p>The requested department does not exist in this catalog.</p>
      </Layout>
    );
  }

  const parent = navTree.find((n) => n.slug === 'courses-credits-hours');
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
            <th style={{ width: '110px' }}>C-NC-P</th>
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
                  to={`/en/${year}/catalog/courses-credits-hours/${s.slug}`}
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
