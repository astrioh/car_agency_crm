import React, { useEffect, useState } from 'react';

import CarList from './CarList/CarList';
import SearchInput from '../SearchInput/SearchInput';
import ModalAdd from '../ModalAdd/ModalAdd';
import './CarView.scss';

const CarView = ({ className }) => {
  const [cars, setCars] = useState([]);

  return (
    <div className={'car-view ' + (className || '')}>
      <div className='car-view__header'>
        <h1 className='title car-view__title'>Машины</h1>
        <ModalAdd modalTitle='Добавить машину' />
      </div>
      <div className='content-pane car-view__content'>
        <SearchInput className='content-view__search' />
        <CarList />
      </div>
    </div>
  );
};

export default CarView;
