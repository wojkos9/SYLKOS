<template>
  <div class="search">
    <div class="md-layout-item">
      <md-field>
        <label for="sortGroups"
          ><md-icon>sort</md-icon> {{ getString("groups", "sort") }}</label
        >
        <md-select v-model="sort" name="sortGroups" id="sortGroups">
          <md-option
            v-for="(option, index) in options"
            :key="index"
            :value="index"
            class="sortGroups"
            >{{ option[0] }}</md-option
          >
        </md-select>
      </md-field>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
export default {
  name: "searchEngine",
  props: ["options"],
  data() {
    return {
      sort: "",
    };
  },
  methods: {
    getString,
  },
  watch: {
    sort: function(val) {
      this.options[val][1]()
    },
  },
};
</script>

<style scoped>
.search {
  width: 200px;
  margin-right: 10px;
}
</style>
