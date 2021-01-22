import React, { useEffect, useState } from 'react';

import ModalAdd from '../ModalAdd/ModalAdd';
import Pagination from '../Pagination/Pagination';
import ObjectTable from '../ObjectTable/ObjectTable';
import './DealerView.scss';
import axios from 'axios';

const DealerView = ({ className }) => {
  const [dealers, setDealers] = useState([]);
  const [nextUrl, setNextUrl] = useState(null);
  const [prevUrl, setPrevUrl] = useState(null);

  const headings = [
    'Id',
    'Дилер',
    'Тип',
    'Контактное лицо',
    'Телефон',
    'Адрес',
    'Email',
  ];

  const prepareTableData = (dealers) => {
    const preparedDealers = dealers.map((dealer) => {
      return [
        dealer.id,
        dealer.name,
        dealer.dealer_type_name,
        dealer.contact,
        dealer.phone,
        dealer.address,
        dealer.email,
      ];
    });

    return preparedDealers;
  };

  useEffect(() => {
    axios.get('http://localhost:8000/api/dealers').then(({ data }) => {
      setDealers(prepareTableData(data.results));

      setPrevUrl(data.previous);
      setNextUrl(data.next);
    });
  }, []);

  return (
    <div className={'dealer-view ' + (className || '')}>
      <div className='dealer-view__header'>
        <h1 className='title dealer-view__title'>Дилеры</h1>
        <ModalAdd modalTitle='Добавить дилера' />
      </div>
      <ObjectTable
        data={dealers}
        headings={headings}
        className='dealer-view__table'
      />
      <Pagination prevUrl={prevUrl} nextUrl={nextUrl} />
    </div>
  );
};

export default DealerView;
