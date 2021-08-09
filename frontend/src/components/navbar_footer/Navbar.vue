<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light cos">
    <img src="@/assets/logo3.png" class="logo" />
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
              v-bind:fun="projectsClicked"/>
      <Button v-bind:title="getString('navbar', 'groups')"
              v-bind:fun="groupsClicked"/>
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
  data() {
    return {
      role: "admin",
      hover: false,
    };
  },
  methods: {
    getString,
    getColor,
    clicked() {
      console.log("kliknieto!");
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
        // alignContent: "center",
        // display: "flex",
        // height: "5%",
        borderBottomRightRadius: "40px",
        borderBottomLeftRadius: "40px",
        // width: "100%"
      };
    },
    button() {
      return {
        backgroundColor: this.getColor("backgroundcolor"),
        // height:"50%",
        alignSelf: "center",
        borderRadius: "35px",
        marginLeft: "1%",
        padding: "1%",
        // paddingLeft: "1%",
        // paddingRight: "1%",
        width: "15%",
        //  width: "10rem",
        textAlign: "center",
        // fontSize: "4px"
      };
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100&display=swap");

.logo {
  /* margin-left: 2%; */
  margin-top: 4px;
  margin-bottom: 4px;
  /* width: 100%; */
  /* height: 90%; */
  /* padding-right: 1%; */
  align-self: center;
}
.rigthSection {
  /* margin-left: 20%; */
  /* margin-right: 1%; */
  /* margin-left: 700px; */
  align-self: center;
  display: flex;
  align-content: center;
  /* font-size: 6px; */
  /* margin-top: 10; */
  /* font-weight: 300; */
}

.role {
  font-size: 36px;
  /* font-size: 350%; */
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
