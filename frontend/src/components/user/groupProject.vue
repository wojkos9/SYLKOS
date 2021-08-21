<template>
    <div class="content">
      <img class="image" v-bind:src="image"/>
      <div  class="titleIn"><div class="text">{{title}}</div></div>
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
  .content{
    /* height: 200px; */
    width: 160px;
    /* padding: 10px; */
    margin:20px;
  }
  .image{
    width: 160px;
    height: 160px ;
    object-fit: cover;
  }
  .titleIn{
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

  

  @media only screen and (max-width: 1300px) {
    .content{
      width: 140px;
    }
  .image{
    width: 140px;
    height: 140px ;
  }
  }

</style>