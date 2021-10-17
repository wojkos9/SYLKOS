<template>
  <div class="text-center mt-12">
    <v-rating
      v-model="rating"
      @input="ratingChange($event)"
      color="yellow darken-3"
      background-color="grey darken-1"
      empty-icon="$ratingFull"
      half-icon="mdi-star-half"
      half-increments
      hover
      large
    ></v-rating>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "stars",
  props: ["rating"],
  data(){
    return{
      ratingValue: 0
    }
  },
  methods: {
    getString,
    getColor,
    ratingChange(newValue){
      this.ratingValue = newValue;
      this.$emit('ratingChanged', this.ratingValue);
    }
  },
  computed: {},
};
</script>

<style scoped>
.starsRow {
  margin-top: 7px;
  margin-bottom: 7px;
  width: 200px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>
