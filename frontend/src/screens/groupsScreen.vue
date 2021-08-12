/* eslint-disable */
<template>
  <div class="center">
   <Title v-bind:numberOfAllGroups="243"/>
   <group/>
   <group/>
   <group/>
   <group/>
   <group/>
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
      title: "Osiedle Kwiatowe",
      desc: "Oswietlenie wszystkich zaciemnionych ulic",
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
    };
  },
  methods: {
    getString,
    getColor,
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
