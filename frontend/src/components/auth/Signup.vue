<template>
  <v-card :color="ant">
    <v-card-title :color="cardheader">
      <h3 class="mx-auto">Registration</h3>
    </v-card-title>
    <v-divider class="mt-n1"></v-divider>
    <v-form ref="form" v-model="valid" lazy-validation @submit.prevent="signup">
      <v-card-text>
        {{ response }}
        <v-text-field
          v-model="email"
          label="Email"
          :loading="loading"
          :rules="emailRules"
          required
          :error-messages="error.email"
        ></v-text-field>

        <v-text-field
          v-model="password"
          label="Password"
          :loading="loading"
          :rules="passwordRules"
          required
          :type="show ? 'text' : 'password'"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show = !show"
        ></v-text-field>
      </v-card-text>
      <v-card-actions no-gutters>
        <v-btn
          :disabled="!valid"
          shaped
          color="success"
          type="submit"
          :loading="loading"
        >
          Create Account
        </v-btn>

        <v-col class="ml-5 caption" style="cursor:pointer;">
          <span>Already Registered? </span>
          <router-link to="/auth/login" class="text-decoration-underline ">
            Login
          </router-link>
        </v-col>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
// import api from "../api"
import axios from "axios";
import generalMxn from "@/mixins/general_mixin";
import validationMxn from "@/mixins/validation_mixin";

export default {
  name: "SignUp",
  mixins: [generalMxn, validationMxn],
  data() {
    return {
      show: false,
      valid: false,
      password: "",
      email: "",
      response: "",
      loading: false,
      error: {}
    };
  },
  methods: {
    signup() {
      const data = {
        email: this.email,
        password: this.password,
        password2: this.password
      };

      axios
        .post("http://localhost:8000/auth/signup/", data)
        .then(res => {
          this.loading = !this.loading;
          console.log(res.data);
          this.error = res.data;
          console.log(this.error);
          if (res.data.response) {
            this.$router.push("/auth/login/");
          }
          if (res.data.errors) {
            console.log(res.data.errors);
            this.error = res.data.errors;
            this.loading = !this.loading;
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
.ant {
  background: #273142;
}
.card-header {
  height: 70px;
  border-bottom: 2px solid #dbd7d779;
}
</style>
