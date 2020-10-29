import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)
// import router from "../router"

export default new Vuex.Store({
    state: {
        authUser: {},
        isAuthenticated: false,
        jwt: localStorage.getItem('t'),
        endpoints: {
          obtainJWT: 'http://127.0.0.1:8000/api/token/',
          refreshJWT: 'http://localhost:8000/api/token/refresh/',
          baseUrl:"http://localhost:8000/"
        }
      },
    mutations: {
      setAuthUser(state, {
          authUser,
          isAuthenticated
        }) {
          state.authUser = authUser
          state.isAuthenticated = isAuthenticated
        },
        updateToken(state, newToken){
          localStorage.setItem('t', newToken);
          state.jwt = newToken;
        },
        removeToken(state){
          localStorage.removeItem('t');
          state.jwt = null;
          state.authUser={}
          state.isAuthenticated=false
        }
        
      },
    actions : {
        obtainToken( username, password) {
            const payload = {
              email: password.payload.email,
              password: password.payload.password,
            }
            console.log(payload)
            axios.post(this.state.endpoints.obtainJWT, payload)
              .then((response)=>{
                  console.log(response.data)
                  this.commit('updateToken', response.data.access);
                })
              .catch((error)=>{
                  console.log(error);
                })

          },

        refreshToken(){
            const payload = {
              token: this.state.jwt
            }
            axios.post(this.state.endpoints.refreshJWT, payload)
              .then((response)=>{
                  this.commit('updateToken', response.data.token)
                })
              .catch((error)=>{
                  console.log(error)
                })
        }
    }
    
});