<template>
  <div>
    <router-link :to="{ name: route }">
      <div :style="button" v-if="!hover" @click="fun">
        <div
          @mouseover="hover = true"
          @mouseleave="hover = false"
          :class="{ active: hover }"
        >
          {{ title.toUpperCase() }}
        </div>
      </div>
      <div :style="buttonHovered" v-else @click="fun">
        <div
          @mouseover="hover = true"
          @mouseleave="hover = false"
          :class="{ active: hover }"
        >
          {{ title.toUpperCase() }}
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
export default {
  name: "Button",
  props: ["title", "fun", "route"],
  data() {
    return {
      role: "admin",
      hover: false,
    };
  },
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
    buttonHovered() {
      return {
        backgroundColor: "#93abc4",
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

<style>
.active {
  cursor: pointer;
  /* background-color: #93abc4 !important; */
}
</style>
