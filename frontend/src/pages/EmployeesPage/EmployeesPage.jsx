import React from 'react';

import SideMenu from '../../components/SideMenu/SideMenu';
import EmployeeView from '../../components/EmployeeView/EmployeeView';

const EmployeesPage = () => {
  return (
    <div className='page-container'>
      <SideMenu className='page__sidebar' />
      <EmployeeView className='page__content' />
    </div>
  );
};

export default EmployeesPage;
