<template>
    <div class="projects">
      <div class="title">{{title}}</div>
      <div class="row">
        <div class="col-lg-6 col-xl-4">
      <group-project  v-bind:title="grupa1.title" v-bind:image="grupa1.image" v-bind:desc="grupa1.desc"/>
        </div>

        <div class="col-lg-6 col-xl-4">
      <group-project  v-bind:title="grupa1.title" v-bind:image="grupa1.image" v-bind:desc="grupa1.desc"/>
        </div>

        <div class="col-lg-6 col-xl-4">
      <group-project  v-bind:title="grupa1.title" v-bind:image="grupa1.image" v-bind:desc="grupa1.desc"/>
        </div>
     
      </div>
      <div class="row">
        <div class="col-lg-4 col-xl-8"></div>
        <div class="col-lg-3 col-xl-3"> <button-next/></div>
    </div>
    </div>
</template>

<script>
import GroupProject from './groupProject.vue'
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
import ButtonNext from '../UI/buttonNext.vue'

export default {
  name: "projects",
  props: [],
  data() {
    return {
      title: getString('userPanel', 'votedProjects'),
      grupa1:{
        title: "Osiedle Kwiatowe",
        desc: "Oswietlenie wszystkich zaciemnionych ulic",
        image: "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg"
      }
    }
  },
  methods: {
    getString,
    getColor
  },
  components:{
    GroupProject,
    ButtonNext 
  }
}
</script>

<style scoped>
  .nextTo{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-self: center;
    height: 280px;
  }
  .title{
    font-family: 'Playfair Display';
    font-size: 26px;
    font-weight: lighter;
    align-self: center;
    margin-bottom: 15px;
  }
  .area{
    display: flex;
    flex-direction: column;
    margin-top: 10px;
    width: 50%;
  }
  
    @media only screen and (max-width: 1200px) {
  .title {
    font-size: 22px;
  }
}

@media only screen and (max-width: 1000px) {
  .title {
    font-size: 20px;
  }
}
</style>