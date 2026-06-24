import React from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import Layout from '../components/Layout';
import { NAV_TREE, DEPARTMENTS } from '../data/mock';

const SearchPage = () => {
  const [params] = useSearchParams();
  const q = (params.get('q') || '').toLowerCase();
  const scope = params.get('scope') || 'Entire Catalog';

  const results = [];

  if (q) {
    if (scope === 'Entire Catalog' || scope === 'Programs') {
      NAV_TREE.forEach((n) => {
        if (n.label.toLowerCase().includes(q)) {
          results.push({
            label: n.label,
            url: `/en/2024-25/catalog/${n.slug}`,
            type: 'Section',
          });
        }
        (n.children || []).forEach((c) => {
          if (c.label.toLowerCase().includes(q)) {
            results.push({
              label: `${n.label} › ${c.label}`,
              url: `/en/2024-25/catalog/${n.slug}/${c.slug}`,
              type: 'Page',
            });
          }
        });
      });
    }
    if (scope === 'Entire Catalog' || scope === 'Courses') {
      Object.entries(DEPARTMENTS).forEach(([slug, d]) => {
        d.courses.forEach((c) => {
          if (
            c.code.toLowerCase().includes(q) ||
            c.title.toLowerCase().includes(q) ||
            c.desc.toLowerCase().includes(q)
          ) {
            results.push({
              label: `${c.code} – ${c.title}`,
              url: `/en/2024-25/catalog/courses-credits-hours/${slug}`,
              type: 'Course',
            });
          }
        });
      });
    }
  }

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-4">
        Search Results
      </h1>
      <p className="text-[14px] text-gray-700 mb-6">
        {q ? (
          <>
            Showing {results.length} result{results.length === 1 ? '' : 's'} for{' '}
            <span className="font-semibold">“{q}”</span> in{' '}
            <span className="italic">{scope}</span>.
          </>
        ) : (
          'Enter a search term in the left sidebar.'
        )}
      </p>
      <ul className="space-y-3">
        {results.map((r, i) => (
          <li key={i} className="border-b border-gray-200 pb-3">
            <Link to={r.url} className="text-[#0a4f8c] hover:underline font-semibold">
              {r.label}
            </Link>
            <div className="text-[12px] uppercase tracking-wide text-gray-500">{r.type}</div>
          </li>
        ))}
      </ul>
    </Layout>
  );
};

export default SearchPage;
