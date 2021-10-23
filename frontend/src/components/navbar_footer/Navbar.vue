<template>
  <v-row>
    <v-col cols="12">
      <v-card color="primary darken-1">
        <v-card-title>
          <div
            class="d-flex justify-content-between  align-items-center leftSection"
            style="width:100%;"
          >
            <div class="d-flex align-items-center">
              <router-link :to="{ name: mainPageRoute }">
                <img src="@/assets/logo.png" class="logo" />
              </router-link>

              <div class="menu">
                <div class="d-flex align-items-center">
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
                  <Button
                    v-bind:title="getString('navbar', 'addProject')"
                    v-bind:route="addProjectRoute"
                    v-on:reset="select = ''"
                  />
                </div>
              </div>
            </div>
            <div class="menu">
              <div
                class="d-flex justify-flex-end  align-self-start  "
                style="position:relative; width: 200px; "
              >
              

                <v-container fluid>
                  <v-row>
                    <v-col cols="12">
                      <v-combobox
                        color="secondary"
                        @click="select = ''"
                        v-model="select"
                        :items="menuOptions"
                        :label="role"
                        item-text="name"
                        item-value="route"
                      ></v-combobox>
                    </v-col>
                  </v-row>
                </v-container>
              </div>
            </div>

            <v-btn
              class="mx-2 showBurger"
              fab
              dark
              color="secondary"
              @click="setShowSideMenu()"
            >
              <v-icon dark>
                mdi-format-list-bulleted-square
              </v-icon>
            </v-btn>
          </div>
        </v-card-title>
      </v-card>
    </v-col>
  </v-row>
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
      select: '',
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
      if(val != '' && this.$route.name != val.route)
        this.$router.push({name: val.route});
    },
  },
};
</script>

<style>
.showBurger {
  display: none;
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

@media only screen and (max-width: 1400px) {
  nav {
    font-size: 14px;
  }
}

@media only screen and (max-width: 992px) {
  .leftSection {
    width: 100%;
    justify-content: space-between;
  }
  .showBurger {
    display: block !important;
  }
  .menu {
    display: none !important;
  }
}
</style>
