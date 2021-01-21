import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import CarsPage from './pages/CarsPage/CarsPage';

const carsPageRenderHook = document.getElementById('cars-page');
if (carsPageRenderHook) {
  ReactDOM.render(
    React.createElement(CarsPage, carsPageRenderHook.dataset),
    carsPageRenderHook
  );
}
