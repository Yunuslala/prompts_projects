import React, { useState } from 'react';
import './App.css';

const App = () => {
  const choices = ['rock', 'paper', 'scissors'];
  const [userChoice, setUserChoice] = useState(null);
  const [computerChoice, setComputerChoice] = useState(null);
  const [result, setResult] = useState(null);
  const [computerScore, setComputerScore] = useState(null);
  const [userScore, setUserScore] = useState(null);
  const [drawScore, setDrawScore] = useState(0);
  const handleResetResult=async()=>{
    console.log("object1")
    const response = await fetch('http://localhost:5000/resetgame', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data=await response.json()
    setUserChoice(null);
    setComputerChoice(null);
    setResult(null);
    setComputerScore(data.computer_score);
    setUserScore(data.user_score);
    setDrawScore(data.draws);
  }

  const handleUserChoice = async (choice) => {
    const response = await fetch('http://localhost:5000/play', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ choice }),
    });

    const data = await response.json();
    setUserChoice(data.user_choice);
    setComputerChoice(data.computer_choice);
    setResult(data.result);
    setComputerScore(data.computer_score);
    setUserScore(data.user_score);
    setDrawScore(data.draws);
  };

  return (
    <div className="container">
      <h1 className="title">Rock, Paper, Scissors</h1>
      <div className="game">
        <div className="choices">
          {choices.map((choice) => (
            <button
              key={choice}
              className={`choice-btn ${userChoice === choice ? 'selected' : ''}`}
              onClick={() => handleUserChoice(choice)}
              
            >
              {choice}
            </button>
          ))}
        </div>
        {userChoice && (
          <div className="result">
            <div className="result-item">
              <span className="result-label">Your choice:</span>
              <span className="result-value">{userChoice}</span>
            </div>
            <div className="result-item">
              <span className="result-label">Computer's choice:</span>
              <span className="result-value">{computerChoice}</span>
            </div>
            <div className="result-item">
              <span className="result-label">Your score:</span>
              <span className="result-value">{userScore}</span>
            </div>
            <div className="result-item">
              <span className="result-label">Computer's score:</span>
              <span className="result-value">{computerScore}</span>
            </div>
            <div className="result-item">
              <span className="result-label">Draws:</span>
              <span className="result-value">{drawScore}</span>
            </div>
            <div className="result-item">
              <span className="result-label">Result:</span>
              <span className="result-value">{result}</span>
            </div>
          </div>
        )}
      </div>
      <div className='choices'>
        <button className='choice-btn rest-choice' onClick={()=>handleResetResult()}>Reset Game</button>
      </div>
    </div>
  );
};

export default App;
