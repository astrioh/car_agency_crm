import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import './fontawesome';
import CarsPage from './pages/CarsPage/CarsPage';
import './index.scss';

const carsPageRenderHook = document.getElementById('cars-page');
if (carsPageRenderHook) {
  ReactDOM.render(
    React.createElement(CarsPage, carsPageRenderHook.dataset),
    carsPageRenderHook
  );
}
