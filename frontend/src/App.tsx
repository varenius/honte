import React from 'react';
import {PlayerList} from './PlayerList';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'


type Player = {
    firstName: string,
    lastName: string,
}

const players: Array<Player> = [
    {
        firstName: "Hampus",
        lastName: "Linander",
    },
    {
        firstName: "Magnus",
        lastName: "Sandén",
    },
    {
        firstName: "Eskil",
        lastName: "Varenius",
    },
];


const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        Honte
      </header>
      <PlayerList players={players} />
    </div>
  );
}

export default App;
