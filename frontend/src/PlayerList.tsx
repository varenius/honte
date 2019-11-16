import React from 'react';


type Player = {
    firstName: string,
    lastName: string,
}


type PlayerListProps = {
    players: Array<Player>,
}


const PlayerList = ({players}: PlayerListProps) => {
    var rows = players.map((player) => (
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
