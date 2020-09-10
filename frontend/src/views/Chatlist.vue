<template>
    
            <div id="curtain"> 
                <div class="card">
                    <div class="card-header">

                        <h3 class="float-left">Chats</h3>
                       
                        <v-btn icon class="float-right" @click.prevent="chatclose"  light>  
                           <!-- <h2><span aria-hidden="true">&times;</span></h2>  -->
                           <v-icon >fa-times</v-icon>

                        </v-btn>
                                     

                    </div>

                    <div class="card-body">
                        <div id="chat-body"  >
                            <v-list two-line light dense @click.native="swapComponent('ChatComponent')">
                                <template v-for="(item,index) in items" >

                                    
                                    <v-list-item 
                                    :key="index"
                                    link>

                                        <v-list-item-avatar>
                                            <v-img :src="item.avatar"></v-img>
                                        </v-list-item-avatar>

                                        <v-list-item-content>
                                                <v-list-item-title v-html="item.title"></v-list-item-title>
                                                <v-list-item-subtitle v-text="item.subtitle"></v-list-item-subtitle>
                                        </v-list-item-content>

                                        <v-list-item-icon>
                                                <v-icon color='primary' x-small>mdi-greater-than</v-icon>
                                        </v-list-item-icon>
                                        
                                    </v-list-item>

                                </template>


                            </v-list>
                        </div>
                    </div>

                </div>

            </div>
</template>

<script>
export default {
    name:"Chatlist",
    props: ['swapComponent'],
    data () {
        return {
            message:"",
            chatstatus:true,
            items:[
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' ,
                    title: 'Ali Connors .11h Ago',
                    subtitle:"I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' ,
                    title: 'Ali Connors .11h Ago',
                    subtitle:"I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' ,
                    title: 'Ali Connors .11h Ago',
                    subtitle:"I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' ,
                    title: 'Ali Connors .11h Ago',
                    subtitle:"I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
            ],
            
            
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
<style scoped>



</style>