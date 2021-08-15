<template>
    <div class="area">
      <div class="title">{{title}}</div>
      <div class="nextTo">
      <group-project  v-bind:title="grupa1.title" v-bind:image="grupa1.image" />
      <group-project  v-bind:title="grupa1.title" v-bind:image="grupa1.image" />
      <group-project  v-bind:title="grupa1.title" v-bind:image="grupa1.image" />
      </div>
    </div>
</template>

<script>
import GroupProject from './groupProject.vue'
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'

export default {
  name: "groups",
  props: [],
  data() {
    return {
      title: getString('userPanel', 'myGroups'),
      grupa1:{
        title: "Osiedle Kwiatowe",
        image: "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg"
      }
    }
  },
  methods: {
    getString,
    getColor
  },
  components:{
    GroupProject 
  }
}
</script>

<style scoped>
  .nextTo{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-self: center;
  }
  .title{
    font-family: 'Playfair Display';
    align-self: center;
    font-size: 26px;
    font-weight: lighter;
    margin-bottom: 15px;
  }
  .area{
    margin-top: 30px;
    display: flex;
    flex-direction: column; 
    width: 50%;
  }

</style>