import React, { Component } from 'react';
import { render } from 'react-dom';
import { App } from './app';
import { usePromiseTracker } from "react-promise-tracker";

 
const LoadingIndicator = props => {
    return (
     <h1>Hey some async call in progress ! </h1>
   );  
  }

render(
  <div>
    <App />
  </div>,
  document.getElementById('root'));