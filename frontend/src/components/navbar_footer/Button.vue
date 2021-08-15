<template>
 
    

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
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
export default {
  name: "Button",
  props: ["title", "fun"],
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
        // height:"50%",
        alignSelf: "center",
        borderRadius: "35px",
        marginLeft: "1%",
        padding: "1%",
        // paddingLeft: "1%",
        // paddingRight: "1%",
        width: "15%",
        //  width: "10rem",
        textAlign: "center",
        // fontSize: "4px"
      };
    },
    buttonHovered(){
      return{
         backgroundColor: "#93abc4",
        // height:"50%",
        alignSelf: "center",
        borderRadius: "35px",
        marginLeft: "1%",
        padding: "1%",
        // paddingLeft: "1%",
        // paddingRight: "1%",
        width: "15%",
        //  width: "10rem",
        textAlign: "center",
        // fontSize: "4px"
      }
    }
  },
};
</script>

<style>
.active {
  cursor: pointer;
  /* background-color: #93abc4 !important; */
}
</style>
