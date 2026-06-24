import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Printer } from 'lucide-react';
import { useCatalog, useYear, parseYearFromVersion } from '../context/CatalogContext';

const buildBreadcrumb = (pathname, navTree, year) => {
  const parts = pathname.split('/').filter(Boolean);
  const catalogIdx = parts.indexOf('catalog');
  const after = parts.slice(catalogIdx + 1);
  const crumbs = [{ label: `Catalog ${year}`, to: `/en/${year}/catalog` }];
  if (after.length === 0) return crumbs;
  const first = navTree.find((n) => n.slug === after[0]);
  if (first) {
    crumbs.push({
      label: first.label,
      to: `/en/${year}/catalog/${first.slug}`,
    });
    if (after[1] && first.children) {
      const child = first.children.find((c) => c.slug === after[1]);
      if (child) {
        crumbs.push({
          label: child.label,
          to: `/en/${year}/catalog/${first.slug}/${child.slug}`,
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
  const navigate = useNavigate();
  const year = useYear();
  const { navTree, versions } = useCatalog();
  // Initialize selector from URL year so it stays in sync
  const initialVersion =
    versions.find((v) => v.includes(year)) || (versions.length ? versions[0] : `Catalog ${year}`);
  const [version, setVersion] = useState(initialVersion);

  useEffect(() => {
    const v = versions.find((x) => x.includes(year));
    if (v) setVersion(v);
  }, [year, versions]);

  const crumbs = buildBreadcrumb(location.pathname, navTree, year);

  const handlePrint = () => window.print();

  const handleSelect = () => {
    const newYear = parseYearFromVersion(version);
    if (newYear && newYear !== year) {
      navigate(`/en/${newYear}/catalog`);
    } else {
      // Same year — just refresh the home of this catalog
      navigate(`/en/${year}/catalog`);
    }
  };

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
          {versions.map((v) => (
            <option key={v}>{v}</option>
          ))}
        </select>
        <button
          type="button"
          onClick={handleSelect}
          className="text-[13px] font-serif px-3 py-[3px] border border-gray-400 bg-gradient-to-b from-white to-gray-100 hover:from-gray-50 hover:to-gray-200 rounded-sm"
        >
          Select
        </button>
      </div>
    </div>
  );
};

export default TopBar;
