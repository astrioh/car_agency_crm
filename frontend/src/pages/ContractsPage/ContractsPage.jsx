import React, { useState, useEffect } from 'react';

import SideMenu from '../../components/SideMenu/SideMenu';
import ContractView from '../../components/ContractView/ContractView';
import axios from 'axios';

const ContractsPage = () => {
  const [employeeRole, setEmployeeRole] = useState(-1);
  useEffect(() => {
    axios
      .get('http://localhost:8000/api/employees/get_auth_employee')
      .then(({ data }) => {
        setEmployeeRole(data.role);
      });
  });

  return (
    <div className='page-container'>
      <SideMenu className='page__sidebar' />
      <ContractView className='page__content' employeeRole={employeeRole} />
    </div>
  );
};

export default ContractsPage;
