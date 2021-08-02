import { Component } from "react";
import { Link } from "react-router-dom";
import { axiosInstace, retrieve } from "../../Services/ApiCalls";
import Card from "../Card";
import "./DonorLIst.scss";
export default class DonorList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      donors: [],
    };
    this.askForNumber = this.askForNumber.bind(this);
  }
  componentDidMount() {
    retrieve("donors/").then((res) => this.setState({ donors: res.data }));
  }

  askForNumber = () =>
    axiosInstace.post("notify/").then((res) => console.log(res));
  render() {
    return (
      <div className="donor-list">
        {this.state.donors.map((donor) => {
          return (
            <div className="donor">
              <Card
                head={donor.id}
                item={{
                  Phone: donor.phone ? (
                    donor.phone
                  ) : (
                    <button onClick={this.askForNumber}>
                      Ask for Phone No
                    </button>
                  ),
                  "Blood Group": donor.blood_group,
                }}
              ></Card>
            </div>
          );
        })}
      </div>
    );
  }
}
