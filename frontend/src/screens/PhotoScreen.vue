<template>
  <div class="allArea">
     <div  @click="$router.go(-1)"><md-icon class="goBack" @click="$router.go(-1)">clear</md-icon></div>
    <div class="photoPage">
      <Carousel :slides="slides" :ifRoute="ifRoute"  :group="group" :title="title"/>
    </div>
   
  </div>
</template>

<script>
import Carousel from "../components/UI/Carousel.vue";
export default {
  name: "photoScreen",
  props: ["slides", "title", "group"],
  components: {
    Carousel,
  },
  data() {
    return {
      ifRoute: false,
      pictures: [],
    };
  },
  methods: {
   
  },
  mounted() {
    for(var i of this.slides){
      console.log("element", i)
    }
    // console.log("cc", this.slides)
  },
};
</script>

<style>
.allArea{
margin-top: -100px;
width: 100%;
background-color: #f2f6fa;
/* position: absolute; */
height: 100%;
}
.photoPage {
  margin: auto;
  width: 60%;
  padding: 10px;
  padding-top: 50px;
}
.goBack{
  width: 50px;
  height: 50px;
  border: solid;
  border-radius: 25px;
  position: absolute;
  margin-left: 90%;
  margin-top: 5%;
}
.goBack:hover{
  cursor: pointer;
  background-color: #C0CFE6;
}
</style>
