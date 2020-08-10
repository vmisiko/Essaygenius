<template>

    <v-row >

        <sidebar class="sidebar"> </sidebar> 

        <v-main class="mx-15 mt-5 main " >

            <h2> settings </h2>

            <div class="ant-card " style="height:250px;">
            <v-form ref="loginform" v-model="valid" lazy-validation>

                <div class="card-header ">
                    <h5 class="float-left"> Account </h5>

                    <div class="float-right">

                        <v-btn type="submit" class="primary" :disabled="!valid" @click="account_submit"> submit </v-btn>

                    </div>

                </div>

                <v-container>
                    <v-row>
                            <v-col
                            cols="12"
                            md="4"
                            >
                            <v-text-field
                            v-model="firstname"
                            :rules="nameRules"
                            :counter="20"
                            label="First name"
                            required
                            ></v-text-field>
                            </v-col>

                            <v-col
                            cols="12"
                            md="4"
                            >
                            <v-text-field
                            v-model="lastname"
                            :rules="nameRules"
                            :counter="20"
                            label="Last name"
                            required
                            ></v-text-field>
                            </v-col>

                            <v-col cols="12" md="4">

                                <v-dialog
                                    ref="dialog"
                                    v-model="modal"
                                    :return-value.sync="date"
                                    persistent
                                    width="290px"
                                    required
                                >
                                    <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                        v-model="date"
                                        label="Date of birth"
                                        readonly
                                        :rules="dateRules"
                                        v-bind="attrs"
                                        v-on="on"
                                    ></v-text-field>
                                    </template>
                                    <v-date-picker v-model="date" scrollable>
                                    <v-spacer></v-spacer>
                                    <v-btn text color="primary" @click="modal = false">Cancel</v-btn>
                                    <v-btn text color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
                                    </v-date-picker>
                                </v-dialog>
                                                        
                            </v-col>
                    </v-row>
                        
                </v-container>  

            </v-form>
               
                <div>


                </div>


            </div>

        <!-- email  -->
             <div class="ant-card mt-5" style="height:150px;">
                
                <div class="card-header">
                    <h5 class="float-left"> Email </h5>

                   


                </div>

                <v-row class="mx-5">

                    <v-col>
                        misikovictor123@gmail.com
                    </v-col>

                    <v-col>

                        <v-chip color="green" default>

                            Verified

                        </v-chip>


                    </v-col>

                    <v-col class="">
                        <div class="text-center float-right">
                            <v-dialog
                            v-model="emailmodal"
                            width="500"
                            >
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn
                                color="primary"
                                dark
                                v-bind="attrs"
                                v-on="on"
                                >
                                Change Email
                                </v-btn>
                            </template>

                            <v-card>

                                <v-form ref="emailchange" >

                                    <v-card-title class="headline ">
                                        Change Email
                                    </v-card-title>

                                    <v-card-text>
                                        <v-container>
                                            <v-text-field
                                                label="Enter Your password"
                                                :type="showPassword ? 'text':'password'"
                                                :append-icon="showPassword ? 'mdi-visibility-off' : 'mdi-visibility'"
                                                @click:append="showPassword = !showPassword"
                                                required
                                            ></v-text-field>

                                            <v-text-field
                                                v-model="email"
                                                :rules="emailRules"
                                                label="Enter new your Adress"
                                                required
                                            ></v-text-field>

                                        </v-container>
                                    </v-card-text>

                                    <v-divider></v-divider>

                                    <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        color="primary"
                                        text
                                        @click="emailmodal = false"
                                    >
                                        Cancel
                                    </v-btn>
                                    <v-btn
                                        color="primary"
                                        text
                                        @click="ChangeEmail"
                                    >
                                    Submit
                                    </v-btn>
                                    </v-card-actions>
                                </v-form>
                            </v-card>
                            </v-dialog>
                        </div>

                    </v-col>
                </v-row>

                


            </div>
         <!-- email  -->




            <!-- phone number   -->

             <div class="ant-card mt-5 mb-5" style="height:250px;">
                
                <div class="card-header">
                    <h5 class="float-left"> Phone Number </h5>

                    <div class="text-center float-right">
                        <v-dialog
                        v-model="dialog"
                        width="500"
                        >
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                            color="primary"
                            dark
                            v-bind="attrs"
                            v-on="on"
                            >
                            Add Phone Number
                            </v-btn>
                        </template>

                        <v-card>

                            <v-form ref="Add_Phone" lazy-validation>
              
                                <v-card-title class="headline ">
                                Add Phone number
                                </v-card-title>

                                <v-card-text>
                                    <v-container>
                                        <vue-tel-input-vuetify
                                         v-model="phone" required
                                         @input="validatephone"
                                         ></vue-tel-input-vuetify>


                                    </v-container>
                                </v-card-text>

                                <v-divider></v-divider>

                                <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    color="primary"
                                    text
                                    @click="dialog = false"
                                >
                                    Cancel
                                </v-btn>
                                <v-btn
                                    color="primary"

                                    text
                                    @click="PhoneChange"
                                >
                                Submit
                                </v-btn>
                                </v-card-actions>
                            </v-form>
                        </v-card>
                        </v-dialog>
                    </div>

                </div >

                    <div class="text-center mt-5 ">
                        
                     <i class="fas fa-phone fa-5x mb-4"></i>
                    <h6> You do not have any phone numbers</h6>
                     <p>Please add any phone numbers to project your profile.</p>
                

                    </div>

                <div>


                </div>


                
                

            </div>

            <!-- phone number   -->
            


        </v-main>
        

    </v-row>
    
</template>

<script>
import NavigationDrawer from "../components/NavigationDrawer"

export default  {
    name:"Settings",

    components:{
        sidebar: NavigationDrawer, 
    },

    data () {
        return {
            valid:true,
            msg :"hey message",
            modal: false,
            emailmodal:false,
            dialog:false, 
            firstname:"",
            lastname:"",
            date: "",
            email:'',
            password: "",
            phone: "",
            showPassword :false,


            nameRules: [
                v => !!v || 'Name is required',
                v => v.length <= 10 || 'Name must be less than 10 characters',
            ],

            dateRules: [
                v => !!v || 'Date is required',
            ],
            emailRules : [
                v=> !!v || "Email is required",
                v => /.+@.+/.test(v) || 'E-mail must be valid',
            
            ],
        }
    },
     methods: {
        account_submit () {
            // alert("clicked");
            if (this.$refs.loginform.validate()) {
                //  console.log(this.$refs.loginform);


            }

        },
        ChangeEmail () {
            if (this.$refs.emailchange.validate()) {
                alert("verlidated");

            }
        },
        PhoneChange () {
            if (this.$refs.Add_Phone.validate()) {
                alert("phone validated")
            }
        },
        // validatephone (formattedNumber, { number, valid, country }) {
        //     console.log(number.international, valid, country.name )
       
        // },


    },
    computed: {

        
    },

    
    
}
</script>

<style  scoped>

.card-header {
    background:#232c3b;
    height:70px;
    border: 2px solid #273142;
    border-radius: 4px;

}

.icon {
   width: 70px;
   text-align: left;
}

.sidebar {
    position:fixed;
}

.main {
    height:600px;
    overflow-y:scroll;
    
}

.main::-webkit-scrollbar {
  display: none;
}


</style>