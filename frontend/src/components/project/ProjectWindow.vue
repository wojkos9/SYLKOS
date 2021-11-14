<template>
     <v-dialog v-model="dialog" width="unset">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on">
                  {{ getString("userPanel", "details") }}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h5 grey lighten-2">
                  {{ project.name }}
                </v-card-title>

                <v-card-text>
                  <div>
                    <div class="projectDesc">
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
                </v-card-text>

                <v-divider></v-divider>

                <div
                  class="animation"
                  v-show="project.images[0].image != 'images/no_picture.png'"
                >
                  <div>
                    <Carousel
                      :slides="project.images"
                      :ifRoute="ifRoute"
                      :group="group"
                    />
                  </div>
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
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" text @click="dialog = false">
                    {{ getString("userPanel", "close") }}
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
</template>
<script>
import { getString } from "@/language/string.js";
import { apiService } from "@/common/api.service.js";
import Comment from "@/components/project/Comment.vue";
import AddComment from "@/components/project/AddComment.vue";
import Carousel from "@/components/UI/Carousel.vue";

export default {
  name: "ProjectWindow",
  props: ["project"],
  data() {
    return {
      dialog: false,
      showGallery: false,
      comments: [],
      myComment: {},
      username: window.localStorage.getItem("username"),
      headers: [
        {
          text: "Dessert (100g serving)",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "Calories", value: "calories" },
      ],
      desserts: [],
    };
  },
  methods: {
    getString,
    async getVotingData() {
      let tmp = this.project.voting ? this.project.voting : this.project.voting_id;
      let votingEdnpoint = `api/voting/${tmp}/`;
      let votingData = await apiService(votingEdnpoint);

      let commentsEndpoint = `api/projects/${this.project.id}/comments/`;
      let commentsData = await apiService(commentsEndpoint);
      this.myComment = this.project.user_comment;
      this.comments = commentsData.results;
      console.log(votingData)
      this.desserts = [
        {
          name: this.getString("projectInfo", "price"),
          calories: this.project.budget + "zł",
        },
        {
          name: this.getString("projectInfo", "votingEndDate"),
          calories: votingData.end_date.slice(
            0,
            votingData.end_date.indexOf(" ")
          ),
        },
        {
          name: this.getString("projectInfo", "projectUploadDate"),
          calories: this.project.finish_date.slice(
            0,
            this.project.finish_date.indexOf(" ")
          ),
        },
      ];
    },
    async updateComments() {
      let projectEndpoint = `api/projects/${this.project.id}/`;
      let projectData = await apiService(projectEndpoint);

      if (projectData.user_has_commented)
        this.myComment = projectData.user_comment;
      else this.myComment = {};

      this.project.user_has_commented = projectData.user_has_commented;
    },
  },
   created() {
    this.getVotingData();
  },
  components: { Carousel, AddComment, Comment },
};
</script>

<style scoped>
.projectDesc {
  font-size: 1.2rem;
  max-width: 500px;
  margin: 20px auto 50px auto;
  color: #000;
}
.comments {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.animation {
  max-height: 900px;
  padding-bottom: 40px;
  max-width: 600px;
  display: inherit !important;
  margin: 0 auto;
  -webkit-box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  -moz-box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  transition: all 2s ease;
  margin: 40px;
}
.animation[style*="display: none;"] {
  max-height: 0;
  opacity: 0;
  padding-bottom: 0px;
  pointer-events: none; /* disable user interaction */
  user-select: none; /* disable user selection */
}

</style>
