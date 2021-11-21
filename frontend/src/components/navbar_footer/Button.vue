<template>
  <div>
    <router-link :to="{ name: route }">
      <div class="myBtn" @click="$emit('reset')">
        
        {{ title.toUpperCase()   }}
      </div>
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
};
</script>

<style>
  .myBtn{
    border-bottom: solid 1px rgba(0,0,0,.3);
    color: var(--v-link-base);
    border-color: var(--v-link-base);
    font-size: 1rem;
    opacity: 1;
    position: relative;
    padding: 2px;
    min-width: 110px;
    margin: 0 16px 10px 0;
    text-align: center;
    text-decoration: none;
    font-weight: 600;

  }
  .myBtn:hover{
    cursor: pointer;
    border-bottom: solid 2px var(--v-link-base);
    -webkit-box-shadow: -5px 42px 30px -11px rgba(253, 251, 251, .6);
    -moz-box-shadow: -5px 42px 30px -11px rgba(253, 251, 251, .6);
    box-shadow: -5px 42px 30px -11px rgba(253, 251, 251, .6);
  }

  .v-input__control{
    max-width: 110px;
  }
  .v-select__slot:hover{
    cursor: pointer;
   -webkit-box-shadow: -5px 42px 30px -11px rgba(253, 251, 251, 1);
  -moz-box-shadow: -5px 42px 30px -11px rgba(253, 251, 251, 1);
  box-shadow: -5px 42px 30px -11px rgba(253, 251, 251, 1);
  }
</style>