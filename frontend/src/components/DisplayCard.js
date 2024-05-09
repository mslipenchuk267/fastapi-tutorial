import React, { useState, useEffect } from 'react';
import BaseCard from './BaseCard';
import '../styles/DisplayCard.css';

function DisplayCard() {
  const [items, setItems] = useState([]);

  const fetchItems = async () => {
    const response = await fetch('http://localhost:8000/items/');
    const data = await response.json();
    setItems(data);
  };

  useEffect(() => {
    fetchItems();
  }, []);

  return (
    <BaseCard className="display-card" title="Task List">
      <div className="items-list">
        {items.map(item => (
          <div key={item.id}>{item.text} - {item.is_done ? "Done" : "Not Done"}</div>
        ))}
      </div>
    </BaseCard>
  );
}

export default DisplayCard;