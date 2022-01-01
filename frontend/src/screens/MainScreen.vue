<template>
  <div>
    <div class="mainSection">
      <div class="container">
        <details class="single-sestion">
          <summary class="section-title">{{$t('yourMemberGroups')}}</summary>
          <div v-for="group in myGroups" :key="group.id">
            <Group
              v-bind:group="group"
              v-show="true"
              v-bind:requestUser="requestUser"
            />
          </div>
        </details>

        <details class="single-sestion">
          <summary class="section-title">{{$t('yourAdminGroups')}}</summary>

        </details>

        <details class="single-sestion">
          <summary class="section-title">{{$t('yourProjects')}}</summary>
          <div v-for="project in myProjects" :key="project.id">
            <Project v-bind:project="project" />
          </div>
        </details>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Group from "../components/groups/Group.vue";
import Project from "../components/projects/Project.vue";

export default {
  name: "mainScreen",
  components: {
    Group,
    Project,
  },
  data() {
    return {
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      myGroups: [],
      myProjects: [],
    };
  },
  methods: {
    ifUser() {
      if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("unauthorized")
      ) {
        // window.location.href = "../accounts/login/?next=/#/"
      }
    },
  },

  created() {
    this.ifUser();
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint2 = `api/user/projects`;
    let data2 = await apiService(endpoint2);

    var projects = [];
    var cnt = 2;
    var nextPage = data2.next != null ? true : false;
    for (var project of data2.results) {
      projects.push(project);
    }

    while (nextPage) {
      await apiService(endpoint2 + "?page=" + cnt).then((data2) => {
        cnt += 1;
        nextPage = data2.next != null ? true : false;
        for (var project of data2.results) {
          projects.push(project);
        }
      });
    }

    let endpoint = `api/user/groups`;
    let data = await apiService(endpoint);
    var groups = [];
    //
    cnt = 2;
    nextPage = data.next != null ? true : false;
    for (var group of data.results) {
      groups.push(group);
    }

    while (nextPage) {
      await apiService(endpoint + "?page=" + cnt).then((data) => {
        cnt += 1;
        nextPage = data.next != null ? true : false;
        for (var group of data.results) {
          groups.push(group);
        }
      });
    }

    return next((vm) => {
      vm.myGroups = groups;
      vm.myProjects = projects;
    });
  },
};
</script>

<style>
.single-sestion{
  /* border: solid var(--v-background-lighten2); */
  /* background-color: var(--v-background-lighten2) ; */
  border-radius: 16px;

}
details {
   font-family: "Petrona";
  background-color: var(--v-primary-lighten3);
  /* opacity: 0.6; */
  padding: 4px 6px;
  font-size: 1.7em;
  font-weight: 700;
  border: none;
  box-shadow: 3px 3px 4px rgba(75, 73, 73, 0.534);
  cursor: pointer;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 900px;
  justify-content: center; 
  transition: 1s transform ease;

}

summary {
  border: 4px solid transparent;
  text-transform: uppercase;
  outline: none;
  transition: all 1s ease;
  padding: 1rem;
  display: block;
  padding-left: 2.2rem;
  position: relative;
  cursor: pointer;
}

summary:before {
  content: "";
  border-width: 0.5rem;
  border-style: solid;
  border-color: transparent transparent transparent var(--v-accent-base);
  position: absolute;
  top: 1.6rem;
  left: 1rem;
  transform: rotate(0);
  transform-origin: 0.2rem 50%;
  transition: 1s transform ease;
}

details summary::-webkit-details-marker {
  display: none;
  transition: all 0.5s ease;
}
details[open] > summary:before {
  transform: rotate(90deg);
  transition: all 0.5s ease;
}
details[open] summary ~ * {
  animation: sweep 2s ease-in-out;
}

.row{
  margin-top: 100px;
}

.section-title{
  text-align: center;
  padding: 15px 26px;
  /* border: solid var(--v-background-lighten2); */
  /* background-color: var(--v-background-lighten2) ; */
  border-radius: 16px;
  margin: 10px auto;
  }

  .mainSection{
    margin: 50px auto;
  }
</style>
