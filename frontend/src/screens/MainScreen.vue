<template>
<div>
  <div class="row">
    <div class="container">
      <div class="section-title">Grupy, do których należysz</div>
      <div v-for="group in myGroups" :key="group.id">
        <Group
          v-bind:group="group"
          v-show="true"
          v-bind:requestUser="requestUser"
        />
      </div>

      <!-- <div style="margin-top: 20px;">
        <Projects />
      </div> -->
    </div>
  </div>
  <!-- <div class="col-lg-12 col-xl-5 ">
    <div class="container">
      <user-projects />
    </div>

    <div class="col-sm-1 " />
  </div> -->
  </div>
</template>

<script>
// import Projects from "../components/user/Projects.vue";
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
// import UserProjects from "../components/user/UserProjects.vue";
import { apiService } from "@/common/api.service.js";
import Group from "../components/groups/Group.vue";

export default {
  name: "mainScreen",
  components: {
    // Projects,
    Group,
    // UserProjects,
  },
  data() {
    return {
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      myGroups: [],
    };
  },
  methods: {
    getString,
    getColor,
    ifUser(){
       if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("unauthorized")
      ) {
        // window.location.href = "../accounts/login/?next=/#/"
      } 
     

    }
  },
  created(){
    this.ifUser()
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `api/user/`;
    let data = await apiService(endpoint);
    return next((vm) => (vm.myGroups = data.groups));
  },
};
</script>

<style></style>
