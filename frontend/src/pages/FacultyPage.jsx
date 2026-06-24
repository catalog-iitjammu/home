import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import Layout from '../components/Layout';
import { catalogApi } from '../api/client';
import { useCatalog, useYear } from '../context/CatalogContext';

const FacultyPage = () => {
  const { group } = useParams();
  const year = useYear();
  const { navTree } = useCatalog();
  const parent = navTree.find((n) => n.slug === 'faculty');

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let alive = true;
    if (!group) {
      setData(null);
      return;
    }
    setLoading(true);
    catalogApi
      .getFacultyGroup(group)
      .then((d) => alive && setData(d))
      .catch(() => alive && setData(null))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [group]);

  if (!group) {
    return (
      <Layout>
        <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-4">Faculty</h1>
        <p className="text-[15px] leading-7 text-gray-800 mb-6">
          IIT Jammu’s faculty are accomplished researchers and dedicated teachers across
          engineering, sciences, and humanities. Use the links below to browse by group.
        </p>
        <ul className="list-disc pl-6">
          {parent &&
            parent.children.map((c) => (
              <li key={c.slug}>
                <Link
                  className="text-[#0a4f8c] hover:underline"
                  to={`/en/${year}/catalog/faculty/${c.slug}`}
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
        <p className="text-gray-500">Loading faculty…</p>
      </Layout>
    );
  }

  if (!data) {
    return (
      <Layout>
        <h1 className="font-serif text-[28px] text-[#0a4f8c] mb-4">Faculty group not found</h1>
      </Layout>
    );
  }

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-3">{data.title}</h1>
      <p className="text-[15px] leading-7 text-gray-800 mb-6">{data.intro}</p>
      <table className="catalog-table w-full">
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
            <th>Area</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {data.members.map((m) => (
            <tr key={m.email}>
              <td className="font-semibold text-[#0a4f8c]">{m.name}</td>
              <td>{m.role}</td>
              <td>{m.area}</td>
              <td>
                <a href={`mailto:${m.email}`} className="text-[#0a4f8c] hover:underline">
                  {m.email}
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {parent && (
        <div className="mt-10 border-t border-gray-200 pt-4">
          <h3 className="font-serif text-[#0a4f8c] text-[18px] font-semibold mb-2">
            Other Faculty Groups
          </h3>
          <ul className="list-disc pl-6">
            {parent.children
              .filter((c) => c.slug !== group)
              .map((c) => (
                <li key={c.slug}>
                  <Link
                    className="text-[#0a4f8c] hover:underline"
                    to={`/en/${year}/catalog/faculty/${c.slug}`}
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

export default FacultyPage;
