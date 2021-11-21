<template>
  <md-drawer :md-active.sync="showSideMenu" class="drawer">
    <md-toolbar class="md-transparent" md-elevation="0"
      ><router-link :to="{ name: routes.mainPage }">
        <svg  src="@/assets/logo.png" class="logo"
      /></router-link>
    </md-toolbar>

    <md-list>
      <router-link :to="{ name: routes.projects }">
        <md-list-item @click="isProjectsClicked">
          <md-icon :class="projects ? isiconChecked : ''">grid_view</md-icon>
          <span class="md-list-item-text">{{
            getString("navbar", "projects")
          }}</span>
        </md-list-item>
      </router-link>

      <router-link :to="{ name: routes.groups }">
        <md-list-item @click="groupsClicked">
          <md-icon :class="groups ? isiconChecked : ''">groups</md-icon>
          <span class="md-list-item-text">{{
            getString("navbar", "groups")
          }}</span>
        </md-list-item>
      </router-link>

      <router-link :to="{ name: routes.addProject }">
        <md-list-item @click="newProjectClicked">
          <md-icon :class="addProject ? isiconChecked : ''">add</md-icon>
          <span class="md-list-item-text">{{
            getString("navbar", "addProject")
          }}</span>
        </md-list-item>
      </router-link>

      <md-list-item md-expand>
        <md-icon>
          manage_accounts
        </md-icon>
        <span class="md-list-item-text">{{
          getString("navbar", "account")
        }}</span>

        <md-list slot="md-expand">
          <md-list-item class="md-inset" @click="settingsClicked">{{
            getString("navbar", "settings")
          }}</md-list-item>
          <md-list-item class="md-inset" @click="userPanelClicked">{{
            getString("navbar", "user")
          }}</md-list-item>
        </md-list>
      </md-list-item>


      <v-switch
      v-model="theme"
      inset
      :label="`Switch 1: ${switch1.toString()}`"
    ></v-switch>

    </md-list>
  </md-drawer>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "App",
  props: ["showSideMenu"],
  theme: false,
  themeLabel: this.$vuetify.theme,
  data() {
    return {
      projects: false,
      groups: false,
      addProject: false,
      routes: {
        addProject: "projectNew",
        projects: "projects",
        groups: "groups",
        mainPage: "main",
      },
    };
  },
  methods: {
    getString,
    getColor,
    isProjectsClicked() {
      this.projects = true;
      this.groups = false;
      this.addProject = false;
    },
    groupsClicked() {
      this.projects = false;
      this.groups = true;
      this.addProject = false;
    },
    newProjectClicked() {
      this.projects = false;
      this.groups = false;
      this.addProject = true;
    },
    settingsClicked() {
      this.projects = false;
      this.groups = false;
      this.addProject = false;
    },
    userPanelClicked() {
      this.projects = false;
      this.groups = false;
      this.addProject = false;
    },
  },
  computed: {
    isiconChecked() {
      return {
        border: 3,
      };
    },
  },
   watch: {
      theme(){
        //called whenever switch1 changes
        if (this.$vuetify.theme.dark)
          this.$vuetify.theme.dark = true;
        else
          this.$vuetify.theme.dark = false;
      }
    }
};
</script>

<style>
.logo {
  width: 100px;
  height: 50px;
}
.drawer {
  width: 250px !important;
}
</style>
