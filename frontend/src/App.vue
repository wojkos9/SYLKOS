<template>
  <v-app class="font">
    <div id="app">
      <div
        class="wrapper"
        :style="{ background: $vuetify.theme.themes[theme].background }"
      >
        <navbar-comp v-bind:setShowSideMenu="navigationDrawer" />
        <router-view />

        <v-navigation-drawer v-model="showSideMenu" absolute temporary >
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
                   {{$t("projects")}}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.groups }">
                <v-list-item>
                  <v-list-item-title>
                    <v-icon>groups</v-icon>
                   {{$t("groups")}}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.addProject }" :is="!showSections ? 'span' : 'router-link'">
                <v-list-item @click="ifLogin">
                  <v-list-item-title>
                    <v-icon>add</v-icon>
                   {{$t("addProject")}}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.settings }" :is="!showSections ? 'span' : 'router-link'">
                <v-list-item  @click="ifLogin">
                  <v-list-item-title>
                    <v-icon>settings</v-icon>
                   {{$t("settings")}} 
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.user }" :is="!showSections ? 'span' : 'router-link'">
                <v-list-item @click="ifLogin">
                  <v-list-item-title>
                    <v-icon>person</v-icon>
                   {{$t("user")}}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <div v-show="showSections">
                <router-link :to="{ name: routes.admin }">
                  <v-list-item>
                    <v-list-item-title>
                      <v-icon>mdi-wrench</v-icon>
                   {{$t("admin")}}
                    </v-list-item-title>
                  </v-list-item>
                </router-link>
              </div>

              <router-link  v-show="showSections" :to="{ name: routes.admin }" :is="!showSections ? 'span' : 'span'">
                <v-list-item @click="logout">
                  <v-list-item-title>
                    <v-icon>logout</v-icon>
                   {{$t("logout")}}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.admin }" :is="!showSections ? 'span' : 'router-link'">
                <v-list-item v-show="!showSections" @click="login">
                  <v-list-item-title>
                    <v-icon>login</v-icon>
                   {{$t("login")}}
                  </v-list-item-title>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: routes.admin }" :is="!showSections ? 'span' : 'router-link'">
                <v-list-item v-show="!showSections" @click="register">
                  <v-list-item-title>
                    <v-icon>mdi-account-plus</v-icon>
                   {{$t("register")}} 
                  </v-list-item-title>
                </v-list-item>
              </router-link>

               <router-link :to="{ name: routes.admin }" :is="!showSections ? 'span' : 'span'">
                <v-list-item   @click="changeLanguage">
                  <v-list-item-title>
                    <!-- <div style="font-size:20px"> -->
                    <flag v-if="currentLang=='pl'" style="font-size:18px; margin-right: 5px" iso="us" />
                    <flag v-else style="font-size:18px; margin-right: 5px" iso="pl" />
                   <!-- </div> -->
                   {{ $t('newLanguage') }} 
                  </v-list-item-title>
                </v-list-item>
              </router-link>


            </v-list-item-group>

            <div class="paddingTop-m paddingLeft-s">
              <v-tooltip v-if="!$vuetify.theme.dark" bottom >
                <template v-slot:activator="{ on }">
                  <v-btn v-on="on" color="night" small fab @click="changeColorMode">
                    <v-icon color="white" class="mr-1">mdi-moon-waxing-crescent</v-icon>
                  </v-btn>
                </template>
                <span>włącz tryb ciemny</span>
              </v-tooltip>

              <v-tooltip v-else bottom >
                <template v-slot:activator="{ on }">
                  <v-btn v-on="on" color="day" small fab @click="changeColorMode">
                    <v-icon color="yellow">mdi-white-balance-sunny</v-icon>
                  </v-btn>
                </template>
                <span>włącz tryb jasny</span>
              </v-tooltip>
            </div>
          </v-list>
        </v-navigation-drawer>
        <div class="push"></div>
      </div>
      <!-- <div class="footer"> <Footer /></div> -->
    </div>
    <Unauthorized
      :dialog="dialog"
      :backAction="backAction"
      :nextAction="nextAction"
    />
  </v-app>
</template>

<script>
import NavbarComp from "@/components/navbar_footer/Navbar.vue";
import { apiService } from "@/common/api.service.js";
// import Footer from "./components/navbar_footer/Footer.vue";
import Unauthorized from "@/components/UI/Unauthorized.vue";

export default {
  name: "App",
  components: {
    NavbarComp,
    Unauthorized,
    // Footer,
  },
  data() {
    return {
      showSideMenu: false,
      group: "",
      themeChange: true,
      dialog: false,
      showSections: true,
      currentLang: 'pl',
      newLang: 'en',
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
    backAction() {
      this.dialog = false;
    },
    nextAction() {
      this.dialog = false;
      window.location.href = "../accounts/login/?next=/#/";
    },
    login(){
      window.location.href = "../accounts/login/?next=/#/";
    },
    register(){
      window.location.href = "../accounts/register/";
    },
    logout(){
      window.location.href = "../logout/";
    },
    ifLogin() {
      this.dialog = this.showSections ? false : true;
    },
    changeLanguage(){
      this.currentLang = this.newLang
      this.newLang = this.$i18n.locale
      this.$i18n.locale = this.currentLang
      
    },
    async changeColorMode(){
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
       await apiService("/api/user/", "PATCH", {color_mode: this.$vuetify.theme.dark ? 0 : 1});
    },
    check(funName) {
      if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("gosc")
      ) {
        this.$root.$refs.App.ifLogin();
      } else {
        funName();
      }
    },
    async setUserInfo() {
      const data = await apiService("/api/user/");
      console.log(data);
      if (data == "gosc") {
        if(window.location.href.slice(Math.max(window.location.href.length - 3, 1)) == "/#/"){
        window.location.href = "../accounts/login/?next=/#/"
        }
        window.localStorage.setItem("username", "gosc");
        this.showSections = false;
        this.$vuetify.theme.dark = 1;
      } else {
        const requestUser = data["username"];
        window.localStorage.setItem("username", requestUser);
        this.$vuetify.theme.dark = !data["color_mode"]
      }
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
    this.$root.$refs.App = this;
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
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap");

a {
  text-decoration: none !important;
}
.v-application {
  font-family: "Open Sans", sans-serif;
  font-weight: 500;
  /* background-color: #f2f6fa; */
  color: #fff;

  /* border:solid white; */
  display: flex;
  height: 100vh;
  margin: 0;
  flex-direction: column;
}

.paddingTop-s {
  padding-top: 10px;
}
.paddingTop-m {
  padding-top: 20px !important;
}
.paddingTop-l {
  padding-top: 30px  !important;
}
.paddingTop-xl {
  padding-top: 40px  !important;
}

.paddingBottom-s {
  padding-bottom: 10px;
}
.paddingBottom-m {
  padding-bottom: 20px;
}
.paddingBottom-l {
  padding-bottom: 30px;
}
.paddingBottom-xl {
  padding-bottom: 40px;
}

.paddingLeft-s {
  padding-left: 10px;
}
.paddingLeft-m {
  padding-left: 20px;
}
.paddingLeft-l {
  padding-left: 30px;
}
.paddingLeft-xl {
  padding-left: 40px;
}

/* .clickable{
  background-color: rgb(89, 89, 184);
  color: #000;
  transition: all .3s ease;
  max-width: 150px;
  border-radius: 8px;

}
.clickable:hover{
  background-color: rgb(202, 202, 233);
  transition: scale(1.1);
  cursor: pointer
} */

.button {
  background-color: var(--v-secondary-lighten1);
  color: #000;
  transition: all 0.3s ease;
  max-width: 150px;
  border-radius: 8px;
  padding: 5px 8px;
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 14px;
  font-weight: 700;
}

v-dialog {
  z-index: 10000 !important;
}
.button:hover {
  background-color: var(--v-secondary-lighten2);
  transform: scale(1.1);
  cursor: pointer;
}

body {
  height: 100vh;
}

#app {
  border: white;
}

.v-icon:hover {
  cursor: pointer;
}

.wrapper {
  min-height: 100vh;
  /* margin-bottom: -100px; */
  /* border:solid white; */
}

.footer,
.push {
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
