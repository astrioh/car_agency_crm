import React from 'react';

import { faAngleLeft, faAngleRight } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './Pagination.scss';

const Pagination = ({ prevUrl, nextUrl }) => {
  return (
    <div className='pagination'>
      <a href={prevUrl} className='pagination__button'>
        <FontAwesomeIcon icon={faAngleLeft} color='white' />
      </a>
      <a href={nextUrl} className='pagination__button'>
        <FontAwesomeIcon icon={faAngleRight} color='white' />
      </a>
    </div>
  );
};

export default Pagination;
