import React, { useEffect, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import Layout from '../components/Layout';
import { catalogApi } from '../api/client';
import { useYear } from '../context/CatalogContext';

const SearchPage = () => {
  const [params] = useSearchParams();
  const q = params.get('q') || '';
  const scope = params.get('scope') || 'Entire Catalog';
  const year = useYear();

  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    if (!q) {
      setResults([]);
      return;
    }
    setLoading(true);
    setError(null);
    catalogApi
      .search(q, scope)
      .then((d) => alive && setResults(d.results || []))
      .catch((e) => alive && setError(e))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, [q, scope]);

  // Rewrite year segment in backend-provided URL to current year
  const rewriteYear = (url) => {
    if (!url) return url;
    return url.replace(/^\/en\/\d{4}-\d{2}\//, `/en/${year}/`);
  };

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-4">Search Results</h1>
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
      {loading && <p className="text-gray-500">Searching…</p>}
      {error && <p className="text-red-600 text-sm">Search failed. Please try again.</p>}
      <ul className="space-y-3">
        {results.map((r, i) => (
          <li key={i} className="border-b border-gray-200 pb-3">
            <Link to={rewriteYear(r.url)} className="text-[#0a4f8c] hover:underline font-semibold">
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
