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
            background2: "#fff",
            link: '#000',
            night: "#7377af",
            day: "#ffe85d"
          },
          dark: {
            primary: '#101026',
            secondary: '#56531b',
            background: "#101026",
            accent:'#ddcc46',
            error: '#dd1e00',
            background2: "#000",
            link: '#fff',
          },

        },
      },
});
