import './App.css';
import { useEffect, useState } from 'react';

function App() {

  let [message, setMessage] = useState('');

  function getMessage() {
    fetch('/api/message/get').then((response) => {
      return response.text();
    }).then((resBody) => {
      setMessage(resBody);
    }).catch((error) => {
      console.log('[Error]getMessage():', error);
    });
  }

  useEffect(() => {
    getMessage();
    console.log('message:', message);
  }, [message]);

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  );
}

export default App;
