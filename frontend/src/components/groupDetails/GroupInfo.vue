<template>
  <div>
    {{ getString("groups", "region") }}: {{ region }}
    <br />
    {{ getString("groups", "areaType") }}: {{ areaType }}
    <br />
    {{ getString("groups", "usersNumber") }}: {{ usersNumber }}
    <br />
    {{ getString("groups", "activeVotings") }}: {{ activeVotings }}
    <br />
    {{ getString("groups", "registeredProjects") }}: {{ registeredProjects }}
    <br />
    {{ getString("groups", "yearCosts")
    }}{{ moment(new Date()).format("YYYY") }}: {{ yearCosts }}
  </div>
</template>

<script>
import { getString } from "@/language/string.js";

export default {
  name: "GroupInfo",
  props: ["region", "areaType", "usersNumber", "activeVotings", "registeredProjects", "yearCosts"],
  methods: {
    getString,
  },

  components: {},
};
</script>

<style scoped></style>
