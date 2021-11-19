import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import App from './components/App';
// import reportWebVitals from './reportWebVitals';

// Keycloak related services
import HttpService from "./services/HttpService";
import UserService from "./services/UserService";

const renderApp = () => ReactDOM.render(<App/>, document.getElementById("root"));

UserService.initKeycloak(renderApp);
HttpService.configure();
renderApp();
// reportWebVitals();
