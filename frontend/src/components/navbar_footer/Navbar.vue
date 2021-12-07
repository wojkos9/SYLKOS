<template>
  <v-card color="primary darken-1" class="gradient ">
    <div class="gradient-transparent"></div>

    <v-card-title>
      <div
        class="d-flex justify-content-center  align-items-center leftSection"
        style="width:100%;"
      >

       <div class="logo-div">
         
                 <router-link :to="{ name: mainPageRoute }" >
                   <!-- <div v-if="$vuetify.theme.light"> -->
                <img src="@/assets/logo.png" class="logo" />

                   <!-- </div> -->
                   <!-- <div v-else> -->
                <!-- <img src="@/assets/logo_white.png" class="logo" /> -->

                   <!-- </div> -->
              </router-link>
              </div>

        <div class="d-flex align-items-center justify-content: center">
          <div class="menu">
            <div
              class="d-flex align-items-center justify-content-center"
            
            >
              <Button
                v-bind:title="getString('navbar', 'groups')"
                v-bind:route="groupsRoute"
                v-on:reset="select = ''"
              />
              <Button
                v-bind:title="getString('navbar', 'projects')"
                v-bind:route="projectsRoute"
                v-on:reset="select = ''"
              />
              <!-- <Button
                v-bind:title="getString('navbar', 'addProject')"
                v-bind:route="addProjectRoute"
                v-on:reset="select = ''"
              /> -->
                    <!-- <v-combobox
                      color="accent"
                      @click="select = ''"
                      v-model="select"
                      :items="menuOptions"
                      :label="role"
                      item-text="name"
                      item-value="route"
                    ></v-combobox> -->
            </div>
          </div>
        </div>
       
      <div class="burger-div">
        <v-btn
          class="mx-2 showBurger"
          fab
          dark
          color="accent"
          @click="setShowSideMenu()"
        >
          <v-icon dark>
            mdi-format-list-bulleted-square
          </v-icon>
        </v-btn>
        </div>
      </div>
    </v-card-title>
  </v-card>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import Button from "./Button.vue";

export default {
  components: { Button },
  name: "NavbarComponent",
  props: ["setShowSideMenu"],
  data() {
    return {
      groupsRoute: "groups",
      projectsRoute: "projects",
      mainPageRoute: "main",
      addProjectRoute: "projectNew",
      role: "",
      sort: "",
      select: "",
      menuOptions: [
        { name: this.getString("navbar", "settings"), route: "groupNew" },
        { name: this.getString("navbar", "user"), route: "projects" },
      ],
    };
  },
  methods: {
    getString,
    getColor,
    async setUserInfo() {
      this.role = window.localStorage.getItem("username");
      if (this.role == "admin") {
        this.menuOptions.push({
          name: this.getString("navbar", "admin"),
          route: "admin",
        });
      }
    },
  },
  created() {
    this.setUserInfo();
  },
  watch: {
    select: function(val) {
      if (val != "" && this.$route.name != val.route)
        this.$router.push({ name: val.route });
    },
  },
};
</script>

<style>

.gradient-transparent {
  width: 100%;
  z-index: 0;
  content: "";
  display: block;
  position: absolute;
  opacity: 0.9;
  top: 0;
  left: 0;
  background: linear-gradient(
    to right,
    var(--v-primary-base) 0%,
    var(--v-primary-base) 60%,
    rgba(255, 255, 255, 0) 100%
  );
  height: 100%;
}

.gradient::before {
  width: 100%;
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
  height: 100%;
  background-color: #78909c;
  opacity: 0.5;
  background-image: linear-gradient(
      30deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      150deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      30deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      150deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      60deg,
      var(--v-secondary-darken2) 25%,
      transparent 25.5%,
      transparent 75%,
      var(--v-secondary-darken2) 75%,
      var(--v-secondary-darken2)
    ),
    linear-gradient(
      60deg,
      var(--v-secondary-darken2) 25%,
      transparent 25.5%,
      transparent 75%,
      var(--v-secondary-darken2) 75%,
      var(--v-secondary-darken2)
    );

  background-size: 26px 46px;
  background-position: 0 0, 0 0, 10px 18px, 10px 18px, 0 0, 10px 18px;
  background-repeat: repeat;
}

.gradient{
  height: 120px;
}
.showBurger {
  display: none;
}

.logo {
  margin-top: 4px;
  margin-bottom: 4px;
  align-self: center;
  z-index: 1000;
  opacity: 1;
  position: relative;
}

.logo-div{
  position: absolute;
  top: 0;
  display: flex;
  align-items: center;
  left: 20px;
  height: 100%;
  /* padding: 10px 0; */
}

.burger-div{
  position: absolute;
  top: 0;
  display: flex;
  align-items: center;
  right: 20px;
  height: 100%;
}

.role {
  font-size: 2.5em;
  align-self: center;
  font-weight: 300;
}

@media only screen and (max-width: 1400px) {
  nav {
    font-size: 14px;
  }
}

@media only screen and (max-width: 700px) {
  .leftSection {
    width: 100%;
    height: 100px;
    justify-content: space-between;
  }
  .showBurger {
    display: block !important;
  }
  .menu {
    display: none !important;
  }
}

@media only screen and (max-width: 300px) {
 .logo-div{
   position: relative;
    left: 0;
 }
 .burger-div{
   position: relative;
   right: 0;
 }

}
</style>
