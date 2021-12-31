<template>
  <div>
    <div class="allTitle">
      <div class="nextToGroups">
        <div class="groupsTitle">
          {{ $t("projectsScreen.title").toUpperCase() }} ({{
            allProjects
          }})
        </div>
      </div>
    </div>

    <div class="allGroups">
     <div v-for="project in projects" :key="project.id">
        <Project
          v-show="check(project.name)"
          v-bind:project="project" 
        />
      </div>
      <div class="text-center">
        <v-container>
          <v-row justify="center">
            <v-col cols="8">
              <v-container class="max-width">
                <v-pagination
                  v-model="page"
                  class="my-4"
                  :length="Math.ceil(allProjects / 4)"
                ></v-pagination>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Project from "../components/projects/Project.vue";
export default {
  name: "groupsScreen",
  components: { Project },
  data() {
    return {
      projects : [],
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      allProjects: '',
      searchName: "",
      id: 1,
      page: 1,
    };
  },
  methods: {
    async getAllProjects() {
      const data = await apiService("/api/projects/");
      this.allProjects = data["count"]
      for(var project of data["results"]){
        if (project.images.length == 0){
        console.log("tak  ")
        project.images=[{image : "images/no_picture.png"}]

      }
        this.projects.push(project)
      }
    },
    async getOnePageProjects(){
      let endpoint = `api/projects/?page=${this.page}`
      let data = await apiService(endpoint);
      this.projects = [];
       for(var project of data["results"]){
        // if (project.images.length == 0){
        // console.log("tak  ")
        // project.images=[{image : "images/no_picture.png"}]
        this.projects.push(project)
      // }
      }
    },
    makeSth(str){
      this.searchName = str
    },
    check(str){
      return str.toLowerCase().includes(this.searchName.toLowerCase())
    },
    sortByName(){
      console.log("sortByName")
    },
    sortByMembers(){
      console.log("sortByMembers")
    },
    setRequestUser(){
      this.requestUser = window.localStorage.getItem("username")
    },
  },

  created() {
    this.getAllProjects()
    this.setRequestUser()
    document.title = this.$t("projectsScreen.pageTitle")
  },
  watch: {
    page: function() {
      this.getOnePageProjects();
    },
  },
};
</script>

<style>
.groupsTitle {
  align-self: center;
  font-size: 2rem;
  text-align: center;
}

.nextToGroups {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: nowrap;
}

.allTitle {
  margin-bottom: 50px;
  margin-top: 50px;
  width: 100%;
}

.center {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.options {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-top: -280px;
}

.allGroups {
  margin-top: 87px;
  margin-bottom: 50px;
}
@media only screen and (max-width: 1100px) {
  .options {
    justify-content: center;
  }
  .search {
    margin-right: 50px;
    margin-left: 50px;
  }
}
</style>
