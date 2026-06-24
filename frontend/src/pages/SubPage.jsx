import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { catalogApi } from '../api/client';
import { useCatalog, useYear } from '../context/CatalogContext';

const SubPage = () => {
  const { section, sub } = useParams();
  const year = useYear();
  const { navTree } = useCatalog();
  const parent = navTree.find((n) => n.slug === section);

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let alive = true;
    setLoading(true);
    catalogApi
      .getInfoPage(sub)
      .then((d) => alive && setData(d))
      .catch(() => alive && setData(null))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [sub]);

  if (loading) {
    return (
      <Layout>
        <p className="text-gray-500">Loading…</p>
      </Layout>
    );
  }

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
                  to={`/en/${year}/catalog/${parent.slug}/${c.slug}`}
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
