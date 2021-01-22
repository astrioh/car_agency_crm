import React from 'react';

import SideMenu from '../../components/SideMenu/SideMenu';
import ClientView from '../../components/ClientView/ClientView';

const ClientsPage = () => {
  return (
    <div className='page-container'>
      <SideMenu className='page__sidebar' />
      <ClientView className='page__content' />
    </div>
  );
};

export default ClientsPage;
