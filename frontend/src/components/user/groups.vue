<template>
    <div>
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

export default {
  name: "groups",
  props: ['title'],
  data() {
    return {
      grupa1:{
        title: "Osiedle Kwiatowe",
        image: "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg"
      }
    }
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
  }
  .title{
    font-family: 'Playfair Display';
    font-size: 36px;
    font-weight: lighter;
    margin-left: 10px;
    margin-bottom: 15px;

  }
</style>