<template>
     <div class="ant-card ">

                    <div class="card-header text-center">
                       <h3 >Login </h3> 
                    </div>
                    <v-divider class="mt-n1"></v-divider>

                    <div class="card-body">
                        
                        <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                        @submit.prevent="login"
                        >
                            <v-text-field
                            v-model="email"
                            label="Email"
                            :loading="loading"
                            :error-messages="error.email"
                            required
                            ></v-text-field>

                            <v-text-field
                            v-model="password"
                            label="Password"
                            required
                            :loading="loading"
                            :error-messages="error.password"
                            :type="show? 'text' : 'password'"
                            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                            @click:append="show=!show"
                            ></v-text-field>

                        <v-row>
                            <v-col>
                                <!-- <router-link to="/dashboard/" > -->
                                    <v-btn shaped color="success" type="submit" :loading="loading">
                                        Login
                                    </v-btn>
                                <!-- </router-link> -->

                            </v-col>

                            <v-col class="">
                                 <router-link to="/auth/forgot-password" tag='div' style="cursor:pointer;"> Forgot Password?</router-link>
                                 <router-link to="/auth/register" tag='div' style="cursor:pointer;"> Create new Account</router-link>
                            </v-col>
                         



                        </v-row>
                        
                    </v-form>


                    </div>

            
    </div>

</template>

<script>
import axios from "axios"
export default {
    name:"Login",
    data () {
        return {
            show:false,
            valid:false,
            email:"",
            password:"",
            loading:false,
            error:{}
        }
    },
    methods:{
        login() {
            const payload = {
              email: this.email,
              password: this.password
            }
            console.log(payload)

           axios.post(this.$store.state.endpoints.obtainJWT, payload)
              .then((response)=>{
                  console.log(response.data)
                  var token = response.data.access
                  
                  this.$store.commit('updateToken', response.data.access);

                   const instance = axios.create({
                            baseURL: "http://localhost:8000/",
                            headers: {'Authorization': 'Bearer '+token}
                            }); 
                
                    instance.get("/auth/user/" ).then((res) => {
                        console.log(res.data)

                        this.$store.commit("setAuthUser",
                            {authUser: res.data, isAuthenticated: true}
                        )

                        this.$router.push("/dashboard/")

                    })
                    .catch((error) => {
                    console.log(error);
                    console.debug(error);
                    console.dir(error);
                    });

                }).catch((error)=>{
                 if (error.response && error.response.status === 401) {
                  this.error.email ="INVALID CREDENTIALS. PLEASE, TRY AGAIN LATER"
                    } else {
                    // Handle error however you want
                    }
                })

                
            // this.$store.dispatch({
            //     type:"obtainToken", payload :payload  })
        },

    },
   


}
</script>

<style scoped>
.ant {
    background: #273142; 
}
.card-header {
    height:70px;
    border-bottom: 2px solid #dbd7d779;

}

</style>
