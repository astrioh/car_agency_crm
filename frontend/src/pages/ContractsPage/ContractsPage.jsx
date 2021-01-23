import React from 'react';

import SideMenu from '../../components/SideMenu/SideMenu';
import ContractView from '../../components/ContractView/ContractView';

const ContractsPage = () => {
  return (
    <div className='page-container'>
      <SideMenu className='page__sidebar' />
      <ContractView className='page__content' />
    </div>
  );
};

export default ContractsPage;
