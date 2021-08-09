<template>
    <div class="contentarea">
      <div class="title">{{title}}</div>
      <div class="nextTo">
      <my-project/>
      </div>
      <div class="button"><button-next/></div>
    </div>
</template>

<script>

import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
import MyProject from './myProject.vue'

export default {
  name: "userProjects",
  props: [],
  data() {
    return {
      title: getString('userPanel', 'myProjects'),
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
    MyProject,
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
  .contentarea{
    display: flex;
    flex-direction: column;
    margin-top: 10px;
    width: 50%;
  }
  .button{
    display:flex;
    flex-direction: row;
    justify-content: flex-end;
  }
</style>