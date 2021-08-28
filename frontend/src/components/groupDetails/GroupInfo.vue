<template>
  <div>
    <div class="singleInfo">{{ getString("groupInfo", "region") }}: {{ region }}</div>
    <div class="singleInfo">{{ getString("groupInfo", "areaType") }}: {{ areaType }}</div>
    <div class="singleInfo">{{ getString("groupInfo", "usersNumber") }}: {{ usersNumber }}</div>
    <div class="singleInfo">{{ getString("groupInfo", "activeVotings") }}: {{ activeVotings }}</div>
    <div class="singleInfo">
      {{ getString("groupInfo", "registeredProjects") }}: {{ registeredProjects }}
    </div>
    <div class="singleInfo">
      {{ getString("groupInfo", "yearCosts")
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
