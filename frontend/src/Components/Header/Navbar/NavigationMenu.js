import { NavLink } from "react-router-dom";
import { UserContext } from "../../../Contexts/UserContext";
import { Component, useContext } from "react";
import "./NavigationMenu.scss";
export default function NavigationMenu() {
  return (
    <div className="nav-menu">
      <NavList />
      <UserNav />
    </div>
  );
}
function NavList() {
  const items = [
    {
      to: "/",
      name: "Home",
      exact: true,
    },
    {
      to: "requests",
      name: "Requests",
      exact: true,
    },
    {
      to: "donors",
      name: "Donors",
      exact: true,
    },
  ];

  return (
    <div className="primary">
      {items.map((item, key) => (
        <NavLink exact={item.exact} key={key} to={item.to}>
          {item.name}
        </NavLink>
      ))}
    </div>
  );
}

class UserNav extends Component {
  items = [
    {
      to: "login",
      name: "Login",
      exact: true,
    },
    {
      to: "logout",
      name: "Logout",
      exact: true,
    },
  ];

  componentDidUpdate(prevProps, prevState) {
    console.log("updated");
  }

  render() {
    return (
      <UserContext.Consumer>
        {({ authenticated, logout, username }) => (
          <div className="user">
            {authenticated ? (
              <>
                <NavLink exact={true} to={"/profile"}>
                  {username}
                </NavLink>
                <NavLink
                  exact={this.items[1].exact}
                  onClick={logout}
                  to={this.items[1].to}
                >
                  {this.items[1].name}
                </NavLink>
              </>
            ) : (
              <NavLink exact={this.items[0].exact} to={this.items[0].to}>
                {this.items[0].name}
              </NavLink>
            )}
          </div>
        )}
      </UserContext.Consumer>
    );
  }
}
