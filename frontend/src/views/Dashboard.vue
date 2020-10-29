<template>

    <v-row >

        <sidebar class="sidebar"> </sidebar> 

        <v-main class="main-wrap">
            <!-- <Myorders/> -->

            
            <div class="main backdrop mx-15 mt-5">
                <router-view/>
            </div>

            <div :is="currentComponent" :swap-component="swapComponent"></div>
       



        </v-main>
        
    </v-row>
    
</template>

<script>
import NavigationDrawer from "../components/NavigationDrawer"
import ChatComponent from "./ChatComponent"
import Chatlist from "./Chatlist"
export default  {
    name:"Dashboard",
    components:{
        sidebar: NavigationDrawer,
        "ChatComponent":ChatComponent,
        "Chatlist":Chatlist,
    },
    data () {
        return {
            msg :"hey message",
            chatstatus:true,
            currentComponent: 'Chatlist'
        }
    },
    methods:{
        chatopen (){

                if( this.chatstatus){
                document.getElementById("curtain").style.display = "none"
                } else {
                document.getElementById("curtain").style.display = "block"

                }
        },
        chatclose (){

            this.chatstatus =!this.chatstatus
            document.getElementById("curtain").style.display = "none"

        },
        swapComponent: function(component) {
         this.currentComponent = component;
        }

    },
  
    


    
    
}
</script>

<style  scoped>

.main-wrap {
    position: relative;
}



.backdrop {
position: fixed;
} 

#curtain {
    display: block;
    height: 100vh;
    width: 370px;
    min-width: 370px;
    background-color:#ffff;
    position: absolute;
    z-index: 9999;
    top: 0px; 
    right: 0px;
    color:black;
}
    

/* .card-header {
    background:#232c3b;
    height:70px;
    border: 2px solid #273142;
    border-radius: 4px;
} */

.icon {
   width: 70px;
   text-align: left;
}
.Field {
   width: 100%;
   text-align: left;
   font-size: 20px;
   font-weight: 500;
   border:2px solid #a2a3a5;
   border-radius: 4px;
}

.inputContainer i {
   position: absolute;
}

</style>