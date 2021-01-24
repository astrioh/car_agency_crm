import { faTrash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import React from 'react';

import './Car.scss';

const Car = ({ car, className, onDelete }) => {
  const imageLink = car.car_photos[0]
    ? 'http://localhost:8000' + car.car_photos[0].image
    : 'data:image/png;base64,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';

  return (
    <div className={'car ' + (className || '')}>
      <div className='car__image'>
        <img src={imageLink} alt={car.model_name} />
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
      <FontAwesomeIcon
        icon={faTrash}
        color='red'
        onClick={() => onDelete(car.id)}
      />
    </div>
  );
};

export default Car;
