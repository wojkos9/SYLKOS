<template>
  <div>
    <div class="allTitle">
      <div class="nextToGroups">
        <div class="groupsTitle">
          {{ $t("projectsEdit.title").toUpperCase() }}
        </div>
      </div>
    </div>

    <div class="allGroups">
      <div
        v-for="project in projects"
        :key="project.id"
        class="d-flex justify-content-center"
      >
        
          <div class="singleGroup">{{ project.name }} <router-link
        :to="{
          name: editAction, params: { id:project.id}
        }"
      >
        <v-card-text
          style=" position: absolute; top: 20px; right: 10px; width: 30px; "
        >
          <v-fab-transition>
            <v-btn color="secondary" dark absolute top right fab>
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </router-link>

        <v-card-text
          style=" position: absolute; top: 20px; right: 80px; width: 20px;"
          @click="deleteProject(project.id)"
        >
          <v-fab-transition>
            <v-btn color="secondary" dark absolute top right fab>
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
    </div>
      
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
      <DialogWithUser
      :desc="$t('projectsEdit.delete')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :yes="$t('projectsEdit.accept')"
      :no="$t('projectsEdit.cancel')"
    />

    <DialogWithUser
      :desc="$t('projectsEdit.success')"
      :nextAction="nextFunction2"
      :backAction="backFunction2"
      :dialog="dialog2"
      :no="$t('projectsEdit.back')"
    />

    </div>

    


  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import DialogWithUser from '../../components/UI/DialogWithUser.vue';

export default {
  name: "projectsEditListScreen",
  components:{
    DialogWithUser
  },
  data() {
    return {
      page: 1,
      dialog: false,
      dialog2: false,
      deleteProjectId: null,
      allProjects: null,
      projects: [],
      sideDrawer: false,
      searchName: "",
      editAction: "projectEdit",
      requestUser: "",
      sortOptions: [
        [this.$t("projects.name"), this.sortByName],
        [this.$t("projects.membersNumberSort"), this.sortByMembers],
      ],
    };
  },
  methods: {
    async getAllProjects() {
      this.projects = [];
      let endpoint = "api/projects/";
      let data = await apiService(endpoint);
      this.allProjects = data["count"];

      for (var project of data["results"]) {
        this.projects.push(project);
      }
    },
    async getOnePageGroups() {
      let endpoint = `api/projects/?page=${this.page}`;
      let data = await apiService(endpoint);
      this.projects = [];
      for (var project of data["results"]) {
        this.projects.push(project);
      }
    },
    async deleteProject(id){
      this.deleteProjectId = id;
      this.dialog = true;
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
      this.projects = this.projects.sort((a, b) => a.count_user - b.count_user);
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    async nextFunction(){
      this.dialog = false
      let endpoint = `api/projects/${this.deleteProjectId}/`;
      await apiService(endpoint, 'DELETE')
      .then(data => {
        console.log(data);
        this.page = 1;
        this.getAllProjects();
        this.dialog2 = true;
      })
      // this.$router.push({name:"admin"})
    },
    backFunction(){
      this.dialog = false
    },
    nextFunction2(){
      this.dialog2 = false
      this.$router.push({name:"admin"})
    },
    backFunction2(){
      this.dialog2 = false
    }
  },

  created() {
    this.getAllProjects();
    this.setRequestUser();
    document.title = this.$t("projectsScreen.pageTitle");
  },
  watch: {
    page: function() {
      this.getOnePageProjects();
    },
  },
};
</script>

<style scoped>
.singleGroup {
  padding: 30px;
  font-size: 1.5rem;
  width: 800px;
  margin-bottom: 15px;
  /* background: red;; */
  border:none;
  -webkit-box-shadow: -10px 10px 34px -21px rgba(120, 144, 156, 1);
-moz-box-shadow: -10px 10px 34px -21px rgba(120, 144, 156, 1);
box-shadow: -10px 10px 34px -21px rgba(120, 144, 156, 1);
  position: relative
}
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
