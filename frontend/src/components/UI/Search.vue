<template>
  <div>
    <md-field class="search">
      <label for="searchName">{{title}}</label>
      <md-input
        name="searchName"
        id="searchName"
        v-model="name"
        autocomplete="given-name"
        v-on:change="clearInput"
      />
    </md-field>
  </div>
</template>

<script>
export default {
  name: "searchEngine",
  props: ["title"],
  data() {
    return {
      name: "",
    };
  },
  methods: {
    clearInput() {
      this.name = "";
      this.$emit("changeSearchName", "");
    },
  },
  watch: {
    name: function(val) {
      this.$emit("changeSearchName", val);
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
