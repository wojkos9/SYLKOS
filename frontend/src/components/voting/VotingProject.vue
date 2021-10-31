<template>
  <div class="area">
    <div class="leftSection">
      <div class="title">
        {{ project.name }}
      </div>
      <div class="description">
        {{ project.description }}
      </div>
      <div class="price">
        {{ getString("votingProject", "price") }} : {{ project.budget }} zł
      </div>
    </div>

    <div class="rightSectionVOting">
      <div class="commentSectionRedirectButton">
        <div v-if="showGallery">
          <v-btn
            color="primary lighten-1"
            class="p-3"
            dark
            style="color:black; margin-bottom: 20px"
            @click="showGallery = false"
          >
            {{ getString("votingProject", "hideGallery").toUpperCase() }}
          </v-btn>
        </div>
        <div v-else>
          <v-btn
            color="primary lighten-1"
            class="p-3"
            dark
            style="color:black; margin-bottom: 20px"
            @click="showGallery = true"
          >
            {{ getString("votingProject", "showGallery").toUpperCase() }}
          </v-btn>
        </div>
      </div>

      <!-- <transition name="component-fade" mode="out-in"> -->
        <div v-show="showGallery" class="animation">
          <div>
            <Carousel
              :slides="project.images"
              :ifRoute="ifRoute"
              :group="group"
              :title="title"
            />
          </div>
        </div>
        <!-- <div v-else></div> -->
      <!-- </transition> -->

      <div class="commentSectionRedirectButton">
        <router-link :to="{ name: 'project', params: { id: 1 } }">
          <v-btn
            color="primary lighten-2"
            class="p-3 myButtotn"
            dark
            style="color:black"
            @click="showGallery = true"
          >
            {{ getString("votingProject", "seeDiscussion") }}
          </v-btn>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import Carousel from "../../components/UI/Carousel.vue";
export default {
  name: "votingProject",
  props: ["project", "clicked"],
  data() {
    return {
      // clicked: false
      title: "tytul",
      ifRoute: true,
      group: true,
      showGallery: false,
    };
  },
  components: {
    Carousel,
  },
  methods: {
    getString,
    buttonClicked() {
      this.clicked = !this.clicked;
      this.$emit("change", this.$props.id);
    },
  },
};
</script>

<style
  link
  rel="stylesheet"
  href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
  scoped
>
.animation{
    max-height: 900px;
    display: inherit !important; 
    /* transition: opacity 1s ease; */
    transition: all 2s ease;
}
.animation[style*="display: none;"] {
    max-height: 0;
    opacity: 0;
    pointer-events: none; /* disable user interaction */
    user-select: none; /* disable user selection */
}

.leftSection {
  width: 40%;
}
.rightSectionVOting {
  width: 50%;
  margin-left: 10%;
  padding: 20px;
  font-size: 20px;
  margin-left: 100px;
  max-width: 800px;
}
.area {
  border: solid 1px black;
  border-radius: 25px;
  display: flex;
  margin: 40px;
  padding: 20px;
}
.title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 20px;
  margin-top: 20px;
}
.bigCircle {
  width: 30px;
  height: 30px;
  border-radius: 15px;
  position: relative;
  background-color: rgb(64, 59, 82);
  margin-right: 10px;
}
.bigCircle:hover {
  cursor: pointer;
}
.smallCircle {
  width: 16px;
  height: 16px;
  border-radius: 8px;
  background-color: rgb(217, 208, 250);
  position: absolute;
  left: 50%;
  margin-left: -8px;
  top: 50%;
  margin-top: -8px;
}
.activeCircle {
  background-color: rgb(22, 187, 50);
}
.description {
  margin-bottom: 20px;
}
.likes {
  display: flex;
  font-size: 25px;
  justify-content: flex-end;
  margin-bottom: 10px;
}
.gallery {
  display: flex;
  margin-bottom: 10px;
  /* margin-left: 50px; */
}
.leftArrow,
.rightArrow {
  align-items: center;
  display: flex;
  justify-content: center;
}
.v-btn {
  width: 200px;
  border-radius: 50px;
}
.galleryImage {
  width: 300px;
}
.commentSectionRedirectButton,
.voteForProject {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
  padding: 0;
  /* margin-right: 10px; */
}
.button {
  font-weight: 500;
  padding: 5px 10px;
}
.red {
  /* background-color: red; */
  font-weight: 500;
  padding: 5px 10px;
}
.green {
  background-color: rgb(217, 208, 250);
  font-weight: 500;
  padding: 5px 10px;
}
.voteForThisProject {
  background-color: rgb(217, 208, 250);
  font-weight: 500;
  padding: 5px 10px;
}
/* @media only screen and (max-width: 1300px) {
        .galleryImage{
        width: 500px;
        }
        .area{
            flex-direction: column;
        }
    } */
@media only screen and (max-width: 800px) {
  .area {
    /* flex-wrap: wrap; */
    flex-direction: column;
  }
  .rightSectionVOting {
    width: 80%;
    margin: 0 auto;
  }
  .leftSection {
    width: 80%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
