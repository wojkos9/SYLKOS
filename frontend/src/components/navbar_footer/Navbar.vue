<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light cos">
    <router-link :to="{ name: mainPageRoute }">
    <img src="@/assets/logo3.png" class="logo" />
    </router-link>
    <button
      @click="clicked"
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <Button v-bind:title="getString('navbar', 'projects')"
              v-bind:fun="projectsClicked"
              v-bind:route="projectsRoute"/>
      <Button v-bind:title="getString('navbar', 'groups')"
              v-bind:fun="groupsClicked"
              v-bind:route="groupsRoute"/>
      <Button v-bind:title="getString('navbar', 'addProject')"
            v-bind:fun="newProjectClicked"/>
      

      <div class="role" v-if="role === 'admin'">
        {{ getString("navbar", "admin") }}
      </div>
      <Button v-bind:title="getString('navbar', 'account')"
            v-bind:fun="accountClicked"/>
     
    </div>
  </nav>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import Button from './Button.vue';
export default {
  components: { Button },
  name: "NavbarComponent",
  props:["setShowSideMenu"],
  data() {
    return {
      role: "admin",
      hover: false,
      groupsRoute: 'groups',
      projectsRoute: 'projects',
      mainPageRoute: 'main'
    };
  },
  methods: {
    getString,
    getColor,
    clicked() {
      console.log("kliknieto!");
      this.setShowSideMenu();
    },
    projectsClicked() {
      console.log("projekty");
    },
    groupsClicked() {
      console.log("grupy");
    },
    newProjectClicked() {
      console.log("nowy projekt");
    },
    accountClicked() {
      console.log("konto");
    },
  },
  mounted() {
    console.log(this.color);
  },
  computed: {
    myNavbar() {
      return {
        backgroundColor: this.getColor("navbar"),
        borderBottom: 1,
        borderBottomRightRadius: "40px",
      };
    },
    button() {
      return {
        backgroundColor: this.getColor("backgroundcolor"),
        alignSelf: "center",
        borderRadius: "35px",
        marginLeft: "1%",
        padding: "1%",
        width: "15%",
        textAlign: "center",
      };
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100&display=swap");

.logo {
  margin-top: 4px;
  margin-bottom: 4px;
  align-self: center;
}
.rigthSection {
  align-self: center;
  display: flex;
  align-content: center;
}

.role {
  font-size: 36px;
  align-self: center;
  font-weight: 300;
  margin-left: 25%;
}

.cos {
  background-color: #c0cfe6 !important;
}

.active {
  cursor: pointer;
  background-color: #93abc4;
}

@media only screen and (max-width: 1400px) {
  .role {
    font-size: 30px;
  }
}

@media only screen and (max-width: 1300px) {
  .role {
    font-size: 26px;
  }
}

@media only screen and (max-width: 1200px) {
  .role {
    font-size: 20px;
  }
}
</style>
