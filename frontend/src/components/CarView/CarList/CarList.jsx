import React from 'react';

import Car from './Car/Car';
import './CarList.scss';

const CarList = ({ cars, className, onDelete }) => {
  return (
    <div className={'car-list ' + (className || '')}>
      {cars.map((car) => (
        <Car
          onDelete={onDelete}
          key={car.id}
          car={car}
          className='car-list__car'
        />
      ))}
    </div>
  );
};

export default CarList;
