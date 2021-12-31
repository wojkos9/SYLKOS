<template>
  <div class="starsRow">
    <div v-for="i in 5" :key="i"><star v-bind:stars="stars" v-bind:number="i" /></div>
  </div>
</template>

<script>
import Star from './Star.vue';

export default {
  name: "stars",
  props: ["stars"],
  methods: {
  },
  computed: {},
  components: {Star},
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
