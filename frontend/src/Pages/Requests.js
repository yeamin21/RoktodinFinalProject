import { Component } from "react";
import Card from "../Components/Card";
import { axiosInstace } from "../Services/ApiCalls";
import "./Requests.scss"
export default class Requests extends Component {
  constructor(props) {
    super(props);
    this.state = { list: [] };
  }
  componentDidMount() {
    axiosInstace.get("/requests/").then((res) => this.setState({ list: res.data }));
  }
  render() {
    const { list } = this.state;
    return (
      <div className="requests">
  
        {list.map((item) => (
          <div className="request"><Card item={item}></Card></div>
        ))}
      </div>
    );
  }
}
