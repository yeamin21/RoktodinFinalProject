import { Component, createContext } from "react";
import { APICalls, LocationApi } from "../Services/ApiCalls";

export const GeoLocation = createContext({});
export default class GeoLocationProvider extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coords: {
        latitude: undefined,
        longitude: undefined,
      },
      full_address: "",
    };
  }
  getLocationValues = () => {
    APICalls.getUserLocation(
      this.state.coords.latitude,
      this.state.coords.longitude
    ).then((r) => this.setState({ full_address: r.data.display_name }));
  };

  componentDidMount() {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          this.setState({
            coords: {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude,
            },
          });
        },
        () => this.getLocationValues()
      );
    }
  }
  componentDidUpdate(prevProps, prevState) {
    if (this.state.coords !== prevState.coords) {
      this.getLocationValues();
    }
  }
  render() {
    return (
      <GeoLocation.Provider value={this.state}>
        {this.props.children}
      </GeoLocation.Provider>
    );
  }
}
