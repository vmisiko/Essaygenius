<template>
    
            <v-layout id="curtain" > 
            
                <div class="card" >
                    <v-toolbar light>
                        <v-btn icon light @click="swapComponent('Chatlist')">
                             <v-icon>mdi-arrow-left</v-icon>

                        </v-btn>
                        
                        
                        <v-badge
                            
                            bottom
                            color="green"
                            dot
                            offset-x="10"
                            offset-y="10"
                        >
                            <v-avatar class="ml-5" size="30">
                            <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg" ></v-img>
                            </v-avatar>

                        </v-badge>
                        <v-list-item-content class="ml-3">
                                <v-list-item-title>Victor</v-list-item-title>
                                <v-list-item-subtitle>Online</v-list-item-subtitle>
                        </v-list-item-content>

                        
                        <v-btn icon class="" @click.prevent="chatclose"  light>  
                           <!-- <h2><span aria-hidden="true">&times;</span></h2>  -->
                           <v-icon >fa-times</v-icon>

                        </v-btn>

                                        

                    </v-toolbar>

                    <div class="card-body">
                         <div id="chat-body" >
                            <div class="mb-4 mx-3" >

                                    <div >
                                        <span class="ml-2 mb-1"> <b> victor: </b> </span> <br>
                                        <span class="rounded green white--text px-4 py-1"> hey bro </span>
                                    </div>

                                    <v-layout >
                                        <v-spacer></v-spacer>
                                        <span class="rounded grey lighten-3 black--text px-4 py-2"> yes whatsup? </span>                           
                                    </v-layout>
                                    
                            </div>
                            <div id="bottomOfArea"> </div>

                            </div> 
                            <v-divider></v-divider>  
                            <div></div>  	
                            <v-layout class="mx-4">
                                <v-text-field
                                    v-model="message"
                                    label="Type here to send"
                                    light
                                    clearable
                                    :append-outer-icon="message ? 'mdi-send' : 'mdi-microphone'"

                                ></v-text-field>
                            </v-layout>



                    </div>
                </div>

            </v-layout>
</template>

<script>
export default {
    name:"ChatComponent",
    props: ['swapComponent'],
    data () {
        return {
            message:"",
            chatstatus:true,
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
        }

        
    },
    mounted() {
        this.$root.$on('chatopen', () => {
            this.chatstatus =!this.chatstatus
            this.chatopen();
        })
    }    
}

</script>
<style lang="stylus" scoped>

</style>