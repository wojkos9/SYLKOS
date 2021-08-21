<template>
  <div class="projects">
    <div class="title">{{ title }}</div>
    <div class="nextToProjects" style="z-index:-1">
      <group-project
        v-bind:title="grupa1.title"
        v-bind:image="grupa1.image"
        v-bind:desc="grupa1.desc"
      />

      <group-project
        v-bind:title="grupa1.title"
        v-bind:image="grupa1.image"
        v-bind:desc="grupa1.desc"
      />

      <group-project
        v-bind:title="grupa1.title"
        v-bind:image="grupa1.image"
        v-bind:desc="grupa1.desc"
      />
    </div>
    <div class="row">
      <div class="col-sm-9"></div>
      <div class="col-sm-3"><button-next /></div>
    </div>
  </div>
</template>

<script>
import GroupProject from "./groupProject.vue";
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import ButtonNext from "../UI/buttonNext.vue";

export default {
  name: "projects",
  props: [],
  data() {
    return {
      title: getString("userPanel", "votedProjects"),
      grupa1: {
        title: "Osiedle Kwiatowe",
        desc: "Oswietlenie wszystkich zaciemnionych ulic",
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
    ButtonNext,
  },
};
</script>

<style scoped>
.nextToProjects {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-self: center;
  justify-content: center;
}
.title {
  font-family: "Playfair Display";
  font-size: 26px;
  font-weight: lighter;
  align-self: center;
  text-align: center;
  margin-bottom: 15px;
}
.area {
  display: flex;
  flex-direction: column;
  margin-top: 10px;
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
