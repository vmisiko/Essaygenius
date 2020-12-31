<template>
    
            <div id="curtain" height="100vh"> 
            
                <v-card flat height="100%"  light>
                    <v-toolbar >
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
                                <v-list-item-title>{{loggedInUser.email}}</v-list-item-title>
                                <v-list-item-subtitle>Online</v-list-item-subtitle>
                        </v-list-item-content>

                        
                        <v-btn icon class="mr-5" @click.prevent="chatclose"  light>  
                           <v-icon >fa-times</v-icon>

                        </v-btn>

                                        

                    </v-toolbar>

                    <v-card-text id="chat-body" >
                             <div v-if="noMessages" class="mt-5 mx-3 text-center">
                                No messages yet
                            </div>

                            <div class="mb-4 mx-3" v-else>
                                
                                <div  class="mb-4 mx-3" v-for="(message,index) in messages" :key="index" >
                                     <div v-if="chatUsersMap[message.sender] !== loggedInUser.email">
                                        <span class="ml-2 mb-1"> <b> {{ chatUsersMap[message.sender] }}: </b> </span> <br>
                                        <span class="rounded green white--text px-4 py-1"> {{ message.text }} </span>
                                    </div>

                                     <v-layout v-else>
                                        <v-spacer></v-spacer>   
                                        <span class="rounded grey lighten-3 black--text px-4 py-2"> {{ message.text }} </span>                           
                                    </v-layout>
                                </div>
                                    
                                    
                            </div>
                            
                            <div id="bottomOfArea"> </div>
                    </v-card-text>
                     <v-divider></v-divider>  
                    <v-card-actions class="footer">
                     <v-text-field
                        v-model="message"
                        label="Type here to send"
                        light
                        clearable
                        v-on:keyup.enter="send"
                        :append-outer-icon="message ? 'mdi-send' : 'mdi-microphone'"
                        ></v-text-field>
                    </v-card-actions>

                </v-card>

            </div>
</template>

<script>
import axios from "axios"
export default {
    name:"ChatComponent",
    props: ['swapComponent'],
    data () {
        return {
            chatstatus:true,
            onlineUsers: "",
            loggedInUser: {},
            selectedUser: {},
            chatUsersMap: {},          
            chatSocket: null,
            message: '',
            messages: [],
            noMessages: true
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
        getChatToken(){
            return (this.loggedInUser.id < this.selectedUser.id) ? ( this.loggedInUser.id+ "_" + this.selectedUser.id ) : this.selectedUser.id + "_" + this.loggedInUser.id   
          },
        recieveMessage (message) {
              this.noMessages = false
              this.messages.push(message)
              setTimeout(() => {document.getElementById("bottomOfArea").scrollIntoView({ block: 'end',  behavior: 'smooth' }) }, 0)    
          },
        send() {
            this.chatSocket.send(JSON.stringify({
                'message': this.message,
                'sender': this.loggedInUser,
                'receiver': this.selectedUser,
            }));

            this.message = ''            
        }       
        
    },
    created(){
        var senderid = 1
        this.$root.$on("passChat", (value) => {
            senderid= value
            console.log("event reieved", senderid)


        })
        const instance =axios.create({
            baseURL: "http://localhost:8000/",
            headers: {'Authorization': 'Bearer '+this.$store.state.jwt}
        }); 

        instance.get(`/messageAPI/message/${senderid}/`).then((res) => {
            // console.log(res.data)
            this.loggedInUser= res.data.current_user
            this.selectedUser = res.data.selected_user
            this.messages = res.data.messages
            this.noMessages = false
            this.chatUsersMap[this.loggedInUser.id] = this.loggedInUser.email
            this.chatUsersMap[this.selectedUser.id] = this.selectedUser.email	

            console.log(this.messages)
            console.log(this.chatUsersMap)
            this.chatSocket = new WebSocket('ws://localhost:8000' + '/ws/chat/' + this.getChatToken() + '/')

            this.chatSocket.onmessage = (m) => {
                console.log(m.data)
                let message = {
                    sender: JSON.parse(m.data).sender.id,
                    text: JSON.parse(m.data).message
                    }
                this.recieveMessage(message)
            }

        }).catch((error)=>{
            console.log(error)
        })
    },

    updated(){     
        var elem = document.getElementById("bottomOfArea");
        elem.scrollIntoView({behavior: "smooth", block: "end"});
    },
    mounted() {
        this.$root.$on('chatopen', () => {
            this.chatstatus =!this.chatstatus
            this.chatopen();
        })
    }    
}

</script>
<style scoped>
.footer.v-card-actions {
    position: fixed;
    bottom:0;
}

</style>