import { Component, createContext } from "react";
import { Redirect } from "react-router-dom";
import Login from "../Pages/Login";
import { axiosInstace } from "../Services/ApiCalls";
export const UserContext = createContext({
  access: "",
  refresh: "",
  authenticated: false,
  authenticate: () => {},
  logout:()=>{}
});

export default class UserContextProvider extends Component {
  constructor(props) {
    super(props);
    this.state = {
      access: "",
      refresh: "",
      authenticated: false,
      authenticate: this.authenticate,
      logout: this.logout
    };
    this.authenticate = this.authenticate.bind(this);
    this.validate = this.validate.bind(this);
    this.logout = this.logout.bind(this)
  }
  componentDidMount() {
    const stored_token = localStorage.getItem("auth");
    stored_token
     && this.setState(JSON.parse(stored_token), () => this.validate())
    
  }
  validate = () =>
    axiosInstace
      .get("users/", {
        headers: { Authorization: `Bearer ${this.state.access}` },
      })
      .then(() => this.setState({ authenticated: true }));
  authenticate = (username, password) => {
    axiosInstace
      .post("/token/", { username: username, password: password })
      .then((res) => {
        const { access, refresh } = res.data;
        this.setState( {access, refresh, authenticated:true}); return {access,refresh};
      })
      .then((access,refresh) => {
        localStorage.setItem("auth", JSON.stringify(access,refresh));
      });
  };
  logout=()=>
  {
    this.setState({authenticated:false, refresh:'', access:''},localStorage.removeItem('auth'))
  }
  render() {
    return (
      <UserContext.Provider value={this.state}>
        {this.props.children}
      </UserContext.Provider>
    );
  }
}
