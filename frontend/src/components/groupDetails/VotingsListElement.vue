<template>
  <div class="area">
    <div class="topSection">
      <div class="nextTo" @click="changeDisplay">
        <div class="votingName">
          {{ votingDetails.title }}
        </div>
        <div
          class="expandIcon"
          style="color: #93abc4"
          v-if="!showDetails"
        >
          <v-mdi name="mdiPlusBox"></v-mdi>
        </div>
        <div
          class="expandIcon"
          style="color: red"
          v-else
        >
          <v-mdi name="mdiMinusBox"></v-mdi>
        </div>
      </div>
    </div>
    <div class="bottomSection" v-if="showDetails">
      <div class="expirationDate">
        {{ getString("votingsList", "expirationDate") }}:
        {{ votingDetails.expirationDate }}
      </div>
      <div class="projectsList">
        <ul>
          <li
            v-for="(project, index) in votingDetails.projects"
            v-bind:key="index"
          >
            {{ project }}
          </li>
        </ul>
      </div>
      <div class="goToVotingLink">
        <router-link :to="{ name: 'voting', params: { id: id, vId: 1 } }"
          ><h3>{{ getString("votingsList", "goToVoting") }}</h3></router-link
        >
      </div>
    </div>
    <div class="bottomSection" v-else></div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
export default {
  name: "VotingsListElement",
  props: ["votingDetails", "id"],
  data() {
    return {
      showDetails: false,
    };
  },
  methods: {
    getString,
    changeDisplay() {
      this.showDetails = !this.showDetails;
      console.log(this.showDetails);
    },
  },
};
</script>
<style
  link
  rel="stylesheet"
  href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
  scoped
>
.area {
  /* border: solid 1px black; */
  margin-bottom: 10px;
}
.nextTo{
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding: 7px;
}
.nextTo:hover{
  background-color: #C0CFE6;
  cursor:pointer
}
.topSection {
  display: flex;
  padding: 10px;
}
.votingName {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
}
.bottomSection {
  align-items: flex-start;
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}
.expirationDate,
.goToVotingLink {
  margin: 10px;
  padding-left: 10px;
}
.expandIcon:hover{
  cursor: pointer;
}
li{
  padding-bottom: 2px;
}
</style>
