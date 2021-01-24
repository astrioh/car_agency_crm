import React from 'react';

import { faAngleLeft, faAngleRight } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './Pagination.scss';

const Pagination = ({ prevUrl, nextUrl, onPageChange }) => {
  return (
    <div className='pagination'>
      {prevUrl && (
        <div
          onClick={() => onPageChange(prevUrl)}
          className='pagination__button'
        >
          <FontAwesomeIcon icon={faAngleLeft} color='white' />
        </div>
      )}
      {nextUrl && (
        <div
          onClick={() => onPageChange(nextUrl)}
          className='pagination__button'
        >
          <FontAwesomeIcon icon={faAngleRight} color='white' />
        </div>
      )}
    </div>
  );
};

export default Pagination;
