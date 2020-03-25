import React, {useState, useEffect} from 'react';

const backend_url = 'http://localhost:3000/api'


interface Game {
    id: number,
    player1: {
        firstName: string,
        lastName: string,
    },
    player2: {
        firstName: string,
        lastName: string,
    },

}


const GamesList: React.FC = () => {
    var [games, setGames] = useState([]);
    useEffect(() => {
        fetch(backend_url + '/games/')
            .then(response => response.json())
            .then(gamesList => {
                setGames(gamesList);
            })
    },
              []);

    const rows = games.map((game: Game) => (
        <tr key={game.id}><td>{game.player1.firstName} {game.player1.lastName}</td><td>{game.player2.firstName} {game.player2.lastName}</td></tr>
    ))
    return (
        <table className="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Black</th>
                    <th scope="col">White</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    )
}

export {GamesList};
