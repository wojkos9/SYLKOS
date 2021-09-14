<template>
  <nav class="cos d-flex justify-content-between p-4">
    <div class="d-flex justify-content-between leftSection"  >
      <router-link :to="{ name: mainPageRoute }">
        <img src="@/assets/logo3.png" class="logo" />
      </router-link>
     <v-btn
      class="mx-2 showBurger"
      fab
      dark
      color="teal"
      @click="clicked"
    >
      <v-icon dark>
        mdi-format-list-bulleted-square
      </v-icon>
    </v-btn>

      <div class="d-flex justify-content-between align-self-center menu" id="navbarSupportedContent">
        <Button v-bind:title="getString('navbar', 'projects')"
                v-bind:route="projectsRoute"/>
        <Button v-bind:title="getString('navbar', 'groups')"
                v-bind:route="groupsRoute"/>
        <Button v-bind:title="getString('navbar', 'addProject')"
                v-bind:route="addProjectRoute"/>
      </div>

    </div>
    <div class="d-flex justify-flex-end  align-self-start menu " style="position:relative; width: 200px; " >
      <list-button :title="role" :options="menuOptions" />
    </div>
    
  </nav>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import Button from './Button.vue';
import {apiService} from "@/common/api.service.js"
import ListButton from '../UI/ListButton.vue';

export default {
  components: { Button, ListButton },
  name: "NavbarComponent",
  props:["setShowSideMenu"],
  data() {
    return {
      role: "admin",
      hover: false,
      groupsRoute: 'groups',
      projectsRoute: 'projects',
      mainPageRoute: 'main',
      addProjectRoute: 'registerProject',
      show: false,
      menuOptions: [ 
        {name: this.getString("navbar", "settings"), route: "groupNew"},
        {name: this.getString("navbar", "user"), route: "projects"},
        ]
    };
  },
  methods: {
    getString,
    getColor,
    clicked() {
      this.setShowSideMenu();
    },
    accountClicked() {
      console.log("konto");
    },
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
      this.role = window.localStorage.getItem("username");
      if(this.role == "admin"){
        this.menuOptions.push({name:this.getString("navbar", "admin"), route: "admin" })
      }
    },
    getToAdminSite(){
      
    }
  },
  created(){
    this.setUserInfo()
  },
  computed: {
    myNavbar() {
      return {
        backgroundColor: this.getColor("navbar"),
        borderBottom: 1,
        borderBottomRightRadius: "40px",
      };
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100&display=swap");

.showBurger {
    display:none;
  }

.logo {
  margin-top: 4px;
  margin-bottom: 4px;
  align-self: center;
}

.role {
  font-size: 2.5em;
  align-self: center;
  font-weight: 300;
}

.cos { 
  background-color: #c0cfe6 !important;
}

@media only screen and (max-width: 1400px) {
  nav {
    font-size: 14px;
  }
}


@media only screen and (max-width: 992px) {
  .leftSection{
    width: 100%;
    justify-content: space-between;
  }
  .showBurger {
    display:block !important;
  }
  .menu{  
  display:none !important;
}
}


</style>
