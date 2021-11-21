import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({

    theme: {
      options: { customProperties: true },
        themes: {
          light: {
            primary: "#78909c",

            secondary: "#00bfa5",
            accent: "#00bfa5",
            error: colors.red,
            background: '#eceff1',
            link: '#000'
          },
          dark: {
            primary: '#49190d',
            secondary: '#56531b',
            background: "#49190d",
            accent:'#ddcc46',
            error: '#dd1e00',
            link: '#fff',
          },
        },
      },
});
