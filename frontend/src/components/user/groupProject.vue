<template>
    <div class="area">
      <img class="image" v-bind:src="image"/>
      <div  class="title"><div class="text">{{title}}</div></div>
      <div class="desc">{{desc}}</div>
    </div>
</template>

<script>
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'

export default {
  name: "groupProject",
  props: ['title', 'desc', 'image'],
  data() {
    return {

    }
  }, 
  methods: {
    getString,
    getColor,
  },
}
</script>

<style scoped>
  .area{
    height: 300px;
    width: 160px;
    padding: 10px;
  }
  .image{
    width: 160px;
    height: 160px ;
    object-fit: cover;
  }
  .title{
    font-family: 'Playfair Display';
    font-size: 16px;
    font-weight: 400;
    margin-top: 10px;
  }
  .desc{
    margin-top:10px;
    font-size: 12px;
    font-weight: 400;
  }
  .text{
    text-align: center;
  }
</style>