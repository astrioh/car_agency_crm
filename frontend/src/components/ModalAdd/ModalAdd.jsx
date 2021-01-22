import React, { useState } from 'react';

import Modal from 'react-bootstrap/Modal';
import './ModalAdd.scss';

const ModalAdd = ({ form, modalTitle }) => {
  const [show, setShow] = useState(false);

  const handleShow = () => setShow(true);
  const handleClose = () => setShow(false);
  return (
    <>
      <button className='add-btn' onClick={handleShow}>
        +
      </button>
      <Modal show={show} onHide={handleClose} size='lg'>
        <Modal.Header closeButton>
          <Modal.Title>{modalTitle || 'Добавить'}</Modal.Title>
        </Modal.Header>
        <Modal.Body>{form}</Modal.Body>
      </Modal>
    </>
  );
};

export default ModalAdd;
