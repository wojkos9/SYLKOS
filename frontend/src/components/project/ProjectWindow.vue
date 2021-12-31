<template>
  <v-dialog v-model="dialog" width="unset">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on">
        {{ $t("details") }}
      </v-btn>
    </template>

    <v-card>
        <v-card-title >
          {{ project.name }}
        </v-card-title>
      <v-card-text>
        <div>
          <div class="projectDesc">
             <div v-if="project.description.length > 200">
                        <span v-if="showMore2">{{ project.description }} </span>
                        <span v-else>
                          {{ project.description.slice(0, 200) }}...</span
                        > 
                        <div v-if="!showMore2" class="paddingTop-m">
                          <v-btn
                            x-small
                            color="primary"
                            dark
                            @click="showMore2 = true"
                          >
                            {{ $t("expand")}}
                          </v-btn>
                        </div>
                        <div v-else class="paddingTop-m">
                          <v-btn
                            x-small
                            color="primary"
                            dark
                            v-if="showMore2"
                            @click="showMore2 = false"
                          >
                            {{ $t("unexpand")}}
                          </v-btn>
                        </div>
                      </div>
                      <div v-else>
                        {{ project.description }}
                      </div>
          </div>
          <v-data-table
            :headers="headers"
            :items="desserts"
            hide-default-header
            hide-default-footer
            class="custom_table"
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
        <div v-show="showAddComment">
        <div v-if="!project.user_has_commented ">
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
         {{$t("close")}}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
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
      group: false,
      showMore2: false,
      ifRoute: false,
      showAddComment: true, 
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
    check(funName) {
      if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("unauthorized")
      ) {
      funName();
      } 
        
    },
    cannotComment(){
      this.showAddComment = false;
    },
    async getVotingData() {
      let tmp = this.project.voting
        ? this.project.voting
        : this.project.voting_id;
      let votingEdnpoint = `api/voting/${tmp}/`;
      let votingData = await apiService(votingEdnpoint);

      let commentsEndpoint = `api/projects/${this.project.id}/comments/`;
      let commentsData = await apiService(commentsEndpoint);
      this.myComment = this.project.user_comment;
      this.comments = commentsData.results;
      this.desserts = [
        {
          name: this.$t("price"),
          calories: this.project.budget + "zł",
        },
        {
          name: this.$t("votingEndDate"),
          calories: votingData.end_date.slice(
            0,
            votingData.end_date.indexOf(" ")
          ),
        },
        {
          name: this.$t("projectUploadDate"),
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
    this.check(this.cannotComment)
  },
  components: { Carousel, AddComment, Comment },
};
</script>

<style scoped>

.projectDesc {
  font-size: 1.2rem;
  max-width: 500px;
  margin: 20px auto 50px auto;
  text-align: center;
  line-height: 1.2;
  /* color: #000; */
}
.comments {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.custom_table{
  line-height: 1.3;
  font-size: 2rem;
  padding: .5em;
}


.animation {
  max-height: 900px;
  padding-bottom: 40px;
  max-width: 600px;
  display: inherit !important;
  margin: 40px 24px;
  -webkit-box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  -moz-box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  transition: all 2s ease;
  /* padding: 24px; */
  background-color: var(--v-primary-lighten3);
  border-radius: 8px;
}

.animation[style*="display: none;"] {
  max-height: 0;
  opacity: 0;
  padding-bottom: 0px;
  pointer-events: none; /* disable user interaction */
  user-select: none; /* disable user selection */
}
</style>
