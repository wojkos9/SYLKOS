<template>
  <div>
    <GroupTitle
      v-bind:numberOfAllGroups="243"
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
      <Group
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
      />
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
      members: 34,
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      sideDrawer: false,
      searchName: "",
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
    },
  },
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
  margin-top: 87px
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
