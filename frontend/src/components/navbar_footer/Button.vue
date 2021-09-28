<template>
  <div>
    <router-link :to="{ name: route }">
      <v-btn
        :style="button"
        elevation="2"
        rounded
        class="p-2"
        color="secondary"
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
        marginLeft: "10px",
        width: "150px",
        height: '40px',
        textAlign: "center",
        color: "black"
      };
    },
  },
};
</script>
