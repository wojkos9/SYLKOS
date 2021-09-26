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
          v-bind:name="project.name"
          v-bind:desc="project.description"
          v-bind:price="project.budget"
          v-bind:picture="image"
          v-bind:id="project.id"  
        />
      </div>
    </div>

   <!-- <Project
    v-show="check(this.title)"
    v-bind:name="title"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    v-bind:id="id"
    />
    <Project
    v-show="check(this.title)"
    v-bind:name="title"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    v-bind:id="id"
    />
    <Project
    v-show="check(this.name)"
    v-bind:name="name"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    v-bind:id="id"
    />
    <Project
    v-show="check(this.title)"
    v-bind:name="title"
    v-bind:desc="desc"
    v-bind:members="members"
    v-bind:picture="image"
    v-bind:id="id"
    /> -->
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
      name:"Zatorze",
      title: "Osiedle Kwiatowe",
      desc: "Boisko do siatkówki plażowej w miejscu obecnego kamienistego placu " +
            "przy ulicy MajaBoisko do siatkówki plażowej w miejscu obecnego " +
            "kamienistego placu przy ulicy MajaBoisko do siatkówki plażowej w " +
            "miejscu obecnego kamienistego placu przy ulicy MajaBoisko do " +
            "siatkówki plażowej w miejscu obecnego kamienistego placu przy ulicy " +
            "Maja",
      projects : [],
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      allProjects: '',
      searchName: "",
      sortOptions: [ [getString("groups", "name"), this.sortByName],  [getString("groups", "membersNumberSort"), this.sortByMembers]],
      id: 1
    };
  },
  methods: {
    getString,
    getColor,
    async getAllProjects() {
      const data = await apiService("/api/projects/");
      this.allProjects = data["count"]
      for(var project of data["results"]){
        console.log(project)
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
