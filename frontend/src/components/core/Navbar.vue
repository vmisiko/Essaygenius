<template>
<div>
  <b-navbar toggleable="lg" type="light" variant="info">
    <b-navbar-brand> <router-link to = "/" ><img src="" style="width:100px; height:50px;" ></router-link>
</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>

        <b-nav-item  > <router-link to ="/index" > <p class= "nav-color"> Index</p>  </router-link></b-nav-item>
        <b-nav-item  > <router-link to ="/edit" > <p class= "nav-color"> Edit</p>  </router-link></b-nav-item>
        <b-nav-item  > <router-link to ="/create" > <p class= "nav-color"> create</p>  </router-link></b-nav-item>
      </b-navbar-nav>

      
    </b-collapse>
  </b-navbar>
</div>
    
</template>

<script>
export default {
    name:"Navbar"
}
</script>

<style scooped>
.nav-color{
  text-decoration: none;
  color:white
}


.nav-color:link {
  color: red;
}

/* visited link */
.nav-color:visited {
  color: green;
}

/* mouse over link */
.nav-color:hover {
  color:purple;
}

/* selected link */
.nav-color:active {
  color: blue;
}
</style>