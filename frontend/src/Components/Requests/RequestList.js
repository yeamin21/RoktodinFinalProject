import { Component } from "react";
import Card from "../Card";
import "./RequestsList.scss";
import { retrieve } from "./../../Services/ApiCalls";
export default class RequestList extends Component {
  constructor(props) {
    super(props);
    this.state = { list: [], display: "grid" };
  }
  componentDidMount() {
    retrieve("requests/").then((res) => this.setState({ list: res.data }));
  }
  render() {
    const { list } = this.state;
    return (
      <div className="requests">
        {list.map((item) => (
          <div className="request">
            <Card item={item}></Card>
          </div>
        ))}
      </div>
    );
  }
}
