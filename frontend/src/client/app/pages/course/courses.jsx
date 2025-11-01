import { useEffect } from 'react';

import DataTable from '../../components/table/index';
import { useCourses } from '../../store/courses-context';
import { getColumns } from './columns';
import { getAllCoursesData } from '../../service/courses-service';

const Courses = () => {
  const { courses, setCourses } = useCourses();

  useEffect(() => {
    const getAllCourses = async () => {
      try {
        const allCourses = await getAllCoursesData();

        setCourses(allCourses);
      } catch (error) {
        console.log(error);
      }
    };

    getAllCourses();
  }, []);

  return (
    <DataTable columns={getColumns()} data={courses} rowKey={({ id }) => id} />
  );
};

export default Courses;
