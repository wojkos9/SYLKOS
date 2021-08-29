<template>
  <div class="area">
    <div class="date">
      <div style="margin-right: 8px">{{ getString("votingHeader", "voting") }}</div>
      <div>{{ date }}</div>
    </div>
    <div class="group">
      <div>{{ getString("votingHeader", "group") }}</div>
      <div>: {{ group }}</div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
export default {
  name: "votingHeader",
  props: ["date", "group"],
  data() {
    return {};
  },
  methods: {
    getString,
  },
};
</script>

<style scoped>
.area {
  align-items: center;
  background-color: yellow;
  border: solid 1px black;
  border-radius: 25px;
  display: flex;
  flex-direction: column;
  /* height: 200px; */
  justify-content: center;
  padding: 20px;
  width: 100%;
}
.date {
  display: flex;
  font-family: "playfair display";
  font-size: 50px;
  margin-bottom: 30px;
  margin-top: 20px;
}
.group {
  display: flex;
  font-family: "playfair display";
  font-size: 30px;
  margin-bottom: 20px;
}
</style>
