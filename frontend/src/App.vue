<template>
  <v-app v-bind:style="{ background: $vuetify.theme.themes.dark.background}">
   

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style >



.ant-card {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    color: #fafafd;
    font-size: 14px;
    font-variant: tabular-nums;
    line-height: 1.5715;
    list-style: none;
    font-feature-settings: "tnum";
    position: relative;
    background: #273142; 
    border-radius: 4px;
    transition: all .3s;
}
.sidebar {
    position:fixed;
}

.main {
    height:100vh;
    overflow-y:scroll;
    
}

.main::-webkit-scrollbar {
  display: none;
}

.main-wrap {
    position: relative;
}



.backdrop {
position: fixed;
} 

#curtain {
    display: block;
    height: 100vh;
    width: 300px;
    min-width: 370px;
    background-color:#ffff;
    position: absolute;
    z-index: 9999;
    top: 0px; 
    right: 0px;
    color:black;
}
#chat-body{
height:350px;
overflow-y:scroll;
}

#chat-body::-webkit-scrollbar {
     display:none
 }
 .ant {
    background: #273142; 
}
    


</style>
