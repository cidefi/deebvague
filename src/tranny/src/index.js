import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

const fs = require('fs');
const path = require('path');

class AudioSegment {
  constructor(filename) {
    this.filename = filename;
    this.transcription = '';
  }

  playAudio() {
    // play the dang audio file

    // should be at a slow speed by default
  }
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

serviceWorker.unregister();
