<template>
  <v-app
    class="font"
    
  >
    <div id="app">
      <div class="wrapper" :style="{ background: $vuetify.theme.themes[theme].background }">
        <navbar-comp v-bind:setShowSideMenu="navigationDrawer" />
        <router-view />

        <v-navigation-drawer v-model="showSideMenu" absolute temporary>
          <v-list nav dense>
            <v-list-item-group
              v-model="group"
              active-class="secondary text--accent-4"
            >
              <router-link :to="{ name: routes.mainPage }">
                <v-list-item>
                  <v-list-item-title>
                    <svg src="@/assets/logo.png" class="logo" />
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.projects }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>grid_view</v-icon>
                    {{ getString("navbar", "projects") }}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.groups }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>groups</v-icon>
                    {{ getString("navbar", "groups") }}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.addProject }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>add</v-icon>
                    {{ getString("navbar", "addProject") }}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.settings }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>settings</v-icon>
                    {{ getString("navbar", "settings") }}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.user }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>person</v-icon>
                    {{ getString("navbar", "user") }}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.admin }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>rules</v-icon>
                    {{ getString("navbar", "admin") }}
                  </v-list-item-title>
                </v-list-item>
              </router-link>
     </v-list-item-group>

             <div>
      <v-tooltip v-if="!$vuetify.theme.dark" bottom>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" color="info" small fab @click="darkMode">
            <v-icon class="mr-1">mdi-moon-waxing-crescent</v-icon>
          </v-btn>
        </template>
        <span>Dark Mode On</span>
      </v-tooltip>

      <v-tooltip v-else bottom>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" color="info" small fab @click="darkMode">
            <v-icon color="yellow">mdi-white-balance-sunny</v-icon>
          </v-btn>
        </template>
        <span>Dark Mode Off</span>
      </v-tooltip>
    </div>

          </v-list>
        </v-navigation-drawer>
        <div class="push"></div>
      </div>
      <div class="footer"> <Footer /></div>
     
    </div>
  </v-app>
</template>

<script>
import NavbarComp from "@/components/navbar_footer/Navbar.vue";
import { apiService } from "@/common/api.service.js";
import Footer from "./components/navbar_footer/Footer.vue";
import { getString } from "@/language/string.js";

export default {
  name: "App",
  components: {
    NavbarComp,
    Footer,
  },
  data() {
    return {
      showSideMenu: false,
      group: "",
      themeChange: true,
      routes: {
        addProject: "projectNew",
        projects: "projects",
        groups: "groups",
        mainPage: "main",
        settings: "main",
        user: "main",
        admin: "admin",
      },
    };
  },
  methods: {
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
    getString,
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
      this.$vuetify.theme.dark = true;
    },
    setShowSideMenu() {
      this.showSideMenu = false;
      this.showSideMenu = true;
    },
    navigationDrawer() {
      this.showSideMenu = !this.showSideMenu;
    },
  },
  created() {
    this.setUserInfo();
  },

  watch: {
    group() {
      this.showSideMenu = !this.showSideMenu;
    },
  },
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

.v-application {
  font-family: "playfair display";
  font-weight: 500;
  /* background-color: #f2f6fa; */
  color: #fff;
  
  /* border:solid white; */
  display: flex;
  height: 100vh;
  margin: 0;
  flex-direction: column;
}

body{
  height: 100vh;
}

#app{
  
/* display: flex; */
  /* flex-direction: column; */
  
  border: white;
}
.v-btn {
  cursor: pointer;
}

.wrapper {
  min-height: 100vh;
  margin-bottom: -100px;
  /* border:solid white; */
}


.footer, .push{
  height: 50px;
  margin-top: auto;
}

.v-card__title {
  background-color: var(--v-primary-lighten1) !important;
}
.v-sheet.v-card {
  background-color: var(--v-primary-lighten2) !important;
}
.v-data-table {
  background-color: var(--v-primary-lighten3) !important;
}
tr:hover {
  background-color: var(--v-primary-lighten1) !important;
}

@media only screen and (max-width: 800px) {
  .v-application {
    font-size: 16px;
  }
}
</style>
