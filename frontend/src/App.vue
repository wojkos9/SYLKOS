/* eslint-disable */
<template>
  <div id="app">
    <navbar-comp/>
    <my-project/>
    <router-view/>
  </div>
  <!-- <router-link to="/"> Home</router-link> -->
</template>

<script>
import NavbarComp from "@/components/navbar_footer/Navbar.vue"
import {apiService} from "@/common/api.service.js"
import myProject from "@/components/user/myProject.vue"

export default {
  name: "App",
  components: {
    NavbarComp,
    myProject
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');

  html,
  body {
    height: 100%;
    font-family: 'Inter', sans-serif ;
    font-weight: 500;
    font-size: 16px;
  }

  .btn:focus{
    box-shadow: none !important;
  }

</style>