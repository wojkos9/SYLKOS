<template>
  <div class="content">
    <!-- <div v-show="!ifRoute" class="groupName">
      <span v-if="group">{{ getString("gallery", "group") }}</span>
      <span v-else-if="!group">{{ getString("gallery", "project") }}</span>
      <div class="galleryTitle">{{ title }}</div>
    </div> -->

    <!-- <div class="carousel-wrapper"> -->

    <VueSlickCarousel :arrows="true" :dots="true" :fade="true" ref="carousel" :centerMode="true">
      <div v-for="(item, index) in slides" v-bind:key="index">
        <div class="image" v-if="ifRoute">
          <div>
          <!-- <router-link :to="{ name: 'photo', params: { slides: slides, title: title, group:group } }"> -->
          <img :src="`/media/${item.image}`" @click="photoDialog=true"/>
          </div>
          <!-- </router-link> -->
        </div>
        <div class="image" v-else><img :src="`/media/${item.image}`" /></div>
        <div class="desc">{{ item.desc }}</div>
      </div>
    </VueSlickCarousel>

    <!-- </div> -->

    <!-- <v-dialog
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
          class="dialogGallery"
           :arrows="true" :dots="true" :fade="true" ref="carousel" :centerMode="true">
            <div v-for="(item, index) in slides" v-bind:key="index">
              <div class="image2" v-if="ifRoute">
                <img :src="`/media/${item.image}`" />
              </div>

              <div class="desc">{{ item.desc }}</div>
            </div>
          </VueSlickCarousel>
        </v-card-text>
      </v-card>
    </v-dialog> -->
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

.content{
  margin: auto;
  padding: 20px;

}
.image{

  max-width: 90%;
  display: flex;
  justify-content: center;
}
.carousel-wrapper {
  padding: 40px;
}
.image img{
  width: auto;
  margin: 0 0; 
}
.v-card__text{
  margin-top: 30px;
  display: flex;
  justify-content: center;
}
.dialogGallery{

  display: flex; 
  justify-content: center;
  max-width: 70%;
  justify-self: center;
}

.image2{
  max-width: 100%;
  display: flex;
  justify-content: center;
}
.image2 img{
  height: calc(80vh - 100px);
  width: auto;
  margin: 0 auto; 

}

.groupName {
  font-size: 2rem;
  text-align: center;
}
.galleryTitle {
  font-weight: 600;
  margin-top: 40px;
}


v-dialog{
  width: 100%;
}
.slick-prev:before{
  color: #000 !important;
  font-size: 40px;
  background-color: none;
  opacity: 1;
  z-index: 9999;

}

.slick-next:before{
  color: #000 !important;
  font-size: 40px;
  background-color: none;
  opacity: 1;
  z-index: 9999;

}

.slick-prev:before:hover{
  color: #000 !important;
  font-size: 40px;
}

.slick-next:before:hover{
  color: #000 !important;
  font-size: 40px;
}

.slick-prev {
    margin-left: 40px;
  }

  .slick-next {
    margin-right: 40px;
  }

  .slick-slider {
    position: relative;
}


</style>
