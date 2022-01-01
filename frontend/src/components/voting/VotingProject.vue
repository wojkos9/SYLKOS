<template>
  <div class="votingProjectarea">


    <div class="leftSectionVotingProject">
      <div class="title">
        {{ project.name }}
      </div>
      <div class="price">
        {{ $t("price") }} : {{ project.budget }} zł
      </div>
    </div>

    <div class="rightSectionVOting">
      <div class="commentSectionRedirectButton">
      </div>

      <div class="commentSectionRedirectButton">
        <ProjectWindow :project="project" />
      </div>
    </div>
  </div>
</template>

<script>
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

.votingProjectarea {
  border-radius: 25px;
  display: flex;
  margin: 40px auto 0 auto;
  max-width: 800px;
  -webkit-box-shadow: 0px 0px 35px -14px #00bfa5 ;
-moz-box-shadow: 0px 0px 35px -14px #00bfa5 ;
box-shadow: 0px 0px 35px -14px #00bfa5 ;
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
    max-width: 90%;
  }
  .rightSectionVOting {
    width: 80%;
    margin: 0 auto;
    display: flex;
    justify-content: center;

  }
  .leftSectionVotingProject {
    width: 80%;
    /* margin: 0 auto; */
    /* border:solid; */
    padding: 10px;
    padding: 10px 10px 10px 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
}
</style>
