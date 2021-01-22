import React from 'react';

import './Car.scss';

const Car = ({ car, className }) => {
  return (
    <div className={'car ' + (className || '')}>
      <div className='car__image'>
        <img src={car.car_photos[0]} alt={car.model_name} />
      </div>
      <div className='car__info'>
        <div className='car__name'>
          {car.brand_name + ' ' + car.car_model_name}
        </div>
        <div className='car__characteristics'>
          {car.dealer_name && (
            <div className='car__characteristic'>
              <b>Дилер</b>: {car.dealer_name}
            </div>
          )}
          {car.car_type_name && (
            <div className='car__characteristic'>
              <b>Тип автомобиля</b>: {car.car_type_name}
            </div>
          )}
          {car.release_year && (
            <div className='car__characteristic'>
              <b>Год выпуска</b>: {car.release_year}
            </div>
          )}

          {car.price && (
            <div className='car__characteristic'>
              <b>Цена</b>: {car.price}
            </div>
          )}
          {car.color && (
            <div className='car__characteristic'>
              <b>Цвет</b>: {car.color}
            </div>
          )}
          {car.drivetrain_type_name && (
            <div className='car__characteristic'>
              <b>Тип привода</b>: {car.drivetrain_type_name}
            </div>
          )}

          {car.engine_type_name && car.engine_volume && car.engine_power && (
            <div className='car__characteristic'>
              <b>Двигатель</b>:{' '}
              {`${car.engine_volume}л/${car.engine_power}/${car.engine_type_name}`}
            </div>
          )}
          {car.body_type_name && (
            <div className='car__characteristic'>
              <b>Тип кузова</b>: {car.body_type_name}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Car;
