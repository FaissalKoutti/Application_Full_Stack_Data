// Profile.js
import UserService from "../services/UserService";
import React, { Component } from 'react';

class Profile extends Component {
  render() {
    
    return (
        <div className="container">
          <h3>{UserService.getUsername()}</h3>
          <p>Not available yet...👷‍♂️</p>
        </div>
    );
  }
}

export default Profile;