import logo from "./logo.svg";
import "./App.scss";
import NavigationMenu from "./Components/Header/Navbar/NavigationMenu";
import { BrowserRouter, Route, Router } from "react-router-dom";
import Login from "./Pages/Login";
import Requests from "./Pages/Requests";
import UserContextProvider, { UserContext } from "./Contexts/UserContext";
import { useContext } from "react";

function App() {
  const context = useContext(UserContext)
  console.log(context);
  return (
    <BrowserRouter>
    <UserContextProvider>
    <div className="App">
          <Header></Header>
          <Body></Body>
           <Footer></Footer>
        </div>
        </UserContextProvider>
    </BrowserRouter>
    
  );
}
function Header() {
  return (
    <div className="Header">
      <NavigationMenu />
    </div>
  );
}

function Body(props) {
  return (
    <div className="Body">
      <Route path="/login" component={Login}></Route>
      <Route path="/requests" component={Requests}></Route>
    </div>
  );
}

function Footer(){
  return(<div></div>)
}

export default App;
