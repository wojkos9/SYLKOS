/* eslint-disable */
<template>
  <div id="app">
    <navbar-comp v-bind:setShowSideMenu="setShowSideMenu"/>
    <main-screen/>
    <router-view/>
    <drawer v-bind:showSideMenu="showSideMenu"/>
  </div>
</template>

<script>
import NavbarComp from "@/components/navbar_footer/Navbar.vue"
import {apiService} from "@/common/api.service.js"
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
import MainScreen from './screens/mainScreen.vue';
import Drawer from './components/navbar_footer/Drawer.vue'

export default {
  name: "App",
  components: {
    NavbarComp,
    MainScreen,
    Drawer
  },
  data() {
    return {
      title:"Osiedle Kwiatowe",
      desc:"Oswietlenie wszystkich zaciemnionych ulic",
      image:"https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      showSideMenu: false
    }
  },
  methods: {
    async setUserInfo(){
      const data = await  apiService("/api/user/")
      const requestUser = data["username"]
      window.localStorage.setItem("username", requestUser)
    },
    getString,
    getColor,
    setShowSideMenu(){
      this.showSideMenu = false
      this.showSideMenu = true
    }
  },
  created() {
    this.setUserInfo()
  },
  
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic|Material+Icons"); 

html,
  body {
    height: 100%;
    font-family: 'Inter', sans-serif ;
    font-weight: 500;
    font-size: 12px;
    background-color: #f2f6fa;
  }

  .btn:focus{
    box-shadow: none !important;
  }

</style>