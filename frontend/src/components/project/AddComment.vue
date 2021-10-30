<template>
  <div class="commentContainer">
    <v-form v-model="valid" ref="newComment">
    <div class="topSection">
      
      <div class="leftTopSection">
        <div class="userName">
          {{ user }}
        </div>

        <div class="rating">
          <v-rating
            v-model="rating"
            color="yellow darken-3"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            half-icon="mdi-star-half"
            half-increments
            hover
            large
          ></v-rating>
        </div>
      </div>
      <div class="rightTopSection">
        {{ moment(new Date()).format("DD.MM.YYYY") }}
      </div>
    </div>
    <div class="bottomSection">
      <v-textarea
        background-color="grey lighten-2"
        color="primary"
        :label="comment.label"
        :rules="comment.rule"
        v-model="comment.value"
      >
      </v-textarea>
     
      <div class="submitCommentIcon" @click="submit">
        <v-mdi class="postComment" name="mdiSend"></v-mdi>
      </div>
       
    </div></v-form>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { apiService } from "@/common/api.service.js";

export default {
  name: "addComment",
  props: ["projectId"],
  data() {
    return {
      valid: false,
      user: window.localStorage.getItem("username"),
      rating: 5,
      comment: {
          label: getString('projects', 'writeComment'),
          rule: [(v) => !!v || getString("projects", "writeCommentError")],
          value: "",
        },
    };
  },
  methods: {
    getString,
      validate() {
      this.$refs.newComment.validate();
    },
    async submit() {
      this.validate();
      if (this.valid) {
        await apiService(`/api/projects/${this.projectId}/comment/`, "POST", {
          content: this.comment.value,
          rating: this.rating,
          project: this.projectId,
        }).then(async (data) => {
          if (data != "wrong data") {
            console.log("udało się");
            this.$emit("addedComment");
          }
        });
      }
    },
  },
};
</script>

<style
  link
  rel="stylesheet"
  href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
  scope
>
.commentContainer {
  border: solid 1px black;
  border-radius: 25px;
  /* height: 400px; */
  margin: 20px;
  padding: 20px;
  width: 400px;
}
.topSection {
  display: flex;
  margin-bottom: 10px;
}
.leftTopSection {
  flex: 50%;
}
.rightTopSection {
  align-items: flex-end;
}
.bottomSection {
  align-items: center;
  display: flex;
}
.submitCommentIcon {
  margin-left: 5px;
}
.postComment {
  width: 40px;
}
textarea {
  background-color: #e8e8e8;
  height: 50px;
  padding: 6px 10px;
  width: 100%;
}
</style>
