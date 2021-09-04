import axios from "axios";
import { useState, useContext } from "react";
import { UserContext } from "../../Contexts/UserContext";
import {
  Button,
  Checkbox,
  IconButton,
  LocateIcon,
  Option,
  Select,
  SelectField,
  TextInput,
} from "evergreen-ui";
import "./Login.scss";
import GeoLocationProvider, {
  GeoLocation,
} from "../../Contexts/LocationContext";
import { BiLogInCircle } from "react-icons/bi";
import { VscEye, VscEyeClosed } from "react-icons/vsc";
import { Component } from "react";

export default class SignUp extends Component {
  static contextType = GeoLocation;
  constructor(props) {
    super(props);
    this.state = {
      geoLocation: "",
      as_donor: false,
      show_password: false,
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

          <SelectField label="Blood Group">
            <option>A+</option>
            <option>A-</option>
            <option>B+</option>
            <option>B-</option>
            <option>O+</option>
            <option>O-</option>
            <option>AB+</option>
            <option>AB-</option>
          </SelectField>
          <div>
            <TextInput
              placeholder="password"
              type={this.state.show_password ? "text" : "password"}
            />
            <IconButton
              icon={this.state.show_password ? VscEyeClosed : VscEye}
              onClick={(e) => {
                e.preventDefault();
                this.setState((prev) => ({
                  show_password: !prev.show_password,
                }));
              }}
            ></IconButton>
          </div>

          <Checkbox
            checked={this.state.as_donor}
            onChange={() =>
              this.setState((prev) => ({ as_donor: !prev.checked }))
            }
            label="Sign me as a donor"
          ></Checkbox>

          <Button appearance="primary" iconAfter={BiLogInCircle}>
            SignUp
          </Button>
        </form>
      </div>
    );
  }
}
