import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';
import TopBar from './TopBar';
import WaveBackground from './WaveBackground';

const Layout = ({ children }) => {
  return (
    <div className="min-h-screen text-gray-800 font-serif relative">
      <WaveBackground />
      <Header />
      <main className="max-w-[1200px] mx-auto px-6 py-8">
        <div className="flex flex-col lg:flex-row gap-8">
          <Sidebar />
          <div className="flex-1 min-w-0">
            <TopBar />
            <div className="prose-catalog">{children}</div>
          </div>
        </div>
      </main>
      <footer className="max-w-[1200px] mx-auto px-6 py-10 text-[12px] text-gray-500 font-serif">
        <div className="border-t border-gray-200 pt-4 flex flex-col md:flex-row justify-between gap-2">
          <div>© {new Date().getFullYear()} Indian Institute of Technology Jammu. All rights reserved.</div>
          <div>Powered by IIT Jammu SmartCatalog</div>
        </div>
      </footer>
    </div>
  );
};

export default Layout;
