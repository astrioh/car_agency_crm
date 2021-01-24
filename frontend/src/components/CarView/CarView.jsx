import React, { useEffect, useState } from 'react';

import CarList from './CarList/CarList';
import SearchInput from '../SearchInput/SearchInput';
import ModalAdd from '../ModalAdd/ModalAdd';
import Pagination from '../Pagination/Pagination';
import FormAddOrEditCar from './FormAddOrEditCar/FormAddOrEditCar';
import './CarView.scss';
import axios from 'axios';

const CarView = ({ className }) => {
  const [cars, setCars] = useState([]);
  const [nextUrl, setNextUrl] = useState(null);
  const [prevUrl, setPrevUrl] = useState(null);

  const getCarsFromBackend = (url) => {
    axios.get(url).then(({ data }) => {
      setCars(data.results);

      setPrevUrl(data.previous);
      setNextUrl(data.next);
    });
  };

  const addCarHandler = (newCar) => {
    setCars([newCar, ...cars]);
  };

  const deleteCarHandler = (carId) => {
    let newCars = cars.filter((car) => car.id !== carId);
    setCars(newCars);

    axios.post(`http://localhost:8000/api/cars/${carId}/delete`);
  };

  const pageChangeHandler = (url) => getCarsFromBackend(url);

  useEffect(() => {
    getCarsFromBackend('http://localhost:8000/api/cars');
  }, []);

  const searchHandler = (searchString) => {
    getCarsFromBackend(`http://localhost:8000/api/cars?search=${searchString}`);
  };

  return (
    <div className={'car-view ' + (className || '')}>
      <div className='car-view__header'>
        <h1 className='title car-view__title'>Машины</h1>
        <ModalAdd modalTitle='Добавить машину'>
          <FormAddOrEditCar />
        </ModalAdd>
      </div>
      <div className='content-pane car-view__content'>
        <SearchInput
          onSearch={searchHandler}
          className='content-view__search'
        />
        <CarList
          cars={cars}
          onDelete={deleteCarHandler}
          className='car-view__list'
        />
        <Pagination
          onPageChange={pageChangeHandler}
          prevUrl={prevUrl}
          nextUrl={nextUrl}
        />
      </div>
    </div>
  );
};

export default CarView;
