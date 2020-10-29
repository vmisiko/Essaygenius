<template>
  <v-card
    height="100vh"
    width="256"
    class="overflow-hidden "
    style="position: relative;"

  >
    <v-navigation-drawer
     :color="ant"
     permanent
     absolute
     class="ml-3"
     >
     
      <v-list-item>
        <v-list-item-content>
      

            <v-img
              :src="require('../assets/img/Genius.jpeg')"
              alt="Essay Genius"
            />
        </v-list-item-content>
      </v-list-item>
    

    <router-link to="/orderdetails/" tag='div'>

        <v-list-item dense nav link >
            <v-list-item-icon>
                <!-- <v-icon>plus-circle</v-icon> -->
                <i class="fas fa-plus-circle fa-2x"></i>
            </v-list-item-icon>

            <v-list-item-content>
                <v-list-item-title>Place Order</v-list-item-title>
            </v-list-item-content>
        </v-list-item>

    </router-link>


      <v-divider></v-divider>

   
    <router-link to="/dashboard/balance/" tag='div'>
      <v-list dense nav>

        <v-list-item link >
          <v-list-item-icon>
            <v-icon> mdi-credit-card </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title> Balance </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </router-link>

    <router-link to="/dashboard/notifications/" tag='div'>
        <v-list dense nav>

                <v-list-item link >
                <v-list-item-icon>
                    <v-icon> mdi-bell </v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title> Notifications </v-list-item-title>
                </v-list-item-content>
                </v-list-item>
        </v-list>

    </router-link> 

    <router-link to="/dashboard/settings/" tag='div'>

        <v-list dense nav>

            <v-list-item link >
                <v-list-item-icon>
                    <v-icon> mdi-tools </v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title> Settings </v-list-item-title>
                </v-list-item-content>
            </v-list-item>
       </v-list>

    </router-link>

      <v-divider> </v-divider>

    <router-link to="/dashboard/myorders" tag='div'>

      <v-list dense nav>

        <v-list-item link dense >
          <v-list-item-icon>
            <v-icon> mdi-pencil </v-icon>
            <!-- <i class="far fa-edit"></i> -->
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title> My Orders </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </router-link>


      <v-list dense nav @click.native="chatopen">

        <v-list-item link >
          <v-list-item-icon>
            <v-icon> mdi-view-dashboard </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title> Chat </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      
    <template v-slot:append>
      <v-list dense nav>
        <v-divider></v-divider>
          <v-list-item link  @click="logout" >
            <v-list-item-icon>
              <v-icon right dark>mdi-logout</v-icon>
              <!-- <i class="far fa-edit"></i> -->
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title> Logout </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
      </v-list>
       
      </template>

    </v-navigation-drawer>
  </v-card>
</template>

<script>
import router from "../router"
import store from "../store/store"
  export default {
    name:"NavigationDrawer",
    data () {
      return {
        items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard' },
          { title: 'Photos', icon: 'mdi-image' },
          { title: 'About', icon: 'mdi-help-box' },
        ],
        right: null,
        ant:"#273142",
      }
    },
    methods:{
      chatopen: function(){
        console.log("clicked")
        this.$root.$emit('chatopen') //like this
      },
      logout: ()=> {
        console.log(store.state.authuser, "this is auth user before")
        store.commit("removeToken")
        console.log(store.state.authuser, "this is auth user")
        router.push("/auth/login")
      }

    },
     mounted(){
        console.log(store.state.jwt, store.state.isAuthenticated)
    }
  }
</script>

<style scoped>
.ant {
    background: #273142; 
}

a  {
    text-decoration: none;
}
</style>