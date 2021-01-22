import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import './fontawesome';
import CarsPage from './pages/CarsPage/CarsPage';
import ClientsPage from './pages/ClientsPage/ClientsPage';
import DealersPage from './pages/DealersPage/DealersPage';
import './index.scss';

const carsPageRenderHook = document.getElementById('cars-page');
if (carsPageRenderHook) {
  ReactDOM.render(
    React.createElement(CarsPage, carsPageRenderHook.dataset),
    carsPageRenderHook
  );
}

const clientsPageRenderHook = document.getElementById('clients-page');
if (clientsPageRenderHook) {
  ReactDOM.render(
    React.createElement(ClientsPage, clientsPageRenderHook.dataset),
    clientsPageRenderHook
  );
}

const dealersPageRenderHook = document.getElementById('dealers-page');
if (dealersPageRenderHook) {
  ReactDOM.render(
    React.createElement(DealersPage, dealersPageRenderHook.dataset),
    dealersPageRenderHook
  );
}
