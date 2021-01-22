import React from 'react';

import SideMenu from '../../components/SideMenu/SideMenu';
import DealerView from '../../components/DealerView/DealerView';

const DealersPage = () => {
  return (
    <div className='page-container'>
      <SideMenu className='page__sidebar' />
      <DealerView className='page__content' />
    </div>
  );
};

export default DealersPage;
