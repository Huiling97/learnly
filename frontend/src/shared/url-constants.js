const URLConstants = {};

const isDev =
  typeof window !== 'undefined' && window.location.hostname === 'localhost';
URLConstants.BASE = isDev ? 'http://localhost:8000' : '';

URLConstants.COURSES_PATH = `${URLConstants.BASE}/api/v1/courses`;

export default URLConstants;
