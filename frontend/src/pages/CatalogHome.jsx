import React from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/Layout';
import { useCatalog, useYear } from '../context/CatalogContext';

const CatalogHome = () => {
  const { navTree } = useCatalog();
  const year = useYear();

  return (
    <Layout>
      <h1 className="font-serif text-[40px] text-[#0a4f8c] font-semibold mb-6">Catalog {year}</h1>
      <div className="w-full overflow-hidden rounded-sm shadow-sm border border-gray-200">
        <div
          className="w-full h-[420px] bg-cover bg-center"
          style={{
            backgroundImage:
              'linear-gradient(rgba(10,79,140,0.20), rgba(10,79,140,0.60)), url(https://images.unsplash.com/photo-1607237138185-eedd9c632b0b?w=1600&q=80)',
          }}
        >
          <div className="h-full flex items-end p-8">
            <div className="text-white">
              <div className="text-[14px] uppercase tracking-[3px] opacity-90">Course Catalog</div>
              <div className="text-[48px] font-serif font-semibold leading-tight">{year}</div>
              <div className="text-[16px] italic mt-1">Indian Institute of Technology Jammu</div>
            </div>
          </div>
        </div>
      </div>

      <div className="mt-8 space-y-4">
        <p className="text-[15px] leading-7 text-gray-800">
          Welcome to the official academic catalog of the Indian Institute of Technology Jammu.
          This catalog contains complete information about our undergraduate, postgraduate, and
          doctoral programs, course listings, credit requirements, academic policies, fees, the
          academic calendar, and faculty for the {year} academic year. Please use the navigation
          on the left to browse by section.
        </p>
        <ul className="list-disc pl-6 text-[15px] leading-7 text-[#0a4f8c]">
          {navTree.map((n) => (
            <li key={n.slug}>
              <Link className="hover:underline" to={`/en/${year}/catalog/${n.slug}`}>
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
