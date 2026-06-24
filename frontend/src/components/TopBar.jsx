import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Printer } from 'lucide-react';
import { CATALOG_VERSIONS, NAV_TREE } from '../data/mock';

const findBreadcrumb = (pathname) => {
  // pathname e.g. /en/2024-25/catalog/courses-credits-hours/cse-...
  const parts = pathname.split('/').filter(Boolean);
  const catalogIdx = parts.indexOf('catalog');
  const after = parts.slice(catalogIdx + 1);
  const crumbs = [{ label: 'Catalog 2024-25', to: '/en/2024-25/catalog' }];
  if (after.length === 0) return crumbs;
  const first = NAV_TREE.find((n) => n.slug === after[0]);
  if (first) {
    crumbs.push({
      label: first.label,
      to: `/en/2024-25/catalog/${first.slug}`,
    });
    if (after[1] && first.children) {
      const child = first.children.find((c) => c.slug === after[1]);
      if (child) {
        crumbs.push({
          label: child.label,
          to: `/en/2024-25/catalog/${first.slug}/${child.slug}`,
        });
      }
    }
  } else if (after[0] === 'search') {
    crumbs.push({ label: 'Search Results', to: pathname });
  }
  return crumbs;
};

const TopBar = () => {
  const location = useLocation();
  const crumbs = findBreadcrumb(location.pathname);
  const [version, setVersion] = useState('Catalog 2024-25');

  const handlePrint = () => window.print();

  return (
    <div className="flex flex-col gap-2 mb-4">
      <div className="flex items-start justify-between gap-4 flex-wrap">
        <nav className="text-[14px] font-serif text-[#0a4f8c]" aria-label="Breadcrumb">
          {crumbs.map((c, idx) => (
            <span key={c.to + idx}>
              {idx > 0 && <span className="mx-1 text-gray-500">»</span>}
              {idx < crumbs.length - 1 ? (
                <Link to={c.to} className="hover:underline">
                  {c.label}
                </Link>
              ) : (
                <span className="text-gray-700">{c.label}</span>
              )}
            </span>
          ))}
        </nav>
        <button
          type="button"
          onClick={handlePrint}
          className="flex items-center gap-1 text-[13px] font-serif text-[#0a4f8c] hover:underline"
        >
          <Printer size={14} />
          Print this page
        </button>
      </div>
      <div className="flex justify-end items-center gap-2">
        <select
          value={version}
          onChange={(e) => setVersion(e.target.value)}
          className="text-[13px] font-serif border border-gray-300 bg-white px-2 py-[3px] rounded-sm"
          aria-label="Catalog version"
        >
          {CATALOG_VERSIONS.map((v) => (
            <option key={v}>{v}</option>
          ))}
        </select>
        <button
          type="button"
          className="text-[13px] font-serif px-3 py-[3px] border border-gray-400 bg-gradient-to-b from-white to-gray-100 hover:from-gray-50 hover:to-gray-200 rounded-sm"
          onClick={() => alert(`Switched to ${version} (mock)`) }
        >
          Select
        </button>
      </div>
    </div>
  );
};

export default TopBar;
