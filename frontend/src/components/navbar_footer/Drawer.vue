/* eslint-disable */
<template>
  <md-drawer :md-active.sync="showSideMenu" class="drawer">
    <md-toolbar class="md-transparent" md-elevation="0">
      <img src="@/assets/logo3.png" class="logo" />
    </md-toolbar>

    <md-list>
      <md-list-item @click="isProjectsClicked">
        <md-icon :class="projects  ? isiconChecked : ''">grid_view</md-icon>
        <span class="md-list-item-text"  >{{
          getString("navbar", "projects")
        }}</span>
      </md-list-item>

      <md-list-item @click="groupsClicked">
        <md-icon :class="groups  ? isiconChecked : ''">groups</md-icon>
        <span class="md-list-item-text">{{
          getString("navbar", "groups")
        }}</span>
      </md-list-item>

      <md-list-item @click="newProjectClicked">
        <md-icon :class="addProject  ? isiconChecked : ''">add</md-icon>
        <span class="md-list-item-text">{{
          getString("navbar", "addProject")
        }}</span>
      </md-list-item>

      <md-list-item md-expand>
        <md-icon >
          manage_accounts
        </md-icon>
        <span class="md-list-item-text">{{
          getString("navbar", "account")
        }}</span>

        <md-list slot="md-expand" >
          <md-list-item class="md-inset" @click="settingsClicked" >{{
            getString("navbar", "settings")
          }}</md-list-item>
          <md-list-item class="md-inset" @click="userPanelClicked" >{{
            getString("navbar", "user")
          }}</md-list-item>
        </md-list>
      </md-list-item>
    </md-list>
  </md-drawer>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "App",
  props: ["showSideMenu"],
  data() {
    return {
      active: "",
      projects: false,
      groups: false,
      addProject: false,
    };
  },
  methods: {
    getString,
    getColor,
    isProjectsClicked() {
      console.log("projekty1");
      this.projects = true
      this.groups = false
      this.addProject = false
      console.log("efekt: ", this.projects)
    },
    groupsClicked() {
      console.log("grupy");
      this.projects = false
      this.groups = true
      this.addProject = false
    },
    newProjectClicked() {
      console.log("nowy projekt");
      this.projects = false
      this.groups = false
      this.addProject = true
    },
    settingsClicked() {
      console.log("ustawienia");
      this.projects = false
      this.groups = false
      this.addProject = false
    },
    userPanelClicked() {
      console.log("panel użytkownika");
      this.projects = false
      this.groups = false
      this.addProject = false
    },
  },
  computed:{
    isiconChecked(){
      return{
        border: "3",
      }
    }
  }
};
</script>

<style>
.logo{
  width: 100px;
  height: 50px;;
}  
.drawer{
  width: 250px !important;
}
</style>
