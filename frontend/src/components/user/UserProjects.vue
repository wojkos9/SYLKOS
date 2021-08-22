<template>
  <div class="contentarea">
    <div class="title">{{ title }}</div>

    <my-project />
    <my-project />
    <my-project />
    <my-project />
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import MyProject from "./MyProject.vue";

export default {
  name: "userProjects",
  props: [],
  data() {
    return {
      title: getString("userPanel", "myProjects"),
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
    MyProject,
  },
};
</script>

<style scoped>
.nextTo {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-self: center;
  height: 280px;
}
.title {
  font-family: "Playfair Display";
  font-size: 26px;
  font-weight: lighter;
  align-self: center;
  margin-bottom: 35px;
}
.contentarea {
  display: flex;
  flex-direction: column;
  margin-top: 50px;
}
.button {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}

@media only screen and (max-width: 1200px) {
  .title {
    font-size: 22px;
  }
  .contentarea{
    margin-left: 120px;
    margin-right: 120px;
  }
}

@media only screen and (max-width: 1000px) {
  .title {
    font-size: 20px;
  }
  
}
</style>
