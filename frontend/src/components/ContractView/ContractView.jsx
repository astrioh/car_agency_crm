import React, { useEffect, useState } from 'react';

import ModalAdd from '../ModalAdd/ModalAdd';
import Pagination from '../Pagination/Pagination';
import ObjectTable from '../ObjectTable/ObjectTable';
import './ContractView.scss';
import axios from 'axios';

const EmployeeView = ({ className }) => {
  const [contracts, setContracts] = useState([]);
  const [nextUrl, setNextUrl] = useState(null);
  const [prevUrl, setPrevUrl] = useState(null);

  const headings = [
    'Id',
    'Сотрудник',
    'Клиент',
    'Машина',
    'Цена',
    'Тип приобретения',
    'Дата',
  ];

  const prepareTableData = (contracts) => {
    const preparedContracts = contracts.map((contract) => {
      const employeeName = `${contract.employee.last_name} ${contract.employee.first_name} ${contract.employee.middle_name}`;
      const clientName = `${contract.client.last_name} ${contract.client.first_name} ${contract.client.middle_name}`;
      const carName = `${contract.car.brand_name} ${contract.car.car_model_name}`;
      return [
        contract.id,
        employeeName,
        clientName,
        carName,
        contract.price,
        contract.payment_type_name,
        contract.date,
      ];
    });

    return preparedContracts;
  };

  const pageChangeHandler = (url) => {
    axios.get(url).then(({ data }) => {
      setContracts(prepareTableData(data.results));

      setPrevUrl(data.previous);
      setNextUrl(data.next);
    });
  };

  useEffect(() => {
    axios.get('http://localhost:8000/api/contracts').then(({ data }) => {
      setContracts(prepareTableData(data.results));

      setPrevUrl(data.previous);
      setNextUrl(data.next);
    });
  }, []);

  return (
    <div className={'contract-view ' + (className || '')}>
      <div className='contract-view__header'>
        <h1 className='title contract-view__title'>Контракты</h1>
        <ModalAdd modalTitle='Добавить сотрудника' />
      </div>
      <ObjectTable
        data={contracts}
        headings={headings}
        className='contract-view__table'
      />
      <Pagination
        prevUrl={prevUrl}
        nextUrl={nextUrl}
        onPageChange={pageChangeHandler}
      />
    </div>
  );
};

export default EmployeeView;
