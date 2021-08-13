<template>
  <div class="area">
    <div v-if="stars >= number"><md-icon class="star">star</md-icon></div>
    <div v-else>
      <div v-if="stars == number-0.5"><md-icon class="star">star_half</md-icon></div>
      <div v-else><md-icon class="star">star_border</md-icon></div>
    </div>
  </div>
  
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "star",
  props: ["stars", "number"],
  methods: {
    getString,
    getColor,
  },
  computed: {},
  components: {},
};
</script>

<style scoped>
.area {
  margin-top: 7px;
  margin-bottom: 7px;
}
.nextTo {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
}
.star{
  color:gold !important
}
</style>
