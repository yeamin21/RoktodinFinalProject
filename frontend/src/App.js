import logo from "./logo.svg";
import "./App.css";
import NavigationMenu from "./Components/Header/Navbar/NavigationMenu";

function App() {
  return (
    <div className="App">
      <Header></Header>
      <Body></Body>
      {/* <Footer></Footer> */}
    </div>
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
  return <div className="Body"></div>;
}

export default App;
