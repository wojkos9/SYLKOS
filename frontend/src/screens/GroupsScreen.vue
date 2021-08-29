<template>
  <div>
    <GroupTitle
      v-bind:numberOfAllGroups="allGroups"
      v-on:changeSearchName="makeSth($event)"
    />

    <div class="options">
      <Search
        v-on:changeSearchName="makeSth($event)"
        :title="getString('groups', 'name')"
      />
      <Sort :options="sortOptions" />
    </div>

    <div class="allGroups">
      <div v-for="group in groups" :key="group.id">
        <Group
        v-show="check(group.name)"
        v-bind:name="group.name"
        v-bind:desc="group.description"
        v-bind:members="group.count_user"
        v-bind:picture="image"
        v-bind:id="group.id"
        v-bind:allMembers="group.members"
        v-bind:requestUser="requestUser"
      />
      </div>
      <!-- <Group
        v-show="check(this.title)"
        v-bind:name="title"
        v-bind:desc="desc"
        v-bind:members="members"
        v-bind:picture="image"
        v-bind:id="id"
      />
      <Group
        v-show="check(this.title)"
        v-bind:name="title"
        v-bind:desc="desc"
        v-bind:members="members"
        v-bind:picture="image"
        v-bind:id="id"
      />
      <Group
        v-show="check(this.name)"
        v-bind:name="name"
        v-bind:desc="desc"
        v-bind:members="members"
        v-bind:picture="image"
        v-bind:id="id"
      />
      <Group
        v-show="check(this.title)"
        v-bind:name="title"
        v-bind:desc="desc"
        v-bind:members="members"
        v-bind:picture="image"
        v-bind:id="id"
      /> -->
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import GroupTitle from "../components/groups/GroupTitle.vue";
import Group from "../components/groups/Group.vue";
import Sort from "../components/UI/Sort.vue";
import Search from "../components/UI/Search.vue";
import { apiService } from "@/common/api.service.js";

export default {
  name: "groupsScreen",
  components: { GroupTitle, Group, Sort, Search },
  data() {
    return {
      name: "Zatorze",
      title: "Osiedle Kwiatowe",
      desc:
        "Boisko do siatkówki plażowej w miejscu obecnego kamienistego placu " +
        "przy ulicy 3 Maja. Boisko do siatkówki plażowej w miejscu obecnego " +
        "kamienistego placu przy ulicy MajaBoisko do siatkówki plażowej w " +
        "miejscu obecnego kamienistego placu przy ulicy MajaBoisko do " +
        "siatkówki plażowej w miejscu obecnego kamienistego placu przy ulicy " +
        "3 Maja",
      allGroups: 34,
      groups : [],
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      sideDrawer: false,
      searchName: "",
      requestUser:"",
      sortOptions: [
        [getString("groups", "name"), this.sortByName],
        [getString("groups", "membersNumberSort"), this.sortByMembers],
      ],
      id: 4,
    };
  },
  methods: {
    getString,
    getColor,
    async getAllGroups() {
      const data = await apiService("/api/groups/");
      this.allGroups = data["count"]
      for(var group of data["results"]){
        console.log(group)
        this.groups.push(group)
      }
    },
    makeSth(str) {
      this.searchName = str;
    },
    check(str) {
      return str.toLowerCase().includes(this.searchName.toLowerCase());
    },
    sortByName() {
      console.log("sortByName");
    },
    sortByMembers() {
      console.log("sortByMembers");
      this.groups = this.groups.sort((a, b) => a.count_user - b.count_user)
    },
    setRequestUser(){
      this.requestUser = window.localStorage.getItem("username")
    },
  },
  
  created(){
    this.getAllGroups()
    this.setRequestUser()
  }
};
</script>

<style>
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

.allGroups{
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
