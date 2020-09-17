<template>
     <div class="ant-card ">

                    <div class="card-header text-center">
                       <h3 >Sign Up For Free</h3> 
                    </div>
                    <v-divider class="mt-n1"></v-divider>

                    <div class="card-body">
                        {{response}}
                        
                        <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                        @submit.prevent="signup"
                        >
                            <v-text-field
                            v-model="email"
                            label="Email"
                            :loading="loading"
                            required
                            :error-messages="error.email"
                            ></v-text-field>

                            <v-text-field
                            v-model="password"
                            label="Password"
                            :loading="loading"
                            required
                            :type="show? 'text' : 'password'"
                            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                            @click:append="show=!show"
                            ></v-text-field>

                        <v-row>
                            <v-col>
                                <v-btn shaped color="success" type="submit" :loading="loading">
                                    Create Account
                                </v-btn>

                            </v-col>

                            <v-col class="ml-10">
                                 <router-link to="/auth/login" tag='div' style="cursor:pointer;" class="caption">Already <br> Registered?</router-link>
                            </v-col>

                        </v-row>
                        
                    </v-form>


                    </div>

            
    </div>

</template>

<script>
// import api from "../api"
import axios from "axios"

export default {
    name:"SignUp",
    data () {
        return {
            show:false,
            valid:false,
            password:"",
            email:"",
            response:"",
            loading:false,
            error:{}
            
        }
    },
    methods: {
        signup () {
           
            const data ={
                email:this.email,
                password: this.password,
                password2:this.password,
            }
            
            axios.post("http://localhost:8000/auth/signup/",
                 data).then((res)=> {
                     this.loading =!this.loading
                     console.log(res.data)
                     this.error= res.data
                    console.log(this.error)
                     if(res.data.response) {
                         this.$router.push("/auth/login/")
                     }
                     if(res.data.errors) {
                         console.log(res.data.errors)
                         this.error = res.data.errors
                         this.loading = !this.loading
                     }


                 }).catch((error)=>{
                     console.log(error)

                 })

        }

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
