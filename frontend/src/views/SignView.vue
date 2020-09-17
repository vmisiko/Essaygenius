<template>


    <div>
        <v-toolbar color="#273142" dense>
            <v-list-item>
            <v-toolbar-title class="">Essay Genius</v-toolbar-title>
            
            </v-list-item>
            <v-spacer></v-spacer>

            <router-link to="/auth/login"><v-btn rounded  class="my-3" color="#273142" > Login </v-btn></router-link>
            <router-link to="/auth/register"><v-btn rounded class="ml-3 my-3" color="#f19d59" > Signup </v-btn></router-link>
    
        </v-toolbar>

        <v-container>
            <div class="mt-5 col-md-4 mx-auto">

                <router-view></router-view>

            </div>
           
        </v-container>


    </div>
    
</template>

<script>

export default {
    name:"SignView",
    data () {
        return {
            show:true,

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