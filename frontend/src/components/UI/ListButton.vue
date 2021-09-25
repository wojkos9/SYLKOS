<template>

  <v-container fluid >
    <v-row>
      <v-col cols="12">
        <v-combobox color="secondary"
          v-model="select"
          :items="options"
          :label="title"
          item-text="name"
          item-value="route"
        ></v-combobox>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getString } from "@/language/string.js";
export default {
  name: "listButton",
  props: ["title", "options"],
  data() {
    return {
      sort: "",
      select: '',
    };
  },
  methods: {
    getString,
  },
  watch: {
    select: function(val) {
      this.$router.push(val.route);
    },
  },
};
</script>

<style scoped>
.search {
  width: 200px;
  margin-right: 10px;
}
li.md-list-item {
  list-style-type: none;
}
.v-list .v-list-item--active .v-list-item__title {
  color: #ffd54f !important;
}
</style>
