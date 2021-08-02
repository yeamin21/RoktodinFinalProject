import axios from "axios";
import { Component } from "react";
const baseURL = "http://localhost:8000/api/";
const timeout = 5000;
export const axiosInstace = axios.create({
  baseURL: baseURL,
  timeout: timeout,
});

// axiosInstace.interceptors.response.use(
//   () => console.log("success"),
//   (err) => console.log(err.status.code)
// );

export const retrieve = async (param, query) => {
  try {
    return await axiosInstace.get(param);
  } catch (r) {
    console.log(r);
  }
};
