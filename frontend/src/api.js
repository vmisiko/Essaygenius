import axios from 'axios';
import store from "./store/store.js"


export default axios.create({
    baseURL: "http://localhost:8000/",
    headers: {'Authorization': 'Bearer '+store.state.jwt}
    
}); 