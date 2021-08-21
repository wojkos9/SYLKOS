/* eslint-disable */
<template>
  <div class="row">
    <div class="col-lg-12 col-xl-6 ">
      <div class="container">
        <groups />
        <div style="margin-top: 20px;">
          <projects />
        </div>
      </div>
    </div>
    <div class="col-lg-12 col-xl-5 ">
      <div class="container">
        <user-projects />
      </div>

      <div class="col-sm-1 " />
    </div>
  </div>
</template>

<script>
import Groups from "../components/user/groups.vue";
import Projects from "../components/user/projects.vue";
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import UserProjects from "../components/user/userProjects.vue";

export default {
  name: "mainScreen",
  components: {
    Groups,
    Projects,
    UserProjects,
  },
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

<style></style>
