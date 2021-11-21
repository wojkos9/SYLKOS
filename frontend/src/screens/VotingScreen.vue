<template>
  <div>
    <!-- <div>
      <voting-header :date="voting.start_date "/>
    </div> -->
      <div class="votingTitle">
          {{ getString("votingHeader", "voting") }} ({{ voting.start_date
            
          }})
        </div>

        <!--borda-->
    <!-- <draggable
      v-model="voting.projects"
      group="votings"
      @start="drag = true"
      @end="drag = false"
    >
      <div v-for="project in voting.projects" :key="project.id">
        <VotingProject
          v-bind:project="project"
          v-on:change="setUserVotedFor($event)"
        />
      </div>
    </draggable> -->
    <div v-if="voting.voting_type == 'borda'">
       <draggable
      v-model="voting.projects"
      group="votings"
      @start="drag = true"
      @end="drag = false"
    >
      <div v-for="project in voting.projects" :key="project.id">
        <VotingProject
          v-bind:project="project"
          v-on:change="setUserVotedFor($event)"
        />
      </div>
    </draggable>
    </div>
    <div v-else-if="voting.voting_type=='majority'">
        <div v-for="project in voting.projects" :key="project.id">
        <VotingProjectSelectOne
          v-bind:project="project"
          v-on:change="setUserVotedFor($event)"
          :clicked="userVotedFor"
        />
      </div>
    </div>
  <div v-else>
    jeszcze nie obsłużony typ głosowania {{voting}}
  </div>
    

    <!--jeden wybor-->

    <!-- <div class="submitButton" @click="submitVote">
      <div :style="button">
        <div>
          {{ getString("buttonSubmitVote", "submitMyVote").toUpperCase() }}
        </div>
      </div>
    </div> -->
  <div class="buttonSubmit">
     <v-btn color="secondary darken-1" class="p-3" dark style="color:black" @click="submitVote">
        {{ getString("buttonSubmitVote", "submitMyVote").toUpperCase() }}
      </v-btn>
  </div>
  </div>
</template>

<script>
// import VotingHeader from "../components/voting/VotingHeader.vue";
import { getString } from "@/language/string.js";
import VotingProject from "../components/voting/VotingProject.vue";
import VotingProjectSelectOne from "../components/voting/VotingProjectSelectOne.vue";
import { apiService } from "@/common/api.service.js";
import draggable from "vuedraggable";

export default {
  name: "votingScreen",
  props: {
    id: {
    
      required: true,
    },
    vId: {
  
      required: true,
    },
  },

  data() {
    return {
      active: true,
      previousUserVote: 0,
      userVotedFor: 0,
      voting: {},
    };
  },
  methods: {
    getString,
    async submitVote() {
      // console.log(this.voting);

      //tutaj jest głosowanie borda
      var choice = [];
      var points = this.voting.projects.length -1;
      for (var project of this.voting.projects) {
        choice.push({ project: project.id, points: points });
        points -= 1;
      }

      //glosowanie na jeden projekt


      console.log(this.voting.id)
      console.log(choice)
      await apiService("/api/vote/", "POST", {
        voting: this.voting.id,
        choice: choice,
      }).then((data) => {
        console.log(data);
        if (data != "wrong data") {
          console.log("chyba sie udalo");
        }
      });
    },
    setUserVotedFor(projectId) {
      if (this.previousUserVote == 0) this.previousUserVote = projectId;
      else this.previousUserVote = this.userVotedFor;
      this.userVotedFor = projectId;
      document.getElementById(this.previousUserVote).style.backgroundColor =
        "rgb(217, 208, 250)";
      document.getElementById(projectId).style.backgroundColor =
        "rgb(22, 187, 50)";
    },
  },
  components: {
    VotingProjectSelectOne,
    VotingProject,
    draggable,
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/voting/${to.params.vId}/`;
    let data = await apiService(endpoint);
    console.log(data);
    return next((vm) => {
      vm.voting = data;
    });
  },
};
</script>

<style scoped>
.projects {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
}

.votingTitle{
  margin-top: 50px;
  font-size: 32px;
  text-align: center;
  margin-bottom: 30px;
}
.buttonSubmit{
  display: flex;
  justify-content: flex-end;
  margin-right: 5%;
  margin-bottom: 20px;
}
</style>
