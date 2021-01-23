import React, { useState } from 'react';

import Modal from 'react-bootstrap/Modal';
import './ModalAdd.scss';

const ModalAdd = ({ form, modalTitle, children, size }) => {
  const [show, setShow] = useState(false);

  const handleShow = () => setShow(true);
  const handleClose = () => setShow(false);
  return (
    <>
      <button className='add-btn' onClick={handleShow}>
        +
      </button>
      <Modal show={show} onHide={handleClose} size={size || 'xl'}>
        <Modal.Header closeButton>
          <Modal.Title>{modalTitle || 'Добавить'}</Modal.Title>
        </Modal.Header>
        <Modal.Body>{children}</Modal.Body>
      </Modal>
    </>
  );
};

export default ModalAdd;
