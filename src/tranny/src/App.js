import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
        <img src={logo} className="App-logo" alt="logo" />
        tranny
        </p>
      </header>
      <div id="main">
        <h1>tranny - a transcription framework</h1>
        <p><strong>trust the plan:</strong></p>
        <ul>
          <li>audio clip will play in a loop</li>
          <li>transcribe the audio clip in the box</li>
          <li>press ctrl + enter when finished to move onto the next clip</li>
          <li>if a clip needs to be thrown out, press ctrl + shift + enter to mark it as retarded</li>
        </ul>
      </div>
    </div>
  );
}

export default App;
