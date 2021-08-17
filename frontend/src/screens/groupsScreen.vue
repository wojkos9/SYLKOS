/* eslint-disable */
<template>
  <div class="center">
   <Title v-bind:numberOfAllGroups="243" v-on:changeSearcgName="makeSth($event)"/>
   
   <group
    v-show="check(this.title)"
    v-bind:name="title"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    />
    <group
    v-show="check(this.title)"
    v-bind:name="title"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    />
    <group
    v-show="check(this.name)"
    v-bind:name="name"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    />
    <group
    v-show="check(this.title)"
    v-bind:name="title"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    />
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import Title from '../components/groups/title.vue';
import Group from '../components/groups/group.vue';


export default {
  name: "groupsScreen",
  components: {Title, Group},
  data() {
    return {
      name:"Zatorze",
      title: "Osiedle Kwiatowe",
      desc: "Boisko do siatkówki plażowej w miejscu obecnego kamienistego placu " +
            "przy ulicy MajaBoisko do siatkówki plażowej w miejscu obecnego " +
            "kamienistego placu przy ulicy MajaBoisko do siatkówki plażowej w " +
            "miejscu obecnego kamienistego placu przy ulicy MajaBoisko do " +
            "siatkówki plażowej w miejscu obecnego kamienistego placu przy ulicy " +
            "Maja",
      members: 34,
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      searchName: ""
    };
  },
  methods: {
    getString,
    getColor,
    makeSth(str){
      this.searchName = str
    },
    check(str){
      console.log(this.searchName)
      console.log(str.toLowerCase().includes(this.searchName.toLowerCase()))
      return str.toLowerCase().includes(this.searchName.toLowerCase())
    }
  },
};
</script>

<style>

.center{
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>
