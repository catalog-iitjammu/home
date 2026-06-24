import React from 'react';
import { Link } from 'react-router-dom';

const Logo = () => (
  <Link to="/en/2024-25/catalog" className="flex items-center gap-3 group" aria-label="GCET College of Engineering Home">
    <svg width="58" height="58" viewBox="0 0 80 80" className="shrink-0">
      <circle cx="40" cy="40" r="38" fill="#0a4f8c" />
      <circle cx="40" cy="40" r="30" fill="none" stroke="#ffffff" strokeWidth="2" />
      <text x="40" y="36" textAnchor="middle" fontSize="18" fontWeight="700" fill="#ffffff" fontFamily="Georgia, serif">GCET</text>
      <text x="40" y="54" textAnchor="middle" fontSize="8" fill="#bcd9f1" letterSpacing="2">EST.1984</text>
    </svg>
    <div className="leading-tight">
      <div className="text-[#0a4f8c] font-serif text-[26px] font-semibold tracking-tight">GCET College</div>
      <div className="text-[#0a4f8c] font-serif text-[26px] font-semibold tracking-tight -mt-1">of Engineering</div>
    </div>
  </Link>
);

const Header = () => {
  return (
    <header className="relative w-full bg-white border-b border-gray-200">
      <div className="max-w-[1200px] mx-auto px-6 py-6 flex items-center justify-between">
        <Logo />
        <a
          href="https://www.gcet.ac.in"
          target="_blank"
          rel="noopener noreferrer"
          className="hidden md:inline-flex items-center text-[#0a4f8c] italic font-serif text-[18px] hover:text-[#072f55] hover:underline transition-colors"
        >
          Leave the catalog and go to GCET.edu
        </a>
      </div>
    </header>
  );
};

export default Header;
