import React from 'react';

import SideMenu from '../../components/SideMenu/SideMenu';
import CarView from '../../components/CarView/CarView';

const CarsPage = () => {
  return (
    <div className='page-container'>
      <SideMenu className='page__sidebar' />
      <CarView className='page__content' />
    </div>
  );
};

export default CarsPage;
