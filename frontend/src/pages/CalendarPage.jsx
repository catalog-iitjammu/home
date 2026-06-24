import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import { catalogApi } from '../api/client';

const CalendarPage = () => {
  const [terms, setTerms] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let alive = true;
    catalogApi
      .getCalendar()
      .then((d) => alive && setTerms(d))
      .catch(() => alive && setTerms([]))
      .finally(() => alive && setLoading(false));
    return () => {
      alive = false;
    };
  }, []);

  return (
    <Layout>
      <h1 className="font-serif text-[34px] text-[#0a4f8c] font-semibold mb-4">Academic Calendar</h1>
      <p className="text-[15px] leading-7 text-gray-800 mb-6">
        The academic calendar lists key dates for registration, instruction, examinations, and
        breaks. Dates are tentative and subject to revision; please refer to notifications from
        the Academic Section for the most current information.
      </p>
      {loading && <p className="text-gray-500">Loading calendar…</p>}
      {terms.map((sem) => (
        <div key={sem.term} className="mb-8">
          <h2 className="font-serif text-[22px] text-[#0a4f8c] font-semibold mb-2">{sem.term}</h2>
          <table className="catalog-table w-full">
            <thead>
              <tr>
                <th style={{ width: '60%' }}>Event</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {sem.rows.map((r) => (
                <tr key={r.event}>
                  <td>{r.event}</td>
                  <td className="text-gray-800">{r.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}
    </Layout>
  );
};

export default CalendarPage;
