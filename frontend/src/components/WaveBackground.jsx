import React from 'react';

// Soft wavy decorative background, mimicking the Olin SmartCatalog skin
const WaveBackground = () => {
  return (
    <div aria-hidden="true" className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
      {/* diagonal stripes at top */}
      <div
        className="absolute top-0 left-0 right-0 h-[140px] opacity-[0.18]"
        style={{
          backgroundImage:
            'repeating-linear-gradient(135deg, #b9c6d2 0 1px, transparent 1px 7px)',
        }}
      />
      {/* wavy lines */}
      <svg className="absolute -left-20 top-40 opacity-40" width="600" height="500" viewBox="0 0 600 500" fill="none">
        {Array.from({ length: 14 }).map((_, i) => (
          <path
            key={i}
            d={`M0 ${40 + i * 30} C 120 ${10 + i * 30}, 240 ${80 + i * 30}, 360 ${40 + i * 30} S 600 ${10 + i * 30}, 720 ${50 + i * 30}`}
            stroke="#c9d3dc"
            strokeWidth="1"
            fill="none"
          />
        ))}
      </svg>
      <svg className="absolute -right-20 top-80 opacity-40" width="600" height="500" viewBox="0 0 600 500" fill="none">
        {Array.from({ length: 14 }).map((_, i) => (
          <path
            key={i}
            d={`M0 ${40 + i * 30} C 120 ${80 + i * 30}, 240 ${10 + i * 30}, 360 ${60 + i * 30} S 600 ${100 + i * 30}, 720 ${40 + i * 30}`}
            stroke="#c9d3dc"
            strokeWidth="1"
            fill="none"
          />
        ))}
      </svg>
      <svg className="absolute -left-10 bottom-0 opacity-40" width="700" height="260" viewBox="0 0 700 260" fill="none">
        {Array.from({ length: 9 }).map((_, i) => (
          <path
            key={i}
            d={`M0 ${30 + i * 26} C 140 ${0 + i * 26}, 280 ${80 + i * 26}, 420 ${20 + i * 26} S 700 ${0 + i * 26}, 840 ${50 + i * 26}`}
            stroke="#c9d3dc"
            strokeWidth="1"
            fill="none"
          />
        ))}
      </svg>
      <svg className="absolute right-0 bottom-10 opacity-40" width="700" height="260" viewBox="0 0 700 260" fill="none">
        {Array.from({ length: 9 }).map((_, i) => (
          <path
            key={i}
            d={`M0 ${30 + i * 26} C 140 ${70 + i * 26}, 280 ${0 + i * 26}, 420 ${50 + i * 26} S 700 ${80 + i * 26}, 840 ${10 + i * 26}`}
            stroke="#c9d3dc"
            strokeWidth="1"
            fill="none"
          />
        ))}
      </svg>
    </div>
  );
};

export default WaveBackground;
