import React, { useState } from "react";

const IncrementDecrementBtn = ({ minValue = 1, maxValue = 100 }) => {
    const [count, setCount] = useState(minValue);

    const handleIncrementCounter = () => {
        if (count < maxValue) {
            setCount((prevState) => prevState + 1);
            }
    };

    const handleDecrementCounter = () => {
        if (count > minValue) {
            setCount((prevState) => prevState - 1);
        }
    };

    return (
        <div className="btn-group">
          <button className="increment-decrement-btn" onClick={handleIncrementCounter}>
            <span class="material-symbols-outlined">-</span>
          </button>
          <p className="increment-decrement-btn-p">{count}</p>
          <button className="increment-decrement-btn" onClick={handleDecrementCounter}>
            <span class="material-symbols-outlined">+</span>
          </button>
        </div>
        );
        };

export default IncrementDecrementBtn;