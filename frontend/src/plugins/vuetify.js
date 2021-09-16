import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          light: {
            primary: "#78909c",

            secondary: "#3f51b5",
            accent: "#3f51b5",
            error: colors.red,
            background: '#eceff1'
          },
          dark: {
            primary: colors.blue.lighten3,
          },
        },
      },
});
