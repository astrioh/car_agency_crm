import React, { useState } from 'react';

import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './SearchInput.scss';

const SearchInput = ({ onSearch, className }) => {
  const [searchString, setSearchString] = useState('');
  return (
    <div className={'search ' + (className || '')}>
      <input
        type='text'
        onChange={(e) => setSearchString(e.target.value)}
        value={searchString}
        className='search__input'
      />
      <FontAwesomeIcon
        icon={faSearch}
        onClick={() => onSearch(searchString)}
        style={{ cursor: 'pointer' }}
      />
    </div>
  );
};
export default SearchInput;
