import './App.css';
import NavBar from './NavBar';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Home from './home';

function App() {
  return (
    <>
    <BrowserRouter>
      < NavBar />
      <Routes>
        <Route path="/home" element ={<Home />} />
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
