<template>
  <div class="votingProjectarea">


    <div class="leftSectionVotingProject">
      <div class="title">
        {{ project.name }}
      </div>
      
      <div class="description">
        {{ getString("votingProject", "desc") }} {{ project.description }}
      </div>

      <div class="price">
        {{ getString("votingProject", "price") }} : {{ project.budget }} zł
      </div>
    </div>

    <div class="rightSectionVOting">

      <div v-if="project.images.length > 0">
            <img :src="`/media/${project.images[0].image}`" class="image" />
          </div>
        <div class="commentSectionRedirectButton">
        <ProjectWindow :project="project"/>
      </div>
    </div>
    <div class="votingSection">
        <div class="bigCircle">
          <div class="smallCircle"></div>
          <div class="tooltiptext">Głosuję na ten projekt</div>
        </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import ProjectWindow from "@/components/project/ProjectWindow.vue";
export default {
  name: "votingProject",
  props: ["project", "clicked"],
  data() {
    return {
      title: "tytul",
      ifRoute: true,
      group: true,
      showGallery: false,
    };
  },
  components: {
    ProjectWindow
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
    padding-bottom: 40px;
    display: inherit !important; 
    margin: 0 auto;
    /* transition: opacity 1s ease; */
    transition: all 2s ease;
}
.animation[style*="display: none;"] {
    max-height: 0;
    opacity: 0;
    padding-bottom: 0px;
    pointer-events: none; /* disable user interaction */
    user-select: none; /* disable user selection */
}

.leftSectionVotingProject {
  width: 60%;
  padding: 10px 10px 10px 40px;
}
.rightSectionVOting {
  width: 30%;
  padding: 20px;
  font-size: 20px;
  margin: auto;
}
.votingSection{
  width: 10%;
  display: flex;
  align-items: center;
  margin: 0 auto;
  justify-content: center;
}

.votingProjectarea {
  border-radius: 25px;
  display: flex;
  margin: 40px auto 0 auto;
  max-width: 800px;
  -webkit-box-shadow: 0px 0px 35px -14px rgba(46, 46, 57, 1);
-moz-box-shadow: 0px 0px 35px -14px rgba(46, 46, 57, 1);
box-shadow: 0px 0px 35px -14px rgba(46, 46, 57, 1);
} 

.title {
  font-size: 20px;
  font-weight: 600;
  margin-top: 10px;
}
.bigCircle {
  width: 30px;
  height: 30px;
  border-radius: 15px;
  position: relative;
  background-color: rgb(64, 59, 82);
  margin-right: 10px;
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

/* .bigCircle .tooltip{
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  position: absolute;
  z-index: 1;
} */


.tooltiptext {
  /* display: flex; 
  flex-direction: column; 
  justify-content: flex-start; 
  background-color: #0366d6;
  padding: 18px; 
  border-radius: 5px; 
  color: white; 
  line-height: 15px;
  transition: 1s;
  width: 200px; */
  position: absolute; 
  opacity: 0; 
  z-index: 1;
  /* left: 50%; */
  top: -60px;
  left: 30px;
  width: 200px;
  padding: 20px;
  border-radius: 143px 150px 150px 0px;
  background-color: rgb(230, 230, 230);
  /* border:solid; */
  /* transform: translateX(-50%); */
-webkit-box-shadow: 8px 8px 20px 3px rgb(92, 76, 76);
-moz-box-shadow: 8px 8px 20px 3px  rgb(92, 76, 76);
box-shadow: 8px 8px 20px 3px  rgb(92, 76, 76);
}

.bigCircle:hover{
  cursor: pointer;
}
.bigCircle:hover .tooltiptext {
  opacity: 1; 
  transition: 0.5s;
  transition-delay: 0.1s;
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

.commentSectionRedirectButton {
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
  .votingProjectarea {
    /* flex-wrap: wrap; */
    flex-direction: column;
  }
  .rightSectionVOting {
    width: 80%;
    margin: 0 auto;
  }
  .leftSectionVotingProject {
    width: 80%;
    margin: 0 auto;
    border:solid;
    padding: 10px;
    padding: 10px 10px 10px 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
