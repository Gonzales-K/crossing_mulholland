import './App.css';
import NavBar from './NavBar';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Home from './home';
import Collections from './collections';
import Care from './care';
import About from './about';
import Contact from './contact';
import Checkout from './checkout';

function App() {
  return (
    <>
    <BrowserRouter>
      < NavBar />
      <Routes>
        <Route path="/home" element ={<Home />} />
        <Route path='/collections' element= {<Collections />} />
        <Route path='/care' element= {<Care />} />
        <Route path='/about' element= {<About />} />
        <Route path='/contact' element= {<Contact />} />
        <Route path='/checkout' element= {<Checkout />} />
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
