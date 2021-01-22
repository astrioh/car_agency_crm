import React, { useEffect, useState } from 'react';

import ModalAdd from '../ModalAdd/ModalAdd';
import Pagination from '../Pagination/Pagination';
import ObjectTable from '../ObjectTable/ObjectTable';
import './ClientView.scss';
import axios from 'axios';

const ClientView = ({ className }) => {
  const [clients, setClients] = useState([]);
  const [nextUrl, setNextUrl] = useState(null);
  const [prevUrl, setPrevUrl] = useState(null);

  const headings = [
    'Id',
    'ФИО клиента',
    'Телефон',
    'Дата рождения',
    'Серия паспорта',
    'Номер паспорта',
    'Адрес',
    'Email',
  ];

  const prepareTableData = (clients) => {
    const preparedClients = clients.map((client) => {
      const clientName = `${client.last_name} ${client.first_name} ${client.middle_name}`;

      return [
        client.id,
        clientName,
        client.phone,
        client.birthday,
        client.pass_series,
        client.pass_number,
        client.address,
        client.email,
      ];
    });

    return preparedClients;
  };

  useEffect(() => {
    axios.get('http://localhost:8000/api/clients').then(({ data }) => {
      setClients(prepareTableData(data.results));

      setPrevUrl(data.previous);
      setNextUrl(data.next);
    });
  }, []);

  return (
    <div className={'client-view ' + (className || '')}>
      <div className='client-view__header'>
        <h1 className='title client-view__title'>Клиенты</h1>
        <ModalAdd modalTitle='Добавить клиента' />
      </div>
      <ObjectTable
        data={clients}
        headings={headings}
        className='client-view__table'
      />
      <Pagination prevUrl={prevUrl} nextUrl={nextUrl} />
    </div>
  );
};

export default ClientView;
