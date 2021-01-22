import React from 'react';

import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './SearchInput.scss';

const SearchInput = ({ onSearch, className }) => {
  return (
    <div className={'search ' + (className || '')}>
      <input type='text' name='' className='search__input' />
      <FontAwesomeIcon
        icon={faSearch}
        onClick={onSearch}
        style={{ cursor: 'pointer' }}
      />
    </div>
  );
};
export default SearchInput;
