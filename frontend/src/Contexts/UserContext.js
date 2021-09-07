import { Component, createContext } from "react";
import { axiosInstace } from "../Services/ApiCalls";
export const UserContext = createContext({
  access: "",
  refresh: "",
  authenticated: false,
  authenticate: () => {},
  logout: () => {},
});

export default class UserContextProvider extends Component {
  constructor(props) {
    super(props);
    this.state = {
      access: "",
      refresh: "",
      authenticated: false,
      authenticate: this.authenticate,
      logout: this.logout,
    };
    this.authenticate = this.authenticate.bind(this);
    this.validate = this.validate.bind(this);
    this.logout = this.logout.bind(this);
  }
  componentDidMount() {
    const stored_token = localStorage.getItem("auth");
    console.log(stored_token);
    stored_token &&
      stored_token !== "undefined" &&
      this.setState(JSON.parse(stored_token), () => this.validate());
  }
  validate = () =>
    axiosInstace
      .get("user/", {
        headers: { Authorization: `Bearer ${this.state.access}` },
      })
      .then((res) =>
        this.setState({ authenticated: true, username: res.data.username })
      )
      .then(
        () =>
          (axiosInstace.defaults.headers.common[
            "Authorization"
          ] = `Bearer ${this.state.access}`)
      )
      .catch((err) => this.setState({ authenticated: false }));

  authenticate = (username, password) => {
    axiosInstace
      .post("/token/", { username: username, password: password })
      .then((res) => {
        const { access, refresh } = res.data;
        this.setState({ access, refresh });
        return { access, refresh };
      })
      .then(() => this.validate())
      .then(() => {
        const { access, refresh } = this.state;
        localStorage.setItem("auth", JSON.stringify({ access, refresh }));
      })
      .catch((err) => this.setState({ authenticated: false }));
  };
  logout = () => {
    this.setState(
      { authenticated: false, refresh: "", access: "" },
      localStorage.removeItem("auth")
    );
  };
  render() {
    return (
      <UserContext.Provider value={this.state}>
        {this.props.children}
      </UserContext.Provider>
    );
  }
}
