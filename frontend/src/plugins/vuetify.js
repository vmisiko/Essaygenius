import Vue from 'vue';
import Vuetify from 'vuetify/lib';
// import colors from 'vuetify/lib/util/colors';



Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        options: {
            customProperties: true,
          },
        dark: true,
        themes: {
          dark: {
            background:"#1f2735",
        
          }
        },
        anycolor:"#1f2735",
      }
});
