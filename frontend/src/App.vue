/* eslint-disable */
<template>
  <div id="app">
    <navbar-comp/>
    <div>
    <groups/>
    <projects />
    </div>
    <user-projects/>
    <router-view/>
  </div>
  <!-- <router-link to="/"> Home</router-link> -->
</template>

<script>
import NavbarComp from "@/components/navbar_footer/Navbar.vue"
import {apiService} from "@/common/api.service.js"
import Groups from './components/user/groups.vue';
import Projects from './components/user/projects.vue';
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
import UserProjects from './components/user/userProjects.vue';

export default {
  name: "App",
  components: {
    NavbarComp,
    Groups,
    Projects,
    UserProjects
  },
  data() {
    return {
      title:"Osiedle Kwiatowe",
      desc:"Oswietlenie wszystkich zaciemnionych ulic",
      image:"https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes"
    }
  },
  methods: {
    async setUserInfo(){
      const data = await  apiService("/api/user/")
      const requestUser = data["username"]
      window.localStorage.setItem("username", requestUser),
      getString,
      getColor
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
  
  html,
  body {
    height: 100%;
    font-family: 'Inter', sans-serif ;
    font-weight: 500;
    font-size: 16px;
    background-color: #f2f6fa;
  }

  .btn:focus{
    box-shadow: none !important;
  }

</style>