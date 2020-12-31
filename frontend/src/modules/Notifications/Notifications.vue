<template>


        <v-main class="" >

            <h2> Notifications </h2>

            <div class="ant-card " style="height:400px;">
            
                    <PlaceHolder
                    :src = "require('@/assets/img/svg/no-notifications.svg')"
                    title=" Your do not have any notifications"
                    text =" Please complete any action such as placing an order, editing an order, hiring a writer, etc., to receive new notifications"
                    />


            </div>

 
            


        </v-main>
        
    
</template>

<script>
import PlaceHolder from "@/components/core/PlaceHolder"

export default  {
    name:"Notifications",
    components:{
        PlaceHolder: PlaceHolder,
    },
    data () {
        return {
            msg :"hey message",
           

        }
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


</style>