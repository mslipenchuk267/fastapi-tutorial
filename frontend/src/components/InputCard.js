import React, { useState } from 'react';
import BaseCard from './BaseCard';
import '../styles/InputCard.css';

function InputCard({ onAddItem }) {
  const [input, setInput] = useState('');

  const handleSubmit = async () => {
    const response = await fetch('http://localhost:8000/items/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: input })
    });
    if (response.ok) {
      setInput('');
      onAddItem();
    }
  };

  return (
    <BaseCard className="input-card" title="Add New Item">
      <input 
        type="text" 
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter text"
      />
      <button onClick={handleSubmit}>Submit</button>
    </BaseCard>
  );
}

export default InputCard;