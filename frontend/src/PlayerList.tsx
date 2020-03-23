import React, {useState, useEffect} from 'react';

const backend_url = 'http://localhost:3000/api'


interface Player {
    firstName: string;
    lastName: string;
}


const PlayerList = () => {
    var [players, setPlayers] = useState([]);
    useEffect(() => {
        fetch(backend_url + '/players/')
            .then(response => response.json())
            .then(playerList => {
                setPlayers(playerList);
            })
    },
              []);

    const rows = players.map((player: Player) => (
            <tr key={player.firstName}><td>{player.firstName}</td><td>{player.lastName}</td></tr>
    ))
    return (
        <table className="table table-hover">
            <thead>
                <tr>
                    <th scope="col">First name</th>
                    <th scope="col">Last name</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    )
}

export {PlayerList};
