import React, { useEffect, useState } from 'react';

import CarList from './CarList/CarList';
import SearchInput from '../SearchInput/SearchInput';
import ModalAdd from '../ModalAdd/ModalAdd';
import Pagination from '../Pagination/Pagination';
import './CarView.scss';
import axios from 'axios';

const CarView = ({ className }) => {
  const [cars, setCars] = useState([]);
  const [nextUrl, setNextUrl] = useState('#');
  const [prevUrl, setPrevUrl] = useState('#');

  useEffect(() => {
    axios.get('http://localhost:8000/api/cars').then(({ data }) => {
      setCars(data.results);

      let gotPrevUrl = data.previous === 'null' ? '#' : data.previous;
      let gotNextUrl = data.next === 'null' ? '#' : data.next;

      setPrevUrl(gotPrevUrl);
      setNextUrl(gotNextUrl);
    });
  }, []);

  const searchHandler = (searchString) => {
    axios
      .get(`http://localhost:8000/api/cars?search=${searchString}`)
      .then(({ data }) => {
        setCars(data.results);

        let gotPrevUrl = data.previous === 'null' ? '#' : data.previous;
        let gotNextUrl = data.next === 'null' ? '#' : data.next;

        setPrevUrl(gotPrevUrl);
        setNextUrl(gotNextUrl);
      });
  };

  return (
    <div className={'car-view ' + (className || '')}>
      <div className='car-view__header'>
        <h1 className='title car-view__title'>Машины</h1>
        <ModalAdd modalTitle='Добавить машину' />
      </div>
      <div className='content-pane car-view__content'>
        <SearchInput
          onSearch={searchHandler}
          className='content-view__search'
        />
        <CarList cars={cars} className='car-view__list' />
        <Pagination prevUrl={prevUrl} nextUrl={nextUrl} />
      </div>
    </div>
  );
};

export default CarView;
