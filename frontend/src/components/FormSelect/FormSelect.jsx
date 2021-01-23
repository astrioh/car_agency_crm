import React from 'react';

import Form from 'react-bootstrap/Form';

const FormSelect = ({ name, options, required, onChange }) => {
  return (
    <Form.Control
      onChange={onChange}
      name={name}
      as='select'
      required={required}
    >
      <option>Выберите</option>
      {options.map((item) => (
        <option key={item.id} value={item.id}>
          {item.name}
        </option>
      ))}
    </Form.Control>
  );
};

export default FormSelect;
