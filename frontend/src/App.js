import React, { useState } from 'react';

import InputCard from './components/InputCard';
import DisplayCard from './components/DisplayCard';

import './App.css';

function App() {
  const [triggerUpdate, setTriggerUpdate] = useState(false);

  const handleAddItem = () => setTriggerUpdate(!triggerUpdate);

  return (
    <div className="app" style={{ display: 'flex' }}>
      <InputCard onAddItem={handleAddItem} />
      <DisplayCard key={triggerUpdate} />
    </div>
  );
}

export default App;
