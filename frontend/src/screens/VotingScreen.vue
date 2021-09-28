<template>
<<<<<<< HEAD
    <div >
        <div>
            <voting-header 
            :date="date"
            :group="group"
            />
        </div>
        <div v-for="(project, index) in voting.projects" :key="index">{{project}}</div>

        <div class="projects">
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            
        </div>
        <div class="submitButton">
            <button-submit-vote/>
        </div>
=======
  <div>
    <div>
      <voting-header :date="date" :group="group" />
>>>>>>> tmpBranch
    </div>
    <div class="projects">
      <div v-for="(project, index) in voting.projects" :key="index">
        <voting-project
          v-bind:title="project.name"
          v-bind:description="project.description"
          v-bind:price="project.budget"
          v-bind:likes="likes"
          v-bind:dislikes="dislikes"
          v-bind:id="project.id"
          v-on:change="setUserVotedFor($event)"
        />
      </div>
    </div>
    <div class="submitButton">
      <button-submit-vote />
    </div>
  </div>
</template>

<script>
import VotingHeader from "../components/voting/VotingHeader.vue";
import ButtonSubmitVote from "../components/voting/ButtonSubmitVote.vue";
import VotingProject from "../components/voting/VotingProject.vue";
import { apiService } from "@/common/api.service.js";
export default {
  name: "votingScreen",
  props: {
    id: {
      type: Number,
      required: true,
    },
    vId: {
      type: Number,
      required: true,
    },
  },
  // props: ['date', 'group', 'title', 'description', 'price', 'likes', 'dislikes', 'userVotedFor'],
  data() {
    return {
      date: "24 listopada 2021",
      group: "Osiedle Kwiatowe",
      title: "Łąka przy osiedlowym strumyku",
      description:
        "Miejsce do relaksu dla mieszkańców osiedla. Obok strumyka przepływającego " +
        "przez osiedle planujemy zasadzić drzewa i kwiaty, postawić ławki i dać możliwość odpoczynku z naturą.",
      price: "10 000",
      likes: "21",
      dislikes: "37",
      previousUserVote: 0,
      userVotedFor: 0,
      voting: {},
    };
  },
  methods: {
    setUserVotedFor(projectId){
      if(this.previousUserVote == 0) this.previousUserVote = projectId;
      else this.previousUserVote = this.userVotedFor;
      this.userVotedFor = projectId
      document.getElementById(this.previousUserVote).style.backgroundColor = "red"
      document.getElementById(projectId).style.backgroundColor = "green"
    },
  },
  components: {
    VotingHeader,
    ButtonSubmitVote,
    VotingProject,
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/voting/${to.params.vId}/`;
    let data = await apiService(endpoint);
    console.log(data);
    return next((vm) => (vm.voting = data));
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
.submitButton {
  display: flex;
  justify-content: flex-end;
  margin-right: 120px;
  margin-bottom: 40px;
}
</style>
