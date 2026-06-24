import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Search, ChevronRight } from 'lucide-react';
import { useCatalog, useYear } from '../context/CatalogContext';

const Sidebar = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const year = useYear();
  const { navTree, versions, currentVersion } = useCatalog();
  const [openSet, setOpenSet] = useState(new Set());
  const [scope, setScope] = useState('Entire Catalog');
  const [query, setQuery] = useState('');
  const [version, setVersion] = useState(currentVersion);

  useEffect(() => {
    setVersion(currentVersion);
  }, [currentVersion]);

  const toggle = (slug) => {
    setOpenSet((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) next.delete(slug);
      else next.add(slug);
      return next;
    });
  };

  const handleSearch = (e) => {
    e.preventDefault();
    const q = query.trim();
    if (!q) return;
    navigate(
      `/en/${year}/catalog/search?q=${encodeURIComponent(q)}&scope=${encodeURIComponent(scope)}`,
    );
  };

  const isOpen = (node) => {
    const fullPath = `/en/${year}/catalog/${node.slug}`;
    return openSet.has(node.slug) || location.pathname.startsWith(fullPath);
  };

  const isActive = (path) => location.pathname === path;

  return (
    <aside className="w-full lg:w-[280px] shrink-0 lg:pr-6">
      {/* Search */}
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Search size={20} className="text-[#0a4f8c]" strokeWidth={2.5} />
          <span className="sr-only">Catalog Search</span>
        </div>
        <form onSubmit={handleSearch} className="space-y-2">
          <div className="flex items-center gap-1 border border-gray-300 bg-white rounded-sm px-2 py-1">
            <Search size={14} className="text-gray-500" />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search the catalog…"
              className="flex-1 text-[13px] font-serif outline-none bg-transparent"
              aria-label="Search"
            />
          </div>
          <div className="text-[12px] font-serif text-gray-700">Search Options</div>
          <div className="flex items-center gap-2">
            <select
              value={scope}
              onChange={(e) => setScope(e.target.value)}
              className="text-[13px] font-serif border border-gray-300 bg-white px-1 py-[2px] rounded-sm"
            >
              <option>Entire Catalog</option>
              <option>Programs</option>
              <option>Courses</option>
            </select>
            <button
              type="submit"
              className="text-[13px] font-serif px-3 py-[2px] border border-gray-400 bg-gradient-to-b from-white to-gray-100 hover:from-gray-50 hover:to-gray-200 rounded-sm"
            >
              Search
            </button>
          </div>
        </form>
      </div>

      {/* Contents tree */}
      <div className="mb-8">
        <h2 className="font-serif text-[20px] text-[#0a4f8c] font-semibold mb-2">Contents</h2>
        <ul>
          {navTree.map((node) => {
            const hasChildren = node.children && node.children.length > 0;
            const fullPath = `/en/${year}/catalog/${node.slug}`;
            const open = isOpen(node);
            return (
              <li key={node.slug} className="my-1">
                <div className="flex items-start gap-1">
                  {hasChildren ? (
                    <button
                      type="button"
                      onClick={() => toggle(node.slug)}
                      aria-label={open ? 'Collapse' : 'Expand'}
                      className="mt-[5px] text-[#0a4f8c] hover:text-[#072f55]"
                    >
                      <ChevronRight
                        size={12}
                        strokeWidth={3}
                        className={open ? 'rotate-90' : ''}
                      />
                    </button>
                  ) : (
                    <span className="inline-block w-3 mt-[5px]" />
                  )}
                  <Link
                    to={fullPath}
                    className={
                      'text-[14px] font-serif leading-snug hover:underline text-[#0a4f8c] ' +
                      (isActive(fullPath) ? 'font-semibold' : '')
                    }
                  >
                    {node.label}
                  </Link>
                </div>
                {hasChildren && open && (
                  <ul className="ml-5 mt-1 border-l border-gray-200 pl-2">
                    {node.children.map((child) => {
                      const childPath = `/en/${year}/catalog/${node.slug}/${child.slug}`;
                      return (
                        <li key={child.slug} className="my-1 flex items-start gap-1">
                          <span className="inline-block w-3 mt-[5px]" />
                          <Link
                            to={childPath}
                            className={
                              'text-[13.5px] font-serif leading-snug hover:underline text-[#0a4f8c] ' +
                              (isActive(childPath) ? 'font-semibold' : '')
                            }
                          >
                            {child.label}
                          </Link>
                        </li>
                      );
                    })}
                  </ul>
                )}
              </li>
            );
          })}
        </ul>
      </div>

      {/* Catalog Links */}
      <div className="mb-8">
        <h2 className="font-serif text-[20px] text-[#0a4f8c] font-semibold mb-2">Catalog Links</h2>
        <ul className="space-y-1">
          <li>
            <Link
              to={`/en/${year}/catalog`}
              className="text-[14px] font-serif text-[#0a4f8c] hover:underline"
            >
              Catalog Home
            </Link>
          </li>
          <li>
            <Link to="/en" className="text-[14px] font-serif text-[#0a4f8c] hover:underline">
              All Catalogs
            </Link>
          </li>
        </ul>
      </div>

      {/* Share */}
      <div className="mb-8">
        <h2 className="font-serif text-[20px] text-[#0a4f8c] font-semibold mb-2">Share</h2>
        <div className="flex items-center gap-2">
          <button
            type="button"
            aria-label="Share on Facebook"
            className="w-7 h-7 rounded-full bg-[#0a4f8c] text-white text-[12px] font-bold flex items-center justify-center hover:bg-[#072f55]"
          >
            f
          </button>
          <button
            type="button"
            aria-label="Share on X"
            className="w-7 h-7 rounded-full bg-[#0a4f8c] text-white text-[12px] font-bold flex items-center justify-center hover:bg-[#072f55]"
          >
            X
          </button>
          <button
            type="button"
            aria-label="Share by Email"
            className="w-7 h-7 rounded-full bg-[#0a4f8c] text-white text-[14px] font-bold flex items-center justify-center hover:bg-[#072f55]"
          >
            @
          </button>
        </div>
      </div>

      <div className="hidden">
        <select value={version} onChange={(e) => setVersion(e.target.value)}>
          {versions.map((v) => (
            <option key={v}>{v}</option>
          ))}
        </select>
      </div>
    </aside>
  );
};

export default Sidebar;
