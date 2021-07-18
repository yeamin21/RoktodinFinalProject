import { NavLink } from "react-router-dom";
import { UserContext } from "../../../Contexts/UserContext";
import { useContext } from "react";

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
      exact:true
    },
    {
      to: "requests",
      name: "Requests",
      exact:true
    },
  ];

  return (
    <div className="nav-list">
      {items.map((item, key) => (
        <NavLink
          exact = {item.exact}
          key={key}
          to={item.to}
        >
          {item.name}
        </NavLink>
      ))}
    </div>
  );
}

function UserNav() {
  const items = [
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
  const userContext = useContext(UserContext);
  return (
    <div>
      {userContext.authenticated ? (
        <NavLink exact={items[1].exact} to={items[1].to}>
          {items[1].name}
        </NavLink>
      ) : (
        <NavLink exact={items[0].exact} to={items[0].to}>
          {items[0].name}
        </NavLink>
      )}
    </div>
  );
}
