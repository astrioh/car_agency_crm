import React from 'react';

import Car from './Car/Car';
import './CarList.scss';

const CarList = ({ cars, className }) => {
  return (
    <div className={'car-list ' + (className || '')}>
      {cars.map((car) => (
        <Car key={car.id} car={car} className='car-list__car' />
      ))}
    </div>
  );
};

export default CarList;
