<template>
  <div>
    <div class="allTitle">
      <div class="nextToGroups">
        <div class="groupsTitle">
          {{ getString("groups", "groups").toUpperCase() }} ({{
            allGroups
          }})
        </div>
      </div>
    </div>

    <div class="allGroups">
     <div v-for="group in groups" :key="group.id">
        <Group
          v-bind:group="group"
          v-show="check(group.name)"
          v-bind:requestUser="requestUser"
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
                  :length="Math.ceil(allGroups / 4)"
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
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
// import Sort from "../../components/UI/Sort.vue";
// import Search from "../../components/UI/Search.vue";
import { apiService } from "@/common/api.service.js";
import Group from "../components/groups/Group.vue";
export default {
  name: "groupsScreen",
  components: { Group },
  data() {
    return {
      page: 1,
      allGroups: null,
      groups: [],
      searchName: "",
      requestUser: "",
      sortOptions: [
        [getString("groups", "name"), this.sortByName],
        [getString("groups", "membersNumberSort"), this.sortByMembers],
      ],
      
    };
  },
  methods: {
    getString,
    getColor,
    async getAllGroups() {
      let endpoint = "api/groups/";
      let data = await apiService(endpoint);
      this.allGroups = data["count"];

      for (var group of data["results"]) {
        this.groups.push(group);
      }
    },
    async getOnePageGroups() {
      let endpoint = `api/groups/?page=${this.page}`;
      let data = await apiService(endpoint);
      this.groups = [];
      for (var group of data["results"]) {
        this.groups.push(group);
      }
    },
    moreGroups() {
      this.getAllGroups();
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
      this.groups = this.groups.sort((a, b) => a.count_user - b.count_user);
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
  },

  created() {
    this.getAllGroups();
    this.setRequestUser();
    document.title = this.getString("groups", "pageTitle");
  },
  watch: {
    page: function() {
      this.getOnePageGroups();
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
