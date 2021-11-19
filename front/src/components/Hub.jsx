import Profile from "./Profile";
import Search from "./Search";
import Home from "./Home";
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom';
import UserService from "../services/UserService";


const Hub = () => (
    <Router>
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="/">
                        <img src="/dsaster.png" alt="" width="24" height="24" class="d-inline-block align-text-top" />
                        <strong> DSaster</strong>
                    </a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNavDropdown">
                        <ul className="navbar-nav mr-auto">
                            <li className="nav-item"><Link to={'/'} className="nav-link">Home</Link></li>
                            <li className="nav-item"><Link to={'/search'} className="nav-link">Search</Link></li>
                            <li className="nav-item"><Link to={'/profile'} className="nav-link">{UserService.getUsername()}</Link></li>
                            <li className="nav-item"><a className="nav-link" href="#" onClick={() => UserService.doLogout()}>Log out</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <br />
            <Switch>
                <Route exact path='/' component={Home} />
                <Route path='/search' component={Search} />
                <Route path='/profile' component={Profile} />
            </Switch>
        </div>
    </Router>
);



export default Hub;