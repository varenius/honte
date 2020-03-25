import React from 'react';
import { BrowserRouter as Router, Link, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.css'

import {PlayerList} from './PlayerList';
import {GamesList} from './GamesList';
import logo from './logo.svg';
import './App.css';


const Home: React.FC = () => {
    return (
        <h3>Home</h3>
    )
}

const App: React.FC = () => {
    return (
        <Router>
            <div className="App">
                <header className="App-header">
                    <div className="App-title">
                        <img src={logo} className="App-logo" alt="logo" />
                        Honte
                    </div>
                    <nav className="App-menu">
                        <ul>
                            <li>
                                <Link to="/">Home</Link>
                            </li>
                            <li>
                                <Link to="/players">Players</Link>
                            </li>
                            <li>
                                <Link to="/games">Games</Link>
                            </li>
                        </ul>
                    </nav>
                </header>
                <Route path="/" exact component={Home} />
                <Route path="/players" component={PlayerList} />
                <Route path="/games" exact component={GamesList} />
            </div>
        </Router>
    );
}

export default App;
