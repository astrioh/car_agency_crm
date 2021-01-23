import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import './fontawesome';
import CarsPage from './pages/CarsPage/CarsPage';
import ClientsPage from './pages/ClientsPage/ClientsPage';
import DealersPage from './pages/DealersPage/DealersPage';
import EmployeesPage from './pages/EmployeesPage/EmployeesPage';
import ContractsPage from './pages/ContractsPage/ContractsPage';
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

const employeesPageRenderHook = document.getElementById('employees-page');
if (employeesPageRenderHook) {
  ReactDOM.render(
    React.createElement(EmployeesPage, employeesPageRenderHook.dataset),
    employeesPageRenderHook
  );
}

const contractsPageRenderHook = document.getElementById('contracts-page');
if (contractsPageRenderHook) {
  ReactDOM.render(
    React.createElement(ContractsPage, contractsPageRenderHook.dataset),
    contractsPageRenderHook
  );
}
