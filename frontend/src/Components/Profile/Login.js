import axios from "axios";
import { useState, useContext } from "react";
import { UserContext } from "../../Contexts/UserContext";
import {
  Button,
  IconButton,
  Label,
  LocateIcon,
  TextInput,
  TextInputField,
} from "evergreen-ui";
import "./Login.scss";
import GeoLocationProvider, {
  GeoLocation,
} from "../../Contexts/LocationContext";
import { BiLogInCircle } from "react-icons/bi";
import { Redirect, useHistory } from "react-router-dom";
export default function Login() {
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();
  const history = useHistory();
  return (
    <UserContext.Consumer>
      {({ authenticate }) => (
        <div className="login">
          <form>
            <TextInput
              type="text"
              onChange={(e) => setUsername(e.target.value)}
            ></TextInput>
            <TextInput
              type="password"
              onChange={(e) => setPassword(e.target.value)}
            ></TextInput>
            <div className="btn-set">
              <Button
                onClick={(e) => {
                  e.preventDefault();
                  authenticate(username, password);
                }}
                appearance="primary"
                iconBefore={BiLogInCircle}
              >
                Login
              </Button>
              <Button
                appearance="primary"
                iconAfter={BiLogInCircle}
                onClick={() => history.push("/signup")}
              >
                SignUp
              </Button>
            </div>
          </form>
        </div>
      )}
    </UserContext.Consumer>
  );
}

export function SignUp() {
  const geoLocation = useContext(GeoLocation);
  const [Location, setlocation] = useState();
  const getLocation = (e) => {
    e.preventDefault();
    setlocation({ geoLocation });
  };
  return (
    <div className="login">
      <form>
        <TextInput placeholder="choose username" />
        <TextInput placeholder="email" type="email" />
        <div>
          <TextInput
            placeholder="location"
            value={Location.full_address}
            onChange={(e) => setlocation(e.target.value)}
            type="text"
          />
          <IconButton
            icon={LocateIcon}
            onClick={(e) => getLocation(e)}
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
