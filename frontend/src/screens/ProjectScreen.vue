<template>
  <div class="area">
    <div class="projectDetails">
      <div class="projectTitle">
        {{ project.name }} ({{ project.rating_avg }})
      </div>

      <div class="groupName">grupa: {{ project.group }}</div>

      <div class="projectDescription">
        {{ project.description }}
      </div>
      <div class="projectInfoAndGallery">
        <div class="projectInfo">
          <div class="singleInfo">
            <span class="text-bold"
              >{{ getString("projectInfo", "price") }}:</span
            >
            {{ project.budget }} zł
          </div>
          <div class="singleInfo">
            <span class="text-bold"
              >{{ getString("projectInfo", "votingEndDate") }}:</span
            >
            {{ votingFinish.slice(0, votingFinish.indexOf("T")) }}
          </div>
          <div class="singleInfo">
            <span class="text-bold"
              >{{ getString("projectInfo", "projectUploadDate") }}:</span
            >
            {{ project.finish_date.slice(0, project.finish_date.indexOf("T")) }}
          </div>
        </div>
        <div class="gallery">
          <Carousel
            :slides="slides"
            :ifRoute="ifRoute"
            :group="group"
            :title="groupName"
          />
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
              />
          </div>
          <div v-for="comment in comments" :key="comment.id">
            <div v-show="comment.author != username">
              <Comment
                v-bind:comment="comment"
              />
            </div>
          </div>
        </div>
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
  name: "projectOptions",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      project: {},
      comments: [],
      votingFinish: "",
      group: false,
      myComment: {},
      slides: [],
      ifRoute: true,
      username: window.localStorage.getItem("username")
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
      this.project.user_has_commented = projectData.user_has_commented;

      let commentsEndpoint = `api/projects/${this.project.id}/comments/`;
      let commentsData = await apiService(commentsEndpoint);
      this.comments = commentsData.results;
    },
    sortByName() {
      console.log("sortByName");
    },
    sortByMembers() {
      console.log("sortByMembers");
    },
    sortByNameDesc() {
      console.log("sortByNameDesc");
    },
    sortByMembersDesc() {
      console.log("sortByMembersDesc");
    },
  },
  async beforeRouteEnter(to, from, next) {
    console.log(to.params.id);
    let projectEndpoint = `api/projects/${to.params.id}/`;
    let commentsEndpoint = `api/projects/${to.params.id}/comments/`;

    let projectData = await apiService(projectEndpoint);
    let commentsData = await apiService(commentsEndpoint);

    let votingEdnpoint = `api/voting/${projectData.voting}/`;
    let votingData = await apiService(votingEdnpoint);

    return next((vm) => {
      vm.project = projectData;
      vm.myComment = projectData.user_comment;
      vm.comments = commentsData.results;
      vm.votingFinish = votingData.end_date;
    });
  },
};
</script>

<style scoped>
.row {
  margin-bottom: 50px;
  margin-top: 50px;
}

.projectTitle {
  padding-top: 50px;
  font-size: 40px;
  width: 100%;
  text-align: center;
}
.text-bold {
  font-weight: 600;
}
.groupName {
  font-size: 30px;
  width: 100%;
  text-align: center;
}
.projectDescription {
  font-size: 20px;
  padding: 50px 100px;
  max-width: 50%;
}
.projectInfoAndGallery {
  padding-left: 100px;
  max-width: 50%;
  text-align: left;
  font-size: 20px;
}
.gallery {
  width: 800px;
}
.comments {
  display: flex;
  flex-direction: row;
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
</style>
