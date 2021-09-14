<template>
  <div>
      <div  v-show="!ifRoute" class="groupName">
      <span v-if="group">{{ getString("gallery", "group") }}</span>
      <span v-else-if="!group">{{ getString("gallery", "project") }}</span>
      <div class="galleryTitle">{{title}}</div>
      </div>
    
    <vue-slick-carousel :arrows="true" :dots="true" :fade="true" ref="carousel">
      
      <div v-for="(item, index) in slides" v-bind:key="index">
        
        <div class="image" v-if="ifRoute">
          <router-link :to="{ name: 'photo', params: { slides: slides, title: title, group:group } }">
            <img :src="`/media/${item.image}`" />
          </router-link>
        </div>
        <div class="image" v-else><img :src="`/media/${item.image}`" /></div>
        <div class="desc">{{ item.desc }}</div>
      </div>
    </vue-slick-carousel>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  name: "Carousel",
  props: ["slides", "ifRoute", "group", "title"],
  data() {
    return {
      focusOnSelect: true,
    };
  },
  methods: {
    getString,
    showNext() {
      this.$refs.carousel.goTo(this.initIndex);
    },
  },
  components: {
    VueSlickCarousel,
  },
  mounted() {
    for(var i of this.slides){
      console.log("element", i.image)
    }
  },
};
</script>

<style scoped>
.slick-prev:before {
  color: black !important;
  background-color: rgba(255, 255, 255, 0);
}
.slick-next:before {
  color: black !important;
  background-color: rgba(255, 255, 255, 0);
}
.desc {
  text-align: center;
  margin-top: 25px;
  margin-bottom: 25px;
}
.image {
  justify-self: center;
  display: flex;
  justify-content: center;
  margin-top: 40px;
}
.groupName{
  font-family: "playfair display";
  font-size: 2rem;
  text-align: center;
}
.galleryTitle{
  font-weight: 600;
  margin-top: 40px;
}
</style>
