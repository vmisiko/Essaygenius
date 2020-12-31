<template>
     <v-card color="#273142" >

                    <v-card-title color="#dbd7d779" >
                       <h3 class="mx-auto"> Login </h3> 
                    </v-card-title>
                    <v-divider class="mt-n1"></v-divider>
                    <v-form             
                        ref="form"
                        v-model="valid"
                        lazy-validation
                    >
                    <v-card-text class="card-body">

                            <v-text-field
                            v-model="email"
                            label="Email"
                            :rules ="emailRules"
                            :loading="loading"
                            :error-messages="error.email"
                            required
                            ></v-text-field>

                            <v-text-field
                            v-model="password"
                            label="Password"
                            :rules="passwordRules"
                            required
                            :loading="loading"
                            :error-messages="error.password"
                            :type="show? 'text' : 'password'"
                            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                            @click:append="show=!show"
                            ></v-text-field>
                    </v-card-text>
                    <v-card-actions >
                        <v-btn class="ml-3" width="30%" :disabled="!valid" shaped color="success" type="submit" :loading="loading" @click.prevent="login">
                            Login
                        </v-btn>

                        <v-col>
                             <router-link to="/auth/forgot-password"  style="cursor:pointer;"> Forgot Password?</router-link> <br>
                             <router-link to="/auth/register"  style="cursor:pointer;"> Create new Account</router-link>
                        </v-col>
                        
                    </v-card-actions>
                        
                </v-form>
            
    </v-card>

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
            emailRules: [
                (v) => !!v || "Email is required",
                (v) => /.+@.+/.test(v) || 'E-mail must be valid',
            ],
            password:"",
            passwordRules: [
                (v) => !!v || "password is required",
            ],
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
