import { CoursesContextProvider } from './courses-context';

const AllProviders = ({ children }) => {
  return <CoursesContextProvider>{children}</CoursesContextProvider>;
};

export default AllProviders;
