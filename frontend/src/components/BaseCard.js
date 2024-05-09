import React from 'react';
import '../styles/BaseCard.css';

function BaseCard({ className, title, children }) {
    return (
      <div className={`base-card ${className}`}>
        <h2 className="card-title">{title}</h2>
        {children}
      </div>
    );
  }
  

export default BaseCard;