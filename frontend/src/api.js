import axios from 'axios';
import store from "./store/store.js"

export default axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        'Content-Type': 'application/json',
        'Authorization': "JWT " + store.state.jwt,
        "Access-Control-Allow-Origin":"*"

    },

});