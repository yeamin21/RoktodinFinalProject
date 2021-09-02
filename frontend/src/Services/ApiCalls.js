import axios from "axios";
const baseURL = "http://localhost:8000/api/";
const timeout = 5000;
export const axiosInstace = axios.create({
  baseURL: baseURL,
  timeout: timeout,
});

export const retrieve = async (param, query) => {
  try {
    return await axiosInstace.get(param);
  } catch (r) {
    console.log(r);
  }
};

// axiosInstace.interceptors.response.use(
//   () => console.log("success"),
//   (err) => console.log(err.status.code)
// );
export const APICalls = {
  async getUserLocation(lat = undefined, lon = undefined) {
    const userLocation = await axios.get(
      `${baseURL}user-location/`,
      lat && lon
        ? {
            params: { lat, lon },
          }
        : null
    );
    return userLocation;
  },
};

export const LocationApi = {
  locationProviderURL: "https://nominatim.openstreetmap.org",
  async getLocationDetails(lat, lon) {
    const dataFormat = "json";
    const locationDetails = await axios.get(
      `${this.locationProviderURL}/reverse?lat=${lat}&lon=${lon}&format=${dataFormat}`
    );
    return locationDetails;
  },
};
