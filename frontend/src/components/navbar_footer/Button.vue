<template>
  <div>
    <router-link :to="{ name: route }">
      <v-btn
        :style="button"
        elevation="2"
        rounded
        color="secondary "
      >{{ title.toUpperCase() }}</v-btn>
    </router-link>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
export default {
  name: "Button",
  props: ["title", "route"],
  methods: {
    getString,
    getColor,
  },
  computed: {
    button() {
      return {
        backgroundColor: this.getColor("backgroundcolor"),
        alignSelf: "center",
        borderRadius: "35px",
        marginLeft: "10px",
        padding: "9px",
        width: "150px",
        textAlign: "center",
      };
    },
  },
};
</script>
