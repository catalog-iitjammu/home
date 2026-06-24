import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API_BASE = `${BACKEND_URL}/api`;

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
  headers: { 'Content-Type': 'application/json' },
});

export const catalogApi = {
  getMeta: () => api.get('/meta').then((r) => r.data),
  getNav: () => api.get('/nav').then((r) => r.data.tree),
  listDepartments: () => api.get('/departments').then((r) => r.data),
  getDepartment: (slug) => api.get(`/departments/${slug}`).then((r) => r.data),
  listFaculty: () => api.get('/faculty').then((r) => r.data),
  getFacultyGroup: (slug) => api.get(`/faculty/${slug}`).then((r) => r.data),
  getCalendar: () => api.get('/calendar').then((r) => r.data),
  listFees: () => api.get('/fees').then((r) => r.data),
  getFee: (slug) => api.get(`/fees/${slug}`).then((r) => r.data),
  listInfoPages: () => api.get('/info-pages').then((r) => r.data),
  getInfoPage: (slug) => api.get(`/info-pages/${slug}`).then((r) => r.data),
  search: (q, scope = 'Entire Catalog') =>
    api.get('/search', { params: { q, scope } }).then((r) => r.data),
  // Mutations
  addCourse: (slug, course) =>
    api.post(`/departments/${slug}/courses`, course).then((r) => r.data),
  removeCourse: (slug, code) =>
    api.delete(`/departments/${slug}/courses/${code}`).then((r) => r.data),
  reseed: (force = false) =>
    api.post('/seed', null, { params: { force } }).then((r) => r.data),
};

export default api;
