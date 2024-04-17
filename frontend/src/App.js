import './App.css';
import { List, ListItem, ListItemIcon, ListItemText, TextField } from '@mui/material'
import LocalMoviesIcon from '@mui/icons-material/LocalMovies'
import { useEffect, useState } from 'react'


function App() {
  const [movieId, setMovieId] = useState("1")

  useEffect(() => {
    console.log(`${movieId}`)

    if(movieId === "") {
      setMovieId(movieId)
    } else if(isNaN(movieId)) {
      setMovieId(movieId)
    } else {
      fetch(`http://localhost:8000/movies/${movieId}`)
      .then(result => result.json())
      .then(result => {
        console.log(result)
      })
    }
  }, [movieId])

  return (
    <div className="App">
      <header className="App-header">
        <TextField
          id="outline-basic"
          label="Movie ID"
          variant="outlined"
          color="warning" focused
          value={movieId}
          onChange={e=>setMovieId(e.target.value)}
        />
      </header>
    </div>
  );
}

export default App;