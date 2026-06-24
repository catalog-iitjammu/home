import React, { createContext, useContext, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { catalogApi } from '../api/client';
import { NAV_TREE as MOCK_NAV, CATALOG_VERSIONS as MOCK_VERSIONS } from '../data/mock';

const CatalogContext = createContext({
  navTree: MOCK_NAV,
  versions: MOCK_VERSIONS,
  currentVersion: 'Catalog 2024-25',
  loading: true,
  error: null,
});

export const CatalogProvider = ({ children }) => {
  const [navTree, setNavTree] = useState(MOCK_NAV);
  const [versions, setVersions] = useState(MOCK_VERSIONS);
  const [currentVersion, setCurrentVersion] = useState('Catalog 2024-25');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    (async () => {
      try {
        const [tree, meta] = await Promise.all([catalogApi.getNav(), catalogApi.getMeta()]);
        if (!alive) return;
        if (Array.isArray(tree) && tree.length) setNavTree(tree);
        if (meta?.versions?.length) setVersions(meta.versions);
        if (meta?.current) setCurrentVersion(meta.current);
      } catch (e) {
        if (alive) setError(e);
      } finally {
        if (alive) setLoading(false);
      }
    })();
    return () => {
      alive = false;
    };
  }, []);

  return (
    <CatalogContext.Provider value={{ navTree, versions, currentVersion, loading, error }}>
      {children}
    </CatalogContext.Provider>
  );
};

export const useCatalog = () => useContext(CatalogContext);

// Hook to read the current catalog year from the URL (e.g. '2024-25').
// Defaults to '2024-25' if not present.
export const useYear = () => {
  const params = useParams();
  return params.year || '2024-25';
};

// Helper to derive year from a version label like "Catalog 2023-24"
export const parseYearFromVersion = (label) => {
  const m = String(label).match(/(\d{4}-\d{2})/);
  return m ? m[1] : '2024-25';
};
