<template>
  <div>
    <div class="allTitle">
      <div class="nextToGroups">
        <div class="groupsTitle">
          {{ $t("votingTypesEdit.title").toUpperCase() }}
        </div>
      </div>
    </div>

    <div class="allGroups">
      <div
        v-for="votingType in votingTypes"
        :key="votingType.name"
        class="d-flex justify-content-center"
      >
          <div class="singleGroup">{{ votingType.name }} <router-link
        :to="{
          name: editAction, params: {nameId:votingType.name}
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
          @click="deleteVotingType(votingType.name)"
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
                  :length="Math.ceil(allVotingTypes / 4)"
                ></v-pagination>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <DialogWithUser
      :desc="$t('votingEdit.delete')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :yes="$t('votingEdit.accept')"
      :no="$t('votingEdit.cancel')"
    />

    <DialogWithUser
      :desc="$t('votingEdit.success')"
      :nextAction="nextFunction2"
      :backAction="backFunction2"
      :dialog="dialog2"
      :no="$t('votingEdit.back')"
    />

    </div>

    


  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import DialogWithUser from '../../components/UI/DialogWithUser.vue';

export default {
  name: "votingTypesEditListScreen",
  components:{
    DialogWithUser
  },
  data() {
    return {
      page: 1,
      dialog: false,
      dialog2: false,
      deleteVotingTypeId: null,
      allVotingTypes: null,
      votingTypes: [],
      sideDrawer: false,
      searchName: "",
      editAction: "votingTypeEdit",
      requestUser: "",
    };
  },
  methods: {
    async getOnePageVotingTypes() {
      let endpoint = `api/voting_type/?page=${this.page}`;
      let data = await apiService(endpoint);
      this.allVotingTypes = data["count"]
      this.votingTypes = [];
      for (var votingType of data["results"]) {
        this.votingTypes.push(votingType);
      }
    },
    async deleteVotingType(name){
      this.deleteVotingTypeId = name;
      this.dialog = true;
    },
    moreGroups() {
      this.getAllVotings();
    },
    makeSth(str) {
      this.searchName = str;
    },
    // check(str) {
    //   return str.toLowerCase().includes(this.searchName.toLowerCase());
    // },
    // sortByName() {
    //   console.log("sortByName");
    // },
    // sortByMembers() {
    //   this.groups = this.groups.sort((a, b) => a.count_user - b.count_user);
    // },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    async nextFunction(){
      this.dialog = false
      let endpoint = `api/voting_type/${this.deleteVotingTypeId}/`;
      await apiService(endpoint, 'DELETE')
      .then(data => {
        console.log(data);
        this.page = 1;
        this.getOnePageVotingTypes();
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
    this.getOnePageVotingTypes();
    this.setRequestUser();
    document.title = this.$t("votingTypesEdit.pageTitle");
  },
  watch: {
    page: function() {
      this.getOnePageVotingTypes();
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
