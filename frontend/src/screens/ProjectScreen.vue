<template>
  <div class="area">
    <div class="leftSection">
      <div class="projectTitle">
        {{ project.name }} ({{ project.rating_avg }})
      </div>

      <div class="groupName">grupa: {{ project.group }}</div>

      <div class="projectInfoAndGallery">
        <div class="projectInfo">
          <div class="projectDescription">
            {{ project.description }}
          </div>

          <v-data-table
            :headers="headers"
            :items="desserts"
            hide-default-header
            hide-default-footer
            class="elevation-1"
          ></v-data-table>
        </div>
        <div class="gallery">
          <div>
            <Carousel
              :slides="project.images"
              :ifRoute="ifRoute"
              :group="group"
              :title="title"
            />
          </div>
        </div>
      </div>

      <div class="commentSection">
        <div class="discussionTitle">
          {{ getString("projects", "discussion") }}
        </div>

        <div class="comments">
          <div v-if="!project.user_has_commented">
            <AddComment
              :projectId="project.id"
              v-on:addedComment="updateComments"
            />
          </div>

          <div v-else>
            <Comment
              v-bind:comment="myComment[0]"
              v-bind:author="username"
              v-on:deleteUpdate="updateComments"
            />
          </div>
          <div v-for="comment in comments" :key="comment.id">
            <div v-show="comment.author != username">
              <Comment v-bind:comment="comment" />
            </div>
          </div>
        </div>
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
              :slides="images"
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
import Comment from "../components/project/Comment.vue";
import AddComment from "../components/project/AddComment.vue";
import Carousel from "../components/UI/Carousel.vue";
import { apiService } from "@/common/api.service.js";

export default {
  name: "projectScreen",
  props: {
    id: {
      // type: Number,
      required: true,
      // headers:[],
     
    },
    project:{
      required: true
    }
  },
  data() {
    return {
      
      zm: false,
      comments: [],
      votingFinish: "",
      // group: true,
      myComment: {},
      slides: [],
       title: "tytul",
      ifRoute: true,
      group: true,
      showGallery: false,
      username: window.localStorage.getItem("username"),
      headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
        ],
        desserts: [
         
          ]
    };
  },
  components: {
    Comment,
    AddComment,
    Carousel,
  },
  methods: {
    getString,
    async updateComments() {

      let projectEndpoint = `api/projects/${this.project.id}/`;
      let projectData = await apiService(projectEndpoint);

      if (projectData.user_has_commented)
        this.myComment = projectData.user_comment;
      else this.myComment = {};

      this.project.user_has_commented = projectData.user_has_commented;
    },
  },

  async beforeRouteEnter(to, from, next) {
    let projectEndpoint = `api/projects/${to.params.id}/`;
    let commentsEndpoint = `api/projects/${to.params.id}/comments/`;

    let projectData = await apiService(projectEndpoint);
    let commentsData = await apiService(commentsEndpoint);

    let votingEdnpoint = `api/voting/${projectData.voting}/`;
    let votingData = await apiService(votingEdnpoint);

    return next((vm) => {
      // vm.project = projectData;
      vm.myComment = projectData.user_comment;
      vm.comments = commentsData.results;
      vm.votingFinish = votingData.end_date;

      vm.desserts = [ {
            name:  vm.getString("projectInfo", "price"),
            calories:  projectData.budget + "zł",
 
          },
           {
            name: vm.getString("projectInfo", "votingEndDate"),
            calories:  votingData.end_date.slice(0, votingData.end_date.indexOf(' ')),
          },
           {
            name:  vm.getString("projectInfo", "projectUploadDate"),
            calories: projectData.finish_date.slice(0, projectData.finish_date.indexOf(' ')),
 
          },
        ]

      if (vm.project.images.length == 0) {
        vm.project.images = [{ image: "images/no_picture.png" }];
      }
    });
  },
};
</script>

<style scoped>
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


.projectInfo{
  /* border:solid; */
  font-family: 'Petrona';
  width: 60%;
  
}

.projectTitle {
  padding-top: 50px;
  font-size: 40px;
  width: 100%;
  text-align: center;
}
.rightSectionVOting {
  width: 30%;
  /* margin-left: 20%; */
  padding: 20px;
  font-size: 20px;
  /* border:solid; */
  margin: auto;
}
.text-bold {
  font-weight: 600;
}
.groupName {
  font-size: 30px;
  max-width: 100%;
  margin: 0 auto 30px auto;
  padding: 0;
  /* text-align: center; */
}
.projectDescription {
  font-size: 20px;
  padding-bottom: 30px;
}
.projectInfoAndGallery {
  padding: 0 100px;
  display: flex;
  /* justify-content: space-between; */
  /* max-width: 50%; */
  flex-wrap: nowrap;
  /* text-align: left; */
  font-size: 20px;
}
.gallery {
  width: 30%;
  max-height: 900px;
    padding-bottom: 40px;
    display: inherit !important; 
    margin: 0 auto;

  /* margin-left: 10%; */
  /* margin: auto; */
  /* display: flex; */
  /* justify-content: center; */
/* padding: 20px; */
  border:solid;
}
.comments {
  display: flex;
  /* flex-direction: row; */
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 50px;
}

.discussionTitle {
  margin: 0 auto;
  text-align: center;
  font-size: 28px;
  text-transform: uppercase;
  /* width: 100%; */
  /* border:solid; */
}
@media only screen and (max-width: 1100px) {
  .projectOptions {
    margin-top: 15px;
    justify-content: center;
  }
}

@media only screen and (max-width: 800px) {
  .projectInfoAndGallery{
    flex-wrap: wrap;
  }
  .gallery{
    width: 100%;
    padding: 0 10%;
  }
}
</style>
