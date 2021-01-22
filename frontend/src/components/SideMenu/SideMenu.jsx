import React, { useEffect, useState } from 'react';

import axios from 'axios';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Accordion from 'react-bootstrap/Accordion';
import { faSignOutAlt } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './SideMenu.scss';

import ArrowToggle from '../ArrowToggle/ArrowToggle';

const SideMenu = ({ className }) => {
  const [profileName, setProfileName] = useState('...');

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/employees/get_auth_employee')
      .then(({ data }) => {
        setProfileName(data.username);
      });
  });

  return (
    <Navbar bg='dark' variant='dark' className={className || ''}>
      <div className='profile navbar__profile'>
        <div className='profile__name'>{profileName}</div>
        <a className='profile__logout' href='/logout'>
          <FontAwesomeIcon icon={faSignOutAlt} color='white' />
        </a>
      </div>
      <Nav className='flex-column'>
        <Nav.Item className='nav-item__accordion'>
          <Accordion>
            <Nav.Link eventKey='/cars' href='cars'>
              Машины
            </Nav.Link>
            <ArrowToggle eventKey='0' />
            <Accordion.Collapse eventKey='0'>
              <Nav.Link className='nav-link_secondary'>Характеристики</Nav.Link>
            </Accordion.Collapse>
          </Accordion>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link>Сделки</Nav.Link>
          <Nav.Link>Клиенты</Nav.Link>
          <Nav.Link>Дилеры</Nav.Link>
          <Nav.Link>Сотрудники</Nav.Link>
        </Nav.Item>
      </Nav>
    </Navbar>
  );
};

export default SideMenu;
