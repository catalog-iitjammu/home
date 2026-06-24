import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import CatalogHome from "./pages/CatalogHome";
import SectionPage from "./pages/SectionPage";
import DepartmentPage from "./pages/DepartmentPage";
import SubPage from "./pages/SubPage";
import SearchPage from "./pages/SearchPage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate to="/en/2024-25/catalog" replace />} />
          <Route path="/en" element={<Navigate to="/en/2024-25/catalog" replace />} />
          <Route path="/en/2024-25/catalog" element={<CatalogHome />} />
          <Route path="/en/2024-25/catalog/search" element={<SearchPage />} />
          <Route
            path="/en/2024-25/catalog/courses-credits-hours/:dept"
            element={<DepartmentPage />}
          />
          <Route
            path="/en/2024-25/catalog/:section/:sub"
            element={<SubPage />}
          />
          <Route
            path="/en/2024-25/catalog/information-about-gcet"
            element={<SectionPage slug="information-about-gcet" />}
          />
          <Route
            path="/en/2024-25/catalog/programs-of-study-and-degree-requirements"
            element={<SectionPage slug="programs-of-study-and-degree-requirements" />}
          />
          <Route
            path="/en/2024-25/catalog/courses-credits-hours"
            element={<SectionPage slug="courses-credits-hours" />}
          />
          <Route
            path="/en/2024-25/catalog/academic-policies-and-procedures"
            element={<SectionPage slug="academic-policies-and-procedures" />}
          />
          <Route
            path="/en/2024-25/catalog/table-of-contents"
            element={<SectionPage slug="table-of-contents" />}
          />
          <Route path="*" element={<Navigate to="/en/2024-25/catalog" replace />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
