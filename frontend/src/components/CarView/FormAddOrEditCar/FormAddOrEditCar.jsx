import React, { useState, useEffect } from 'react';

import axios from 'axios';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import FormSelect from '../../FormSelect/FormSelect';
import ModalAdd from '../../ModalAdd/ModalAdd';

const FormAddOrEditCar = ({ carId, onSubmit }) => {
  const [carInfo, setCarInfo] = useState({
    brand: '',
    car_model: '',
    car_type: '',
    dealer: '',
    pts: '',
    vin: '',
    color: '',
    mileage: '',
    release_year: '',
    price: '',
    wheel: '',
    engine_type: '',
    engine_volume: '',
    engine_power: '',
    body_type: '',
    drivetrain_type: '',
    transmission_type: '',
    defects: [],
    car_photos: [],
  });

  const [selectOptions, setSelectOptions] = useState({
    brand: [],
    car_model: [],
    car_type: [],
    engine_type: [],
    body_type: [],
    drivetrain_type: [],
    transmission_type: [],
    defect_type: [],
  });

  const [dealers, setDealers] = useState([]);

  // TODO: вынести в отдельный компонент
  const [defect, setDefect] = useState({
    defect_type: '',
    name: '',
    text: '',
    image: '',
  });

  useEffect(() => {
    axios.get('http://localhost:8000/api/cars/misc').then(({ data }) => {
      setSelectOptions(data);
    });
    axios.get('http://localhost:8000/api/dealers/').then(({ data }) => {
      setDealers(data.results);
    });
  }, []);

  if (carId) {
  }

  const addCarHandler = (e) => {
    e.preventDefault();
    let formData = new FormData();
    for (let key in carInfo) {
      if (key === 'defects') {
        carInfo[key].forEach((value) => {
          formData.append(`${key}[]`, JSON.stringify(value));
        });
      } else if (key === 'car_photos') {
        carInfo[key].forEach((value) => {
          formData.append(`${key}[]`, value);
        });
      } else {
        formData.append(key, carInfo[key]);
      }
    }
    axios
      .post('http://localhost:8000/api/cars/create/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(({ data }) => onSubmit(data));
  };

  const editCarHandler = (e) => {
    e.preventDefault();
    console.log(carId);
  };

  const onInputChange = (event) => {
    const stateCopy = JSON.parse(JSON.stringify(carInfo));
    stateCopy[event.target.name] = event.target.value;
    setCarInfo(stateCopy);
    console.log(stateCopy);
  };

  const onDefectInputChange = (event) => {
    const stateCopy = JSON.parse(JSON.stringify(defect));
    stateCopy[event.target.name] = event.target.value;
    setDefect(stateCopy);

    console.log(defect);
  };

  const onDefectImageChange = (event) => {
    const image = event.target.files[0];
    const stateCopy = JSON.parse(JSON.stringify(defect));
    stateCopy.image = image;
    setDefect(stateCopy);
    console.log(defect);
  };

  const addDefect = (newDefect) => {
    setCarInfo({ ...carInfo, defects: [...carInfo.defects, newDefect] });
  };

  const onCarPhotoChange = (event) => {
    const image = event.target.files[0];
    const stateCopy = JSON.parse(JSON.stringify(carInfo));
    stateCopy.car_photos = [...stateCopy.car_photos, image];
    setCarInfo(stateCopy);
  };

  return (
    <Form className='form' onSubmit={carId ? editCarHandler : addCarHandler}>
      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Бренд</Form.Label>
          <FormSelect
            options={selectOptions.brand}
            onChange={onInputChange}
            value={carInfo.brand}
            required
            name='brand'
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Модель</Form.Label>
          <FormSelect
            options={selectOptions.car_model}
            onChange={onInputChange}
            value={carInfo.car_model}
            required
            name='car_model'
          />
        </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Дилер</Form.Label>
          <FormSelect
            options={dealers}
            onChange={onInputChange}
            value={carInfo.dealer}
            required
            name='dealer'
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>ПТС</Form.Label>
          <Form.Control
            name='pts'
            onChange={onInputChange}
            value={carInfo.pts}
            required
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>VIN</Form.Label>
          <Form.Control
            name='vin'
            onChange={onInputChange}
            value={carInfo.vin}
            required
          />
        </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Тип машины</Form.Label>
          <FormSelect
            options={selectOptions.car_type}
            onChange={onInputChange}
            value={carInfo.car_type}
            required
            name='car_type'
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Цвет</Form.Label>
          <Form.Control
            name='color'
            onChange={onInputChange}
            value={carInfo.color}
            required
          />
        </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Год выпуска</Form.Label>
          <Form.Control
            name='release_year'
            onChange={onInputChange}
            value={carInfo.release_year}
            required
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Цена</Form.Label>
          <Form.Control
            name='price'
            onChange={onInputChange}
            value={carInfo.price}
            required
          />
        </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Пробег</Form.Label>
          <Form.Control
            name='mileage'
            onChange={onInputChange}
            value={carInfo.mileage}
            required
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Руль</Form.Label>
          <Form.Control
            name='wheel'
            onChange={onInputChange}
            value={carInfo.wheel}
            as='select'
            required
          >
            <option value='Левый'>Левый</option>
            <option value='Правый'>Правый</option>
          </Form.Control>
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Тип привода</Form.Label>
          <FormSelect
            options={selectOptions.drivetrain_type}
            onChange={onInputChange}
            value={carInfo.drivetrain_type}
            required
            name='drivetrain_type'
          />
        </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Тип кузова</Form.Label>
          <FormSelect
            options={selectOptions.body_type}
            onChange={onInputChange}
            value={carInfo.body_type}
            required
            name='body_type'
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Тип подвески</Form.Label>
          <FormSelect
            options={selectOptions.transmission_type}
            onChange={onInputChange}
            value={carInfo.transmission_type}
            required
            name='transmission_type'
          />
        </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group as={Col}>
          <Form.Label>Тип двигателя</Form.Label>
          <FormSelect
            options={selectOptions.engine_type}
            onChange={onInputChange}
            value={carInfo.engine_type}
            required
            name='engine_type'
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Объем двигателя</Form.Label>
          <Form.Control
            name='engine_volume'
            onChange={onInputChange}
            value={carInfo.engine_volume}
            required
          />
        </Form.Group>
        <Form.Group as={Col}>
          <Form.Label>Мощность двигателя</Form.Label>
          <Form.Control
            name='engine_power'
            onChange={onInputChange}
            value={carInfo.engine_power}
            required
          />
        </Form.Group>
      </Form.Row>

      <Form.Label className='d-block'>Дефекты:</Form.Label>
      <Form.Row>
        {carInfo.defects.length < 5 && (
          <ModalAdd size='lg'>
            <Form className='form' onSubmit={(e) => e.preventDefault()}>
              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                  Тип дефекта
                </Form.Label>
                <Col>
                  <FormSelect
                    options={selectOptions.defect_type}
                    onChange={onDefectInputChange}
                    value={defect.defect_type}
                    required
                    name='defect_type'
                  />
                </Col>
              </Form.Group>
              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                  Имя дефекта
                </Form.Label>
                <Col>
                  <Form.Control
                    name='name'
                    onChange={onDefectInputChange}
                    value={defect.name}
                    required
                  />
                </Col>
              </Form.Group>
              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                  Описание
                </Form.Label>
                <Col>
                  <Form.Control
                    name='text'
                    onChange={onDefectInputChange}
                    value={defect.text}
                    required
                  />
                </Col>
              </Form.Group>
              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                  Фото
                </Form.Label>
                <Col>
                  <Form.File
                    name='image'
                    onChange={onDefectImageChange}
                    required
                  />
                </Col>
              </Form.Group>
              <Button
                onClick={(e) => {
                  e.preventDefault();
                  addDefect(JSON.parse(JSON.stringify(defect)));
                }}
                variant='primary'
              >
                Добавить дефект
              </Button>
            </Form>
          </ModalAdd>
        )}
        {carInfo.defects.map((defect, i) => (
          <span key={i}>{defect.name}</span>
        ))}
      </Form.Row>
      <Form.Label>Фото:</Form.Label>
      <Form.Row>
        <Form.File
          name='car_photos'
          onChange={onCarPhotoChange}
          multiple
          required
        />
      </Form.Row>
      <Button variant='primary' type='submit'>
        Сохранить
      </Button>
    </Form>
  );
};

export default FormAddOrEditCar;
