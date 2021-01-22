import { useContext } from 'react';
import { useAccordionToggle } from 'react-bootstrap/AccordionToggle';
import AccordionContext from 'react-bootstrap/AccordionContext';
import { faAngleUp, faAngleDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
const ArrowToggle = ({ eventKey, callback }) => {
  const currentEventKey = useContext(AccordionContext);

  const decoratedOnClick = useAccordionToggle(
    eventKey,
    () => callback && callback(eventKey)
  );

  const isCurrentEventKey = currentEventKey === eventKey;

  return (
    <FontAwesomeIcon
      icon={isCurrentEventKey ? faAngleUp : faAngleDown}
      onClick={decoratedOnClick}
      size='sm'
      style={{ cursor: 'pointer' }}
    />
  );
};

export default ArrowToggle;
