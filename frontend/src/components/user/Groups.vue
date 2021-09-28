<template>
  <div class="groups">
    <div class="title">{{ title }}</div>
    <div class="nextToGroupsScreen" style="z-index:-1">
      <div v-for="(group, index) in groups" :key="index">
        <group-project v-bind:title="group.name" v-bind:image="grupa1.image" />
      </div>
      <group-project v-bind:title="grupa1.title" v-bind:image="grupa1.image" />

      <group-project v-bind:title="grupa1.title" v-bind:image="grupa1.image" />

      <group-project v-bind:title="grupa1.title" v-bind:image="grupa1.image" />
    </div>
  </div>
</template>

<script>
import GroupProject from "./GroupProject.vue";
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "groups",
  props: ["groups"],
  data() {
    return {
      title: getString("userPanel", "myGroups"),
      grupa1: {
        title: "Osiedle Kwiatowe",
        image:
          "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      },
    };
  },
  methods: {
    getString,
    getColor,
  },
  components: {
    GroupProject,
  },
};
</script>

<style scoped>
.groups {
  margin-top: 50px;

}
.nextToGroupsScreen {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-self: center;
  justify-content: center;
}
.title {
  align-self: center;
  text-align: center;
  font-size: 26px;
  font-weight: lighter;
  margin-bottom: 15px;
}
.area {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  /* width: 50%; */
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
