<template>
  <div class="content">

    <VueSlickCarousel :arrows="true" :dots="true" :fade="true" ref="carousel" :centerMode="true">
      <div v-for="(item, index) in slides" v-bind:key="index">
        <div class="image" v-if="ifRoute">
          <div>
          <img :src="`/media/${item.image}`" @click="photoDialog=true"/>
          </div>
        </div>
        <div class="image" v-else><img :src="`/media/${item.image}`" /></div>
        <div class="desc">{{ item.desc }}</div>
      </div>
    </VueSlickCarousel>

  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  name: "Carousel",
  props: ["slides", "ifRoute", "group", "title"],
  data() {
    return {
      focusOnSelect: true,
      photoDialog: false,
      settings:{
      dots: true,
      dotsClass: "slick-dots custom-dot-class",
      "edgeFriction": 0.35,
      "infinite": false,
      "speed": 500,
      "slidesToShow": 1,
      "slidesToScroll": 1,
      // "centerMode": true,
      }
    };
  },
  methods: {
    showNext() {
      this.$refs.carousel.goTo(this.initIndex);
    },
  },
  components: {
    VueSlickCarousel,
  },
  mounted() {
    for (var i of this.slides) {
      console.log("element", i.image);
    }
  },
};
</script>

<style >

.desc {
  text-align: center;
  margin-top: 25px;
}
.slick-dots li button:before{
  color: white
}

.slick-dots li.slick-active button:before{
  color: white
}
.content{
  margin: auto;
  padding: 50px;

}
.image{
  height: calc(50vh - 50px);
  width: auto;
  max-height: 200px;
  object-fit: contain;
  margin: 0 auto;
  /* max-width: 90%; */
  display: flex;
  justify-content: center;
}

.slick-prev{
  left: -40px !important
}
.slick-next{
  right: -10px !important
}
.image img{
  width: auto;
  margin: 0 auto; 
}
.v-card__text{
  margin-top: 30px;
  display: flex;
  justify-content: center;
}
.dialogGallery{

  display: flex; 
  justify-content: center;
  /* max-width: 70%; */
  justify-self: center;
}

v-dialog{
  width: 100%;
}
.slick-prev:before{
  /* color: #000 !important; */
  font-size: 40px;
  background-color: none;
  opacity: 1;
  z-index: 9999;

}

.slick-next:before{
  /* color: #000 !important; */
  font-size: 40px;
  background-color: none;
  opacity: 1;
  z-index: 9999;

}

.slick-prev:before:hover{
  /* color: #000 !important; */
  font-size: 40px;
}

.slick-next:before:hover{
  /* color: #000 !important; */
  font-size: 40px;
}

  .slick-slider {
    position: relative;
}

.v-application ul{
  padding-left: 0 !important
}
@media only screen and (max-width: 500px){
  .image{
  height: calc(50vh - 50px);
  width: auto;
  max-height: 150px;
  object-fit: contain;
  margin: 0 auto;
  /* max-width: 90%; */
  display: flex;
  justify-content: center;
}
.content{
  padding: 20px;
} 
.slick-prev:before{
  color: #000 !important;
  font-size: 20px;
}

.slick-next:before{
  color: #000 !important;
  font-size: 20px;
}

.slick-prev{
  left: -10px !important
}
.slick-next{
  right: -10px !important
}
}

@media only screen and (max-width: 400px){
  .image{
  height: calc(50vh - 50px);
  width: auto;
  max-height: 100px;
  object-fit: contain;
}

}

</style>
