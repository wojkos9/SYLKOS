<template>
  <div style="position:absolute">
    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="show" style="background-color:white; z-index:1000">
        <v-divider></v-divider>

        <v-card-text>
          panel administratora
        </v-card-text>
        <v-card-text>
          panel administratora
        </v-card-text>
        <v-card-text>
          panel administratora
        </v-card-text>
      </div>
    </v-expand-transition>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
export default {
  name: "Button",
  props: ["title", "fun", "route"],
  methods: {
    getString,
    getColor,
  },
  data() {
      return {
          show:false
      }
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

<style scoped>
v-card-text{
    background-color: white;
}
</style>
