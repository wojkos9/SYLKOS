<template>
  <div
    class="votingProjectarea"
    v-bind:class="[
      {
        votingProjectClicked: (clicked && ifUserCanVote) || myChoice,
      },
    ]"
    @click="chooseThisProject()"
  >
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
          <ProjectWindow :project="project" />
        </div>
      </div>
    </div>
</template>

<script>
import { getString } from "@/language/string.js";
import ProjectWindow from "@/components/project/ProjectWindow.vue";
export default {
  name: "votingProject",
  props: ["project", "clicked", "ifUserCanVote", "myChoice"],
  data() {
    return {
      title: "tytul",
      ifRoute: true,
      group: true,
      showGallery: false,
    };
  },
  components: {
    ProjectWindow,
  },
  methods: {
    getString,
    buttonClicked() {
      this.clicked = !this.clicked;
      this.$emit("change", this.project.id);
    },
    chooseThisProject() {
      if (this.ifUserCanVote) {
        this.$emit("change");
      }
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
.animation {
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
.votingSection {
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
  -webkit-box-shadow: 0px 0px 35px -14px rgb(113, 113, 151);
  -moz-box-shadow: 0px 0px 35px -14px rgb(113, 113, 151);
  box-shadow: 10px 10px 35px -14px rgb(113, 113, 151);
}

.votingProjectarea:hover {
  cursor: pointer;
}

.votingProjectClicked {
  background-color: var(--v-primary-lighten2);
  width: 100%;
  border-radius: 32px;
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

.description {
  margin-bottom: 20px;
  font-size: 16px;
}

.commentSectionRedirectButton {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
  padding: 0;
}

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
    border: solid;
    padding: 10px;
    padding: 10px 10px 10px 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
