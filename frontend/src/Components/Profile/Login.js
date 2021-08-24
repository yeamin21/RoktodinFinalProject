import axios from "axios";
import { useState } from "react";
import { UserContext } from "../../Contexts/UserContext";
import { Button, TextInput, TextInputField } from "evergreen-ui";
import "./Login.scss";
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
  return (
    <div className="login">
      <form>
        <TextInput placeholder="choose username" />
        <TextInput placeholder="email" type="email" />
        <TextInput placeholder="password" type="password" />
        <Button appearance="primary" iconAfter={BiLogInCircle}>
          SignUp
        </Button>
      </form>
    </div>
  );
}
