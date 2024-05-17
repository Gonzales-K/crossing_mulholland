import logo from './logo.svg';
import './App.css';
import NavBar from './NavBar';
import {ReactRouter, Routes, Route} from 'react';

function App() {
  return (
    <>
    < NavBar />
    <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
    </>
  );
}

export default App;
