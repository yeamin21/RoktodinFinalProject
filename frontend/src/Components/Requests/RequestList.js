import { Component } from "react";
import Card from "../Card";
import "./RequestsList.scss";
import { getData, retrieve } from "./../../Services/ApiCalls";
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
        {list.map((item) => {
          const obj = {
            Receiver: item.receiver,
            "Bag Required": item.no_bag_required,
            "Bag Managed": item.no_bag_managed,
          };
          return (
            <div className="request">
              <Card item={obj}></Card>
            </div>
          );
        })}
      </div>
    );
  }
}
