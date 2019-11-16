import React, {useState, useEffect} from 'react';
import {PlayerList} from './PlayerList';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'

const backend_url = 'http://localhost:3000/api'

type Player = {
    firstName: string,
    lastName: string,
}

const App: React.FC = () => {
    var [players, setPlayers] = useState([]);
    useEffect(() => {
        fetch(
            backend_url + '/vinst/')
            .then((response) => response.json())
            .then((data) => {
                setPlayers(data.players);
            })
    },
              []);
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
