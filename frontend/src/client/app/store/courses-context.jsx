import { createContext, useContext, useReducer } from 'react';

const CoursesContext = createContext();

const useCourses = () => useContext(CoursesContext);

const coursesReducer = (state, action) => {
  switch (action.type) {
    case 'SET':
      return action.payload;
    default:
      return state;
  }
};

const CoursesContextProvider = ({ children }) => {
  const [coursesState, dispatch] = useReducer(coursesReducer, []);

  const getSelectedCourse = (id) =>
    coursesState.find(({ course_id }) => course_id === id);

  const setCourses = (courses) => {
    dispatch({ type: 'SET', payload: courses });
  };

  const value = {
    courses: coursesState,
    getSelectedCourse,
    setCourses,
  };

  return (
    <CoursesContext.Provider value={value}>{children}</CoursesContext.Provider>
  );
};

export { CoursesContextProvider, useCourses };
