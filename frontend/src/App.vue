/* eslint-disable */
<template>
  <div id="app">
    <navbar-comp/>
    <router-view/>
  </div>
  <!-- <router-link to="/"> Home</router-link> -->
</template>

<script>
import NavbarComp from "@/components/Navbar.vue"
import {apiService} from "@/common/api.service.js"

export default {
  name: "App",
  components: {
    NavbarComp
  },
  methods: {
    async setUserInfo(){
      const data = await  apiService("/api/user/")
      const requestUser = data["username"]
      window.localStorage.setItem("username", requestUser)
    }
  },
  created() {
    this.setUserInfo()
  },
};
</script>

<style>
  html,
  body {
    height: 100%;
    font-family: "Playfair Display", serif;
  }

  .btn:focus{
    box-shadow: none !important;
  }

</style>