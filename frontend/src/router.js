import Vue from "vue";
import Router from "vue-router";
import Edit from "./components/Edit.vue"
import Create from "./components/Create.vue"
import Index from "./components/Index.vue"
import orderdetails from "./components/orderdetails"
import Instructions from "./components/Instructions"
import Uploads from "./components/Uploads"
import orderdetailsdraft from "./components/orderdetailsdraft"
import Dashboard from "./views/Dashboard"
import Notifications from "./views/Notifications"
import Settings from "./views/Settings"
import Balance from "./views/Balance"
import Myorders from "./views/Myorders"
import SignView from "./views/SignView"
import Login from "./components/Login"
import Signup from "./components/Signup"
import Forgotpassword from "./components/Forgotpassword"



Vue.use(Router);


export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
      path: "/create",
      name: "create",
      component: Create
    },
    {
      path: "/edit",
      name: "edit",
      component:Edit
    },
    {
      path: "/index",
      name: "index",
      component: Index
    },
    {
      path: "/orderdetails",
      name: "orderdetails",
      component: orderdetails
    },
    {
      path: "/instructions/",
      name: "instructions ",
      component: Instructions
    },
    {
      path: "/instructions/:id",
      name: "instructionsid ",
      component: Instructions
    },
    {
      path:"/uploads",
      name:"uploads",
      component: Uploads
    },
    {
      path:"/uploads/:id",
      name:"uploadsid",
      component: Uploads
    },
    {
      path: "/orderdetails/:id",
      name: "orderdetailsdraft",
      component: orderdetailsdraft
    },
    {
      path:"/dashboard/",
      component:Dashboard,
      children: [
        {
          path:'',
          component: Myorders
        },
        
        {
          path:'myorders',
          component: Myorders
        },

        {
          path:'notifications',
          component: Notifications
        },
        {
          path:'settings',
          component:Settings
    
        },
        {
          path:"balance",
          name:"balance",
          component:Balance
        },
     
      ],
    },
    {
      path:"/auth/",
      component:SignView,
      children:[
        {
         path:"login",
        component:Login,
        },
        {
          path:"register",
          component:Signup
        },
       {
         path:"forgot-password",
         component:Forgotpassword

       }

      ]
    },
    
  ]
});

