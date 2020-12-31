<template>
     <v-card color="#273142" >

                    <v-card-title color="#dbd7d779">
                       <h3 class="mx-auto"> Forgot Password </h3> 
                    </v-card-title>
                    <v-divider class="mt-n1"></v-divider>
                <v-form v-model='valid'>
                    <v-card-text >
                        
                            <v-text-field
                            v-model="Email"
                            label="Email"
                            :rules="emailRules"
                            required
                            prepend-icon="mdi-email"

                            ></v-text-field>

                            <p>
                                Enter the email address associated with your account, and we’ll email you a link to reset your password.
                            </p>

                    </v-card-text>

                    <v-card-actions class="text-center mb-5" >
                        <v-spacer> </v-spacer>
                        <v-btn :disabled="!valid" round color="primary" class="mb-5"> Send Reset Link </v-btn>
                        <v-spacer> </v-spacer>
                    </v-card-actions>
                </v-form>
           
     </v-card>

</template>

<script>
import validationMxn from '@/mixins/validation_mixin'

export default {
    name:"Login",
    mixins: [validationMxn],
    data () {
        return {
            show:true,
            valid: false,
        }
    }

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
