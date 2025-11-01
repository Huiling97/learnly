import { Route, Routes } from 'react-router-dom';

import AllProviders from './app/store';
import Courses from './app/pages/course/courses';

const App = () => (
  <AllProviders>
    <Routes>
      <Route path='courses' element={<Courses />} />
    </Routes>
  </AllProviders>
);

export default App;
