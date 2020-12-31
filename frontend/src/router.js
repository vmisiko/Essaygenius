import Vue from "vue";
import Router from "vue-router";
import Index from "@/components/Index.vue";
import Dashboard from "@/views/Dashboard.vue";
import SignView from "@/views/SignView.vue";


Vue.use(Router);

const routes = [
  {
    path: "/",
    redirect: "/index"
  },
  {
    path: "/create",
    name: "create",
    component: () => import("@/modules/Orders/Create")
  },
  {
    path: "/edit",
    name: "edit",
    component: () => import("@/modules/Orders/Edit")
  },
  {
    path: "/index",
    name: "index",
    component: Index
  },
  {
    path: "/orderdetails",
    name: "orderdetails",
    component: () => import("@/modules/Orders/orderdetails.vue")
  },
  {
    path: "/instructions/",
    name: "instructions ",
    component: () => import("@/modules/Orders/Instructions.vue")
  },
  {
    path: "/instructions/:id",
    name: "instructionsid ",
    component: () => import("@/modules/Orders/Instructions.vue")
  },
  {
    path: "/uploads",
    name: "uploads",
    component: () => import("@/modules/Orders/Uploads.vue")
  },
  {
    path: "/uploads/:id",
    name: "uploadsid",
    component: () => import("@/modules/Orders/Uploads.vue")
  },
  {
    path: "/orderdetails/:id",
    name: "orderdetailsdraft",
    component: () => import("@/modules/Orders/orderdetailsdraft.vue")
  },
  {
    path: "/dashboard/",
    component: Dashboard,
    children: [
      {
        path: "",
        component: ()=> import("@/modules/Orders/Myorders")
      },

      {
        path: "myorders",
        component: () => import("@/modules/Orders/Myorders")
      },

      {
        path: "notifications",
        name: "notifications",
        component: () => import("@/modules/Notifications/Notifications")
      },
      {
        path: "settings",
        component: () => import("@/modules/Settings/Settings")
      },
      {
        path: "balance",
        name: "balance",
        component: () => import("@/modules/Balance/Balance")
      }
    ]
  },
  {
    path: "/auth/",
    component: SignView,
    children: [
      {
        path: "login",
        component: ()=> import("@/components/auth/Login")
      },
      {
        path: "register",
        component: ()=> import("@/components/auth/Signup")
      },
      {
        path: "forgot-password",
        component: ()=> import("@/components/auth/Forgotpassword")
      }
    ]
  }
];

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});
export default router;
