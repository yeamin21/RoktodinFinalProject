import { Component } from "react";
import "./Card.scss";
export default class Card extends Component {
  constructor(props) {
    super(props);
    this.state = {
      head: props.head,
      item: props.item,
    };
  }

  render() {
    //const {receiver}  = this.state.item

    return (
      <div className="card">
        <div className="head">{this.state.head}</div>
        {Object.keys(this.state.item).map((i) => (
          <div>
            {i} {this.state.item[i]}
          </div>
        ))}
      </div>
    );
  }
}
