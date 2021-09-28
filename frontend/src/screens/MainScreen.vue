<template>
  <div class="row">
    <div class="col-lg-12 col-xl-6 ">
      <div class="container">
        <Groups :groups="myGroups" />
        <div style="margin-top: 20px;">
          <Projects />
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
import Groups from "../components/user/Groups.vue";
import Projects from "../components/user/Projects.vue";
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import UserProjects from "../components/user/UserProjects.vue";
import { apiService } from "@/common/api.service.js";

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
      myGroups: [],
    };
  },
  methods: {
    getString,
    getColor,
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `api/user/`;
    let data = await apiService(endpoint)
    return next((vm) => vm.myGroups = data.groups);
  },
};
</script>

<style></style>
