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
        v-bind:group="group"
        v-show="check(group.name)"
        v-bind:name="group.name"
        v-bind:desc="group.description"
        v-bind:members="group.count_user"
        v-bind:picture="group.image"
        v-bind:id="group.id"
        v-bind:allMembers="group.members"
        v-bind:requestUser="requestUser"
      />
      </div>
      <div v-show="ifNext" @click="moreGroups">wiecej</div>
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
      allGroups: '',
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
      next:"",
      ifNext:false,
      endpoint: "/api/groups/",
    };
  },
  methods: {
    getString,
    getColor,
    async getAllGroups() {
      var data
      if(!this.ifNext){
         data = await apiService(this.endpoint)
        this.allGroups = data["count"]
      }
      else{
          data = await apiService(this.next);
      }
      
      for(var group of data["results"]){
        this.groups.push(group)
      }

      if(data["next"] != null){
        this.next = data["next"].substr(data["next"].indexOf("/api"))
        console.log(this.next)
        this.ifNext = true
      }else{
        this.ifNext = false
      }
    },
    moreGroups(){
      this.getAllGroups()
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
