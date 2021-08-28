<template>
  <div >
   <ProjectsTitle v-bind:numberOfAllGroups="243" v-on:changeSearchName="makeSth($event)"/>

   <div class="options">
     <Sort :options="sortOptions"/>
     <div class="searchOptions"> <Search v-on:changeSearchName="makeSth($event)" :title="getString('projects', 'group')"/>
      <Search v-on:changeSearchName="makeSth($event)" :title="getString('projects', 'name')"/>
      </div>
    </div>

   <Project
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
    />
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import ProjectsTitle from '../components/projects/ProjectsTitle.vue';
import Project from '../components/projects/Project.vue';
import Sort from '../components/UI/Sort.vue'
import Search from '../components/UI/Search.vue'

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
      members: 34,
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      searchName: "",
      sortOptions: [ [getString("groups", "name"), this.sortByName],  [getString("groups", "membersNumberSort"), this.sortByMembers]],
      id: 1
    };
  },
  methods: {
    getString,
    getColor,
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
    }
  },
};
</script>

<style>

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
