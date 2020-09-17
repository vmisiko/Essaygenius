<template>
     <div class="ant-card ">

                    <div class="card-header text-center">
                       <h3 > Forgot Password </h3> 
                    </div>
                    <v-divider class="mt-n1"></v-divider>

                    <div class="card-body">
                        
                        <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                        >
                            <v-text-field
                            v-model="Email"
                            label="Email"
                            required
                            prepend-icon="mdi-email"

                            ></v-text-field>

                            <p>
                                Enter the email address associated with your account, and we’ll email you a link to reset your password.
                            </p>

                           

                        </v-form>

                    </div>

                    <div class="card-footer text-center">
                         
                         <v-btn round color="primary"> Send Reset Link </v-btn>

                    </div>

            
    </div>

</template>

<script>
export default {
    name:"Login",
    data () {
        return {
            show:true,
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
