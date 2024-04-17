import logo from './logo.svg';
import './App.css';
import { TextField } from '@mui/material';
import { useEffect, useState } from 'react';

function App() {
  const [itemId, setItemId] = useState("1")

  useEffect(() => {
    console.log(`$itemId`)
  }, [itemId])

  return (
    <div className="App">
      <header className="App-header">
      <TextField
          id="outline-basic"
          label="Item ID"
          variant="outlined"
          color="warning" focused
          value={itemId}
          onChange={e=>setItemId(e.target.value)}
        />
      </header>
    </div>
  );
}

export default App;