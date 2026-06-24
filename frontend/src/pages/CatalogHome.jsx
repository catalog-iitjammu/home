import React from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { NAV_TREE } from '../data/mock';

const CatalogHome = () => {
  return (
    <Layout>
      <h1 className="font-serif text-[40px] text-[#0a4f8c] font-semibold mb-6">Catalog 2024-25</h1>
      <div className="w-full overflow-hidden rounded-sm shadow-sm border border-gray-200">
        <div
          className="w-full h-[420px] bg-cover bg-center"
          style={{
            backgroundImage:
              'linear-gradient(rgba(10,79,140,0.15), rgba(10,79,140,0.55)), url(https://images.unsplash.com/photo-1562774053-701939374585?w=1600&q=80)',
          }}
        >
          <div className="h-full flex items-end p-8">
            <div className="text-white">
              <div className="text-[14px] uppercase tracking-[3px] opacity-90">Course Catalog</div>
              <div className="text-[48px] font-serif font-semibold leading-tight">2024 – 25</div>
              <div className="text-[16px] italic mt-1">GCET College of Engineering</div>
            </div>
          </div>
        </div>
      </div>

      <div className="mt-8 space-y-4">
        <p className="text-[15px] leading-7 text-gray-800">
          Welcome to the official academic catalog of GCET College of Engineering. This catalog
          contains complete information about our undergraduate and graduate programs, course
          listings, credit requirements, academic policies, and procedures for the 2024–25 academic
          year. Please use the navigation on the left to browse by section.
        </p>
        <ul className="list-disc pl-6 text-[15px] leading-7 text-[#0a4f8c]">
          {NAV_TREE.map((n) => (
            <li key={n.slug}>
              <Link className="hover:underline" to={`/en/2024-25/catalog/${n.slug}`}>
                {n.label}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </Layout>
  );
};

export default CatalogHome;
