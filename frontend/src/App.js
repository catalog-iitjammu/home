import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { CatalogProvider } from "./context/CatalogContext";

import CatalogHome from "./pages/CatalogHome";
import SectionPage from "./pages/SectionPage";
import DepartmentPage from "./pages/DepartmentPage";
import SubPage from "./pages/SubPage";
import SearchPage from "./pages/SearchPage";
import FacultyPage from "./pages/FacultyPage";
import CalendarPage from "./pages/CalendarPage";
import FeesPage from "./pages/FeesPage";

function App() {
  return (
    <div className="App">
      <CatalogProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Navigate to="/en/2024-25/catalog" replace />} />
            <Route path="/en" element={<Navigate to="/en/2024-25/catalog" replace />} />

            <Route path="/en/:year/catalog" element={<CatalogHome />} />
            <Route path="/en/:year/catalog/search" element={<SearchPage />} />

            {/* Courses, Credits, Hours */}
            <Route
              path="/en/:year/catalog/courses-credits-hours"
              element={<SectionPage slug="courses-credits-hours" />}
            />
            <Route
              path="/en/:year/catalog/courses-credits-hours/:dept"
              element={<DepartmentPage />}
            />

            {/* Faculty */}
            <Route path="/en/:year/catalog/faculty" element={<FacultyPage />} />
            <Route path="/en/:year/catalog/faculty/:group" element={<FacultyPage />} />

            {/* Academic Calendar */}
            <Route path="/en/:year/catalog/academic-calendar" element={<CalendarPage />} />

            {/* Fees */}
            <Route path="/en/:year/catalog/fees-and-financial-aid" element={<FeesPage />} />
            <Route path="/en/:year/catalog/fees-and-financial-aid/:sub" element={<FeesPage />} />

            {/* Info about IIT Jammu */}
            <Route
              path="/en/:year/catalog/information-about-iitjammu"
              element={<SectionPage slug="information-about-iitjammu" />}
            />

            {/* Programs of Study */}
            <Route
              path="/en/:year/catalog/programs-of-study-and-degree-requirements"
              element={<SectionPage slug="programs-of-study-and-degree-requirements" />}
            />

            {/* Academic Policies */}
            <Route
              path="/en/:year/catalog/academic-policies-and-procedures"
              element={<SectionPage slug="academic-policies-and-procedures" />}
            />

            {/* Table of Contents */}
            <Route
              path="/en/:year/catalog/table-of-contents"
              element={<SectionPage slug="table-of-contents" />}
            />

            {/* Generic sub-pages (Programs, Academic Policies, Info) */}
            <Route path="/en/:year/catalog/:section/:sub" element={<SubPage />} />

            <Route path="*" element={<Navigate to="/en/2024-25/catalog" replace />} />
          </Routes>
        </BrowserRouter>
      </CatalogProvider>
    </div>
  );
}

export default App;
