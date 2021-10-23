<template>
  <div>
    <div v-show="!ifRoute" class="groupName">
      <span v-if="group">{{ getString("gallery", "group") }}</span>
      <span v-else-if="!group">{{ getString("gallery", "project") }}</span>
      <div class="galleryTitle">{{ title }}</div>
    </div>

    <vue-slick-carousel :arrows="true" :dots="true" :fade="true" ref="carousel">
      <div v-for="(item, index) in slides" v-bind:key="index">
        <div class="image" v-if="ifRoute">
          <!-- <router-link :to="{ name: 'photo', params: { slides: slides, title: title, group:group } }"> -->
          <img :src="`/media/${item.image}`" @click="photoDialog=true"/>
          <!-- </router-link> -->
        </div>
        <div class="image" v-else><img :src="`/media/${item.image}`" /></div>
        <div class="desc">{{ item.desc }}</div>
      </div>
    </vue-slick-carousel>

    <v-dialog
      v-model="photoDialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
      scrollable
    >
      <v-card tile>
        <v-toolbar flat dark color="primary">
          <v-btn icon dark @click="photoDialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title><span v-if="group">{{ getString("gallery", "group") }}</span>
      <span v-else-if="!group">{{ getString("gallery", "project") }}</span> <span class="galleryTitle">{{ title }}</span></v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text >
          <VueSlickCarousel 
            v-bind="settings"
          >
            <div v-for="(item, index) in slides" v-bind:key="index">
              <div class="image" v-if="ifRoute">
                <img :src="`/media/${item.image}`" />
              </div>
              <div class="image2" v-else>
                <img :src="`/media/${item.image}`" />
              </div>
              <div class="desc">{{ item.desc }}</div>
            </div>
          </VueSlickCarousel>
        </v-card-text>
      </v-card>
    </v-dialog>
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
      photoDialog: false,
      settings:{
      "dots": true,
      "dotsClass": "slick-dots custom-dot-class",
      "edgeFriction": 0.35,
      "infinite": false,
      "speed": 500,
      "slidesToShow": 1,
      "slidesToScroll": 1
      }
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
    for (var i of this.slides) {
      console.log("element", i.image);
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
.groupName {
  font-size: 2rem;
  text-align: center;
}
.galleryTitle {
  font-weight: 600;
  margin-top: 40px;
}

img{
  max-width: 90%;
}

v-dialog{
  width: 100%;
}
.slick-prev:before {
  color: red !important;
  background-color: #eee;
}
.slick-next:before {
  color: red !important;
  background-color: #eee;
}
</style>
