import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import Layout from '../components/Layout';
import { catalogApi } from '../api/client';
import { useCatalog, useYear } from '../context/CatalogContext';

const FeesPage = () => {
  const { sub } = useParams();
  const year = useYear();
  const { navTree } = useCatalog();
  const parent = navTree.find((n) => n.slug === 'fees-and-financial-aid');

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let alive = true;
    if (!sub) {
      setData(null);
      return;
    }
    setLoading(true);
    catalogApi
      .getFee(sub)
      .then((d) => alive && setData(d))
      .catch(() => alive && setData(null))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [sub]);

  if (!sub) {
    return (
      <Layout>
        <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-4">
          Fees and Financial Aid
        </h1>
        <p className="text-[15px] leading-7 text-gray-800 mb-6">
          IIT Jammu strives to ensure that no admitted student is denied education for want of
          financial resources. The sections below summarize tuition, hostel &amp; mess charges,
          and available scholarships and aid.
        </p>
        <ul className="list-disc pl-6">
          {parent &&
            parent.children.map((c) => (
              <li key={c.slug}>
                <Link
                  className="text-[#0a4f8c] hover:underline"
                  to={`/en/${year}/catalog/fees-and-financial-aid/${c.slug}`}
                >
                  {c.label}
                </Link>
              </li>
            ))}
        </ul>
      </Layout>
    );
  }

  if (loading) {
    return (
      <Layout>
        <p className="text-gray-500">Loading fees…</p>
      </Layout>
    );
  }

  if (!data) {
    return (
      <Layout>
        <h1 className="font-serif text-[28px] text-[#0a4f8c] mb-4">Page not found</h1>
      </Layout>
    );
  }

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-3">{data.title}</h1>
      <p className="text-[15px] leading-7 text-gray-800 mb-6">{data.intro}</p>
      {data.tables.map((t) => (
        <div key={t.heading} className="mb-8">
          <h2 className="font-serif text-[20px] text-[#0a4f8c] font-semibold mb-2">{t.heading}</h2>
          <table className="catalog-table w-full">
            <thead>
              <tr>
                {t.columns.map((c) => (
                  <th key={c}>{c}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {t.rows.map((row, i) => (
                <tr key={i}>
                  {row.map((cell, j) => (
                    <td key={j} className={j === 0 ? 'font-semibold' : ''}>
                      {cell}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}
      {parent && (
        <div className="mt-10 border-t border-gray-200 pt-4">
          <h3 className="font-serif text-[#0a4f8c] text-[18px] font-semibold mb-2">More in Fees</h3>
          <ul className="list-disc pl-6">
            {parent.children
              .filter((c) => c.slug !== sub)
              .map((c) => (
                <li key={c.slug}>
                  <Link
                    className="text-[#0a4f8c] hover:underline"
                    to={`/en/${year}/catalog/fees-and-financial-aid/${c.slug}`}
                  >
                    {c.label}
                  </Link>
                </li>
              ))}
          </ul>
        </div>
      )}
    </Layout>
  );
};

export default FeesPage;
