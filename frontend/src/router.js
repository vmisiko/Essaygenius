import Vue from "vue";
import Router from "vue-router";
import Index from "@/components/Index.vue"
import Myorders from '@/views/Myorders';
import Dashboard from "@/views/Dashboard.vue"
import Settings from "@/views/Settings.vue"
import Balance from "@/views/Balance.vue"
import SignView from "@/views/SignView.vue"
import Login from "@/components/auth/Login.vue"
import Signup from "@/components/auth/Signup.vue"
import Forgotpassword from "@/components/auth/Forgotpassword.vue"

Vue.use(Router);

const routes = [
    {
      path: "/",
      redirect: '/index'
    },
    {
      path: "/create",
      name: "create",
      component: Myorders,
      // component: { 
      //   Create: () => import('@/modules/Orders/Create')
      //  },
    },
    {
      path: "/edit",
      name: "edit",
      component: Myorders,
      // component:{
      //   Edit: () => import('@/modules/Orders/Edit')
      // }
    },
    {
      path: "/index",
      name: "index",
      component: Index
    },
    {
      path: "/orderdetails",
      name: "orderdetails",
      component: {
        orderdetails: () => import('@/modules/Orders/orderdetails.vue')
      }
    },
    {
      path: "/instructions/",
      name: "instructions ",
      component: {
        Instructions: () => import('@/modules/Orders/Instructions.vue')
      }
    },
    {
      path: "/instructions/:id",
      name: "instructionsid ",
      component:{ 
        Instructions: () => import('@/modules/Orders/Instructions.vue')
      }
    },
    {
      path:"/uploads",
      name:"uploads",
      component: {
        Uploads: ()=> import('@/modules/Orders/Uploads.vue')
      }
    },
    {
      path:"/uploads/:id",
      name:"uploadsid",
      component: {
        Uploads: ()=> import('@/modules/Orders/Uploads.vue')
      }
    },
    {
      path: "/orderdetails/:id",
      name: "orderdetailsdraft",
      component: {
        orderdetailsdraft: () =>  import('@/modules/Orders/orderdetailsdraft.vue')
      }
    },
    {
      path:"/dashboard/",
      component:Dashboard,
      children: [
        {
          path:'',
          component: {
            Myorders: () => import('@/views/Myorders')
          }
        },
        
        {
          path:'myorders',
          component: {
             Myorders: () => import('@/views/Myorders')
          }
        },

        {
          path:'notifications',
          name: 'notifications',
          component: {
            Notifications: () => import('@/modules/Notifications/Notifications'),
          }
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

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
export default router

