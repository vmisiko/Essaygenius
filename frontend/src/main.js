import Vue from 'vue'
import App from './App.vue'
import router from "./router"
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import  Datetime  from 'vue-datetime'
import 'vue-datetime/dist/vue-datetime.css'

Vue.use(Datetime)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify';
import VueTelInputVuetify from 'vue-tel-input-vuetify/lib';
import store from './store/store.js'
import api from "./api.js";


 
Vue.use(VueTelInputVuetify, {
  vuetify,
});

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.config.productionTip = false

Vue.prototype.$http = api; 
api.defaults.timeout = 10000;


new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
