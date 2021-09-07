import { useContext } from "react";
import { FaReact } from "react-icons/fa";
import { BrowserRouter, Route } from "react-router-dom";
import "./App.scss";
import NavigationMenu from "./Components/Header/Navbar/NavigationMenu";
import Login from "./Components/Profile/Login";
import SignUp from "./Components/Profile/SignUp";
import GeoLocationProvider from "./Contexts/LocationContext";
import UserContextProvider, { UserContext } from "./Contexts/UserContext";
import Donors from "./Pages/Donors";
import Home from "./Pages/Home";
import Profile from "./Pages/Profile";
import Requests from "./Pages/Requests";
function App() {
  const context = useContext(UserContext);
  console.log(context);
  return (
    <BrowserRouter>
      <UserContextProvider>
        <GeoLocationProvider>
          <Header></Header>
          <Body></Body>
          <Footer></Footer>
        </GeoLocationProvider>
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
      <Route path="/signup" component={SignUp}></Route>
    </body>
  );
}

function Footer() {
  return (
    <footer>
      <FaReact size="100px" color="blue"></FaReact>
    </footer>
  );
}

export default App;
