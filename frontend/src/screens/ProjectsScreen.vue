<template>
  <div >
   <ProjectsTitle 
    v-bind:numberOfAllProjects="allProjects" 
    v-on:changeSearchName="makeSth($event)"
    />

   <div class="options">
     <Sort :options="sortOptions"/>
     <div class="searchOptions"> <Search v-on:changeSearchName="makeSth($event)" :title="getString('projects', 'group')"/>
      <Search v-on:changeSearchName="makeSth($event)" :title="getString('projects', 'name')"/>
      </div>
    </div>

    <div class="allProjects">
      <div v-for="project in projects" :key="project.id">
        <Project
          v-show="check(project.name)"
          v-bind:project="project" 
        />
      </div>
      <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              class="my-4"
              :length="Math.ceil(allProjects/4)"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>

    </div>

    

  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import ProjectsTitle from '../components/projects/ProjectsTitle.vue';
import Project from '../components/projects/Project.vue';
import Sort from '../components/UI/Sort.vue';
import Search from '../components/UI/Search.vue';
import { apiService } from "@/common/api.service.js";


export default {
  name: "projectsScreen",
  components: {ProjectsTitle, Project, Sort, Search},
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
      sortOptions: [ [getString("groups", "name"), this.sortByName],  [getString("groups", "membersNumberSort"), this.sortByMembers]],
      id: 1,
      page: 1,
    };
  },
  methods: {
    getString,
    getColor,
    async getAllProjects() {
      const data = await apiService("/api/projects/");
      this.allProjects = data["count"]
      for(var project of data["results"]){
        this.projects.push(project)
      }
    },
    async getOnePageProjects(){
      let endpoint = `api/projects/?page=${this.page}`
      let data = await apiService(endpoint);
      this.projects = [];
       for(var project of data["results"]){
        this.projects.push(project)
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

  created(){
    this.getAllProjects()
    this.setRequestUser()
    document.title = this.getString("projects", "pageTitle")
  },
  watch: {
    page: function() {
      this.getOnePageProjects();
    },
    
  }
};
</script>

<style>
.allProjects{
  margin-top: 87px;
  margin-bottom: 50px;
}

.center{
  display: flex;
  flex-direction: column;
  align-items: center;
}

.options{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-top: -110px;
  margin-bottom: -30px;
}

.searchOptions{
  display: flex;
  flex-direction: column;
}
@media only screen and (max-width: 1600px) {

.options{
    margin-top: 15px;
    justify-content: center;
    margin-bottom:0px
  }
  .searchOptions{
    flex-direction: row;
  }
}
</style>
