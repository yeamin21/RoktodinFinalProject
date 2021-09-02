import axios from "axios";
import { useState, useContext } from "react";
import { UserContext } from "../../Contexts/UserContext";
import { Button, IconButton, LocateIcon, TextInput } from "evergreen-ui";
import "./Login.scss";
import GeoLocationProvider, {
  GeoLocation,
} from "../../Contexts/LocationContext";
import { BiLogInCircle } from "react-icons/bi";
import { Component } from "react";

export default class SignUp extends Component {
  static contextType = GeoLocation;
  constructor(props) {
    super(props);
    this.state = {
      geoLocation: "",
    };

    this.getLocation = this.getLocation.bind(this);
  }
  getLocation = (e) => {
    e.preventDefault();
    this.setState({ geoLocation: this.context.full_address });
  };

  render() {
    return (
      <div className="login">
        <form>
          <TextInput placeholder="choose username" />
          <TextInput placeholder="email" type="email" />
          <div>
            <TextInput
              placeholder="location"
              value={this.state.geoLocation}
              onChange={(e) => this.setState({ geoLocation: e.target.value })}
              type="text"
            />
            <IconButton
              icon={LocateIcon}
              onClick={(e) => this.getLocation(e)}
            ></IconButton>
          </div>
          <TextInput placeholder="password" type="password" />
          <Button appearance="primary" iconAfter={BiLogInCircle}>
            SignUp
          </Button>
        </form>
      </div>
    );
  }
}
