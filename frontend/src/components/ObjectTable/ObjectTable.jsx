import React from 'react';

import Table from 'react-bootstrap/Table';
import './ObjectTable.scss';

const ObjectTable = ({ headings, data, className }) => {
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
        </tr>
      </thead>
      <tbody>
        {data.map((dataRow, i) => (
          <tr key={i}>
            {dataRow.map((dataCol, i) => (
              <td key={i}>{dataCol || ''}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default ObjectTable;
