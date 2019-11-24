import React, {useState, useEffect} from 'react';
import {PlayerList} from './PlayerList';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'

const backend_url = 'http://localhost:3000/api'

interface ServerPlayer {
    first_name: string;
    last_name: string;
}

const App: React.FC = () => {
    var [players, setPlayers] = useState([]);
    useEffect(() => {
        fetch(backend_url + '/players/')
            .then(response => response.json())
            .then((data) => data.map((player: ServerPlayer) => (
            {
                firstName: player.first_name,
                lastName: player.last_name,
            }
            )))
            .then(playerList => {
                setPlayers(playerList);
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
