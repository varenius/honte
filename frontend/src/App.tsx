import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'


type Player = {
    firstName: string,
    lastName: string,
}

type PlayerListProps = {
    players: Array<Player>,
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


const PlayerList = ({players}: PlayerListProps) => {
    var rows = players.map((player) => (
            <tr><td>{player.firstName}</td><td>{player.lastName}</td></tr>
    ))
    return (
            <table className="table table-hover">
              <thead>
                <th scope="col">First name</th>
                <th scope="col">Last name</th>
              </thead>
              <tbody>
                {rows}
              </tbody>
            </table>
    )
}

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
