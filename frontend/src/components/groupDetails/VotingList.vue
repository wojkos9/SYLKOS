<template>
  <div class="votingList">
    <div class="votingsListTitle">
      {{ getString("votingsList", "title") }}
    </div>
    <div class="votingsList">
      <ol>
        <li v-for="(voting, index) in votings" v-bind:key="index">
          <votings-list-element :votingDetails="voting" :id="id" />
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
import VotingsListElement from "./VotingsListElement.vue";
import { getString } from "@/language/string.js";

export default {
  name: "VotingList",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      votings: [
        {
          title: "Inwestycje na rok 2022",
          expirationDate: "21.12.2021",
          projects: [
            "remont placu zabaw",
            "parking w miejsce łąki",
            "siłownia na powietrzu",
          ],
        },
        {
          title: "Remonty 2021",
          expirationDate: "21.11.2021",
          projects: [
            "remont placu zabaw",
            "remont śmietnika",
            "remont klatki schodowej",
          ],
        },
        {
          title: "Boisko 2021",
          expirationDate: "21.10.2021",
          projects: [
            "boisko do siatkówki",
            "boisko do piłki nożnej",
            "boisko do koszykówki",
          ],
        },
      ],
    };
  },
  methods: {
    getString
  },
  components: {
    VotingsListElement,
  },
};
</script>

<style scoped>

  .votingsListTitle{
    font-family: "playfair display";
    font-weight: 700;
    margin-bottom: 40px;
    margin-top: 30px;
    text-align: center;
  }
  
  .votingList{
    border-radius: 10px;
    background-color: #f2f6fa;
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom:5px;
    padding-top: 10px;
    margin-top: 30px;
    margin-left: 10px;
  }
  </style>
