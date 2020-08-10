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
      name:"dashboard",
      component: Dashboard
    },
    {
      path:'/notifications/',
      name:"notifications",
      component: Notifications
    },
    {
      path:'/settings/',
      name:"settings",
      component:Settings

    },
    {
      path:"/balance/",
      name:"balance",
      component:Balance
    }
    
  ]
});

