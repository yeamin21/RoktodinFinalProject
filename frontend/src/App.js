import logo from "./logo.svg";
import "./App.scss";
import NavigationMenu from "./Components/Header/Navbar/NavigationMenu";
import { BrowserRouter, Route } from "react-router-dom";
import Requests from "./Pages/Requests";
import UserContextProvider, { UserContext } from "./Contexts/UserContext";
import { useContext } from "react";
import Profile from "./Pages/Profile";
import Login from "./Components/Profile/Login";
import Donors from "./Pages/Donors";
import Home from "./Pages/Home";

function App() {
  const context = useContext(UserContext);
  console.log(context);
  return (
    <BrowserRouter>
      <UserContextProvider>
        <Header></Header>
        <Body></Body>
        <Footer></Footer>
      </UserContextProvider>
    </BrowserRouter>
  );
}
function Header() {
  return (
    <header className="Header">
      <NavigationMenu />
    </header>
  );
}

function Body(props) {
  return (
    <body className="Body">
      <Route path="/" exact component={Home}></Route>
      <Route path="/login" component={Login}></Route>
      <Route path="/requests" component={Requests}></Route>
      <Route path="/profile" component={Profile}></Route>
      <Route path="/donors" component={Donors}></Route>
    </body>
  );
}

function Footer() {
  return <footer></footer>;
}

export default App;
