<template>
  <div>
    <div class="singleInfo">{{ getString("groups", "region") }}: {{ region }}</div>
    <div class="singleInfo">{{ getString("groups", "areaType") }}: {{ areaType }}</div>
    <div class="singleInfo">{{ getString("groups", "usersNumber") }}: {{ usersNumber }}</div>
    <div class="singleInfo">{{ getString("groups", "activeVotings") }}: {{ activeVotings }}</div>
    <div class="singleInfo">
      {{ getString("groups", "registeredProjects") }}: {{ registeredProjects }}
    </div>
    <div class="singleInfo">
      {{ getString("groups", "yearCosts")
      }}{{ moment(new Date()).format("YYYY") }}: {{ yearCosts }}
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";

export default {
  name: "GroupInfo",
  props: [
    "region",
    "areaType",
    "usersNumber",
    "activeVotings",
    "registeredProjects",
    "yearCosts",
  ],
  methods: {
    getString,
  },

  components: {},
};
</script>

<style scoped>
.singleInfo{
  padding: 10px;
}
</style>
