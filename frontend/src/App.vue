/* eslint-disable */
<template>
  <div id="app">
    <navbar-comp v-bind:setShowSideMenu="setShowSideMenu"/>
    <router-view/>
    <drawer v-bind:showSideMenu="showSideMenu"/>
    <div>
      <comments
        userName = 'Mateusz Kluba'
        rating = "3.5"
        postingDate = '13.09.2021'
        commentText = 'Świetny pomysł! Sam nieraz widzę potrzebę lepszego oświetlenia naszych alejek. Chciałbym jednak znać więcej szczegółów'
        likes = "0"
        dislikes = "0"
        userVotedFor="nothing"
      />
    </div>
    <div>
      <voting-page
        date="24 listopada 2021"
        group="Osiedle Kwiatowe"
        title="Łąka przy osiedlowym strumyku"
        description="Miejsce do relaksu dla mieszkańców osiedla. Obok strumyka przepływającego
         przez osiedle planujemy zasadzić drzewa i kwiaty, postawić ławki i dać możliwość odpoczynku z naturą."
        price="10 000"
        likes="21"
        dislikes="37"
        userVotedFor="nothing"
      />
    </div>
  </div>
</template>

<script>
import NavbarComp from "@/components/navbar_footer/Navbar.vue"
import {apiService} from "@/common/api.service.js"
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
<<<<<<< HEAD
import Drawer from './components/navbar_footer/Drawer.vue'
=======
import UserProjects from './components/user/userProjects.vue';
import Comments from './components/user/comments.vue';
import VotingPage from './components/user/votingPage.vue';
>>>>>>> feature/frontComponentsMateusz

export default {
  name: "App",
  components: {
    NavbarComp,
<<<<<<< HEAD
    Drawer, 
=======
    Groups,
    Projects,
    UserProjects,
    Comments,
    VotingPage,
>>>>>>> feature/frontComponentsMateusz
  },
  data() {
    return {
      title:"Osiedle Kwiatowe",
      desc:"Oswietlenie wszystkich zaciemnionych ulic",
      image:"https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
<<<<<<< HEAD
      showSideMenu: false
=======
      likes: 0,
      dislikes: 0,
      userVotedFor: "nothing"
>>>>>>> feature/frontComponentsMateusz
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
<<<<<<< HEAD
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic|Material+Icons"); 

html,
=======
@import url("https://fonts.googleapis.com/css?family=Material+Icons");
  
  html,
>>>>>>> feature/frontComponentsMateusz
  body {
    /* height: 100%; */
    font-family: 'Inter', sans-serif ;
    font-weight: 500;
    font-size: 12px;
    background-color: #f2f6fa;
  }

  .btn:focus{
    box-shadow: none !important;
  }

  .icon{
    color: #32e20e;
  }

</style>