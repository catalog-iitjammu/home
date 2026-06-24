import React from 'react';
import { Link } from 'react-router-dom';
import { useYear } from '../context/CatalogContext';

const LOGO_URL =
  'https://customer-assets.emergentagent.com/job_course-hours/artifacts/1vookqye_iit-jammu-logo-new_0_0.png';

const Header = () => {
  const year = useYear();
  return (
    <header className="relative w-full bg-white border-b border-gray-200">
      <div className="max-w-[1200px] mx-auto px-6 py-5 flex items-center justify-between gap-6">
        <Link to={`/en/${year}/catalog`} className="flex items-center gap-4" aria-label="IIT Jammu Home">
          <img
            src={LOGO_URL}
            alt="Indian Institute of Technology Jammu"
            className="h-[78px] w-[78px] object-cover rounded-sm shadow-sm"
            style={{ objectPosition: 'left center' }}
          />
          <div className="leading-tight">
            <div className="text-[#0a4f8c] font-serif text-[26px] font-bold tracking-tight">
              INDIAN INSTITUTE OF
            </div>
            <div className="text-[#0a4f8c] font-serif text-[26px] font-bold tracking-tight -mt-1">
              TECHNOLOGY JAMMU
            </div>
            <div className="text-[12px] italic text-gray-500 font-serif mt-[2px]">
              भारतीय प्रौद्योगिकी संस्थान जम्मू
            </div>
          </div>
        </Link>
        <a
          href="https://www.iitjammu.ac.in"
          target="_blank"
          rel="noopener noreferrer"
          className="hidden md:inline-flex items-center text-[#0a4f8c] italic font-serif text-[17px] hover:text-[#072f55] hover:underline transition-colors text-right"
        >
          Leave the catalog and go to IITJammu.ac.in
        </a>
      </div>
    </header>
  );
};

export default Header;
