import { faTrash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import React from 'react';

import Table from 'react-bootstrap/Table';
import './ObjectTable.scss';

const ObjectTable = ({ headings, data, className, onDelete }) => {
  console.log(data);
  return (
    <Table
      striped
      bordered
      hover
      className={'object-table ' + (className || '')}
    >
      <thead>
        <tr>
          {headings.map((heading, i) => (
            <th key={i}>{heading}</th>
          ))}
          <th></th>
        </tr>
      </thead>
      <tbody>
        {data.map((dataRow, i) => (
          <tr key={i}>
            {dataRow.map((dataCol, i) => (
              <td key={i}>{dataCol || ''}</td>
            ))}
            <td>
              <FontAwesomeIcon
                onClick={() => onDelete(dataRow[0])}
                icon={faTrash}
                color='red'
              />
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default ObjectTable;
