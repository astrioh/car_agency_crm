import React, { useEffect, useState } from 'react';

import ModalAdd from '../ModalAdd/ModalAdd';
import Pagination from '../Pagination/Pagination';
import ObjectTable from '../ObjectTable/ObjectTable';
import './EmployeeView.scss';
import axios from 'axios';

const EmployeeView = ({ className }) => {
  const [employees, setEmployees] = useState([]);
  const [nextUrl, setNextUrl] = useState(null);
  const [prevUrl, setPrevUrl] = useState(null);

  const headings = [
    'Id',
    'Логин',
    'Роль',
    'ФИО сотрудника',
    'Пол',
    'Дата рождения',
    'Серия паспорта',
    'Номер паспорта',
    'ИНН',
    'Телефон',
    'Email',
    'Адрес',
  ];

  const prepareTableData = (employees) => {
    const preparedEmployees = employees.map((employee) => {
      const employeeName = `${employee.last_name} ${employee.first_name} ${employee.middle_name}`;
      return [
        employee.id,
        employee.username,
        employee.role_name,
        employeeName,
        employee.sex_full,
        employee.birthday,
        employee.pass_series,
        employee.pass_number,
        employee.inn,
        employee.phone,
        employee.email,
        employee.address,
      ];
    });

    return preparedEmployees;
  };

  useEffect(() => {
    axios.get('http://localhost:8000/api/employees').then(({ data }) => {
      setEmployees(prepareTableData(data.results));

      setPrevUrl(data.previous);
      setNextUrl(data.next);
    });
  }, []);

  return (
    <div className={'employee-view ' + (className || '')}>
      <div className='employee-view__header'>
        <h1 className='title employee-view__title'>Сотрудники</h1>
        <ModalAdd modalTitle='Добавить сотрудника' />
      </div>
      <ObjectTable
        data={employees}
        headings={headings}
        className='employee-view__table'
      />
      <Pagination prevUrl={prevUrl} nextUrl={nextUrl} />
    </div>
  );
};

export default EmployeeView;
