import axios from "axios";
import { Component } from "react";
const baseURL = "http://localhost:8000/api/";
const timeout = 5000;
export const axiosInstace = axios.create({
  baseURL: baseURL,
  timeout: timeout,
});

export const retrieve = async (param, query) => {
  return await axiosInstace.get(param);
};
