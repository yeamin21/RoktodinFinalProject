import axios from "axios";
import { useState } from "react";
import UserContextProvider, {UserContext} from "../Contexts/UserContext";


export default function Login() {
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();

  return (
<UserContext.Consumer>
  {({authenticate})=>
  <div className="login">
  <form method="POST" onSubmit={(e)=>{e.preventDefault(); authenticate(username,password)}}>
    <input type="text" onChange={(e) => setUsername(e.target.value)}></input>
    <input
      type="password"
      onChange={(e) => setPassword(e.target.value)}
    ></input>
    <input
      type="submit">
      </input>
  </form>
</div>
  }   
</UserContext.Consumer>

    
  );
}
