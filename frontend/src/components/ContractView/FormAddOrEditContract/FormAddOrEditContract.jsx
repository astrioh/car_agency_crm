import React, { useState, useEffect } from 'react';

import axios from 'axios';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import FormSelect from '../../FormSelect/FormSelect';

const FormAddOrEditContract = ({ contractId, employee, onSubmit }) => {
  const [contractInfo, setContractInfo] = useState({
    employee: employee.id,
    client: '',
    car: '',
    price: '',
    payment_type: '',
  });

  const [selectOptions, setSelectOptions] = useState({
    client: [],
    car: [],
    payment_type: [],
  });

  useEffect(() => {
    axios.get('http://localhost:8000/api/clients/').then(({ data }) => {
      const preparedClientsArray = data.results.map((item) => ({
        id: item.id,
        name: item.last_name + ' ' + item.first_name + ' ' + item.middle_name,
      }));

      setSelectOptions((state) => ({
        ...state,
        client: preparedClientsArray,
      }));
    });

    axios.get('http://localhost:8000/api/cars/').then(({ data }) => {
      const preparedCarsArray = data.results.map((item) => ({
        id: item.id,
        name: item.brand_name + ' ' + item.car_model_name,
      }));

      setSelectOptions((state) => ({
        ...state,
        car: preparedCarsArray,
      }));
    });

    axios
      .get('http://localhost:8000/api/contracts/payment_types/')
      .then(({ data }) => {
        setSelectOptions((state) => ({
          ...state,
          payment_type: data.results,
        }));
      });
  }, []);

  if (contractId) {
  }

  const addContractHandler = (e) => {
    e.preventDefault();

    axios
      .post('http://localhost:8000/api/contracts/create/', contractInfo, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(({ data }) => {
        const employeeName = `${data.employee.last_name} ${data.employee.first_name} ${data.employee.middle_name}`;
        const clientName = `${data.client.last_name} ${data.client.first_name} ${data.client.middle_name}`;
        const carName = `${data.car.brand_name} ${data.car.car_model_name}`;

        const newContract = [
          data.id,
          employeeName,
          clientName,
          carName,
          data.price,
          data.payment_type_name,
          data.date,
        ];
        onSubmit(newContract);
      });
  };

  const editContractHandler = (e) => {
    e.preventDefault();
    console.log(contractId);
  };

  const onInputChange = (event) => {
    const stateCopy = JSON.parse(JSON.stringify(contractInfo));
    stateCopy[event.target.name] = event.target.value;
    setContractInfo(stateCopy);
    console.log(stateCopy);
  };

  return (
    <Form
      className='form'
      onSubmit={contractId ? editContractHandler : addContractHandler}
    >
      <Form.Group as={Row}>
        <Form.Label column sm={2}>
          Сотрудник
        </Form.Label>
        <Col>
          <Form.Control name='employee' value={employee.username} disabled />
        </Col>
      </Form.Group>
      <Form.Group as={Row}>
        <Form.Label column sm={2}>
          Машина
        </Form.Label>
        <Col>
          <FormSelect
            name='car'
            options={selectOptions.car}
            onChange={onInputChange}
            value={contractInfo.car}
            required
          />
        </Col>
      </Form.Group>
      <Form.Group as={Row}>
        <Form.Label column sm={2}>
          Клиент
        </Form.Label>
        <Col>
          <FormSelect
            name='client'
            options={selectOptions.client}
            onChange={onInputChange}
            value={contractInfo.client}
            required
          />
        </Col>
      </Form.Group>
      <Form.Group as={Row}>
        <Form.Label column sm={2}>
          Тип приобретения
        </Form.Label>
        <Col>
          <FormSelect
            name='payment_type'
            options={selectOptions.payment_type}
            onChange={onInputChange}
            value={contractInfo.payment_type}
            required
          />
        </Col>
      </Form.Group>
      <Form.Group as={Row}>
        <Form.Label column sm={2}>
          Цена
        </Form.Label>
        <Col>
          <Form.Control
            name='price'
            onChange={onInputChange}
            value={contractInfo.price}
            required
          />
        </Col>
      </Form.Group>
      <Button variant='primary' type='submit'>
        Сохранить
      </Button>
    </Form>
  );
};

export default FormAddOrEditContract;
