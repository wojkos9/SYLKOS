<template>
  <md-list-item md-expand style="position:absolute;">
        <md-icon>
          manage_accounts
        </md-icon>
        <span class="md-list-item-text">{{
          title
        }}</span>

        <md-list slot="md-expand">
          <md-list-item class="md-inset" @click="settingsClicked">{{
            getString("navbar", "settings")
          }}</md-list-item>
          <md-list-item class="md-inset" @click="userPanelClicked">{{
            getString("navbar", "user")
          }}</md-list-item>
        </md-list>
      </md-list-item>

</template>

<script>
import { getString } from "@/language/string.js";
export default {
  name: "listButton",
  props: ["title", "options"],
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
li.md-list-item{
    list-style-type: none;
}
</style>
