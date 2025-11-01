import axios from 'axios';

import URLConstants from '../../../shared/url-constants';

const getAllCoursesData = async () => {
  try {
    const response = await axios.get(`${URLConstants.COURSES_PATH}/all`);

    if (response) {
      const { data } = response;

      return data;
    }
  } catch (error) {
    throw error;
  }
};

export { getAllCoursesData };
