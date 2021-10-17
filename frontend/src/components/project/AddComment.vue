<template>
  <div class="commentContainer">
    <div class="topSection">
      <div class="leftTopSection">
        <div class="userName">
          {{ userName }}
        </div>
        <div class="rating">
          <stars :rating="pickedRating" v-on:ratingChanged="updateRating" />
        </div>
      </div>
      <div class="rightTopSection">
        {{ moment(new Date()).format("DD.MM.YYYY") }}
      </div>
    </div>
    <div class="bottomSection">
      <v-form v-model="valid" ref="addCommentForm" id="addCommentForm">
        <v-container>
          <v-text-field
            class="textarea"
            dense
            v-model="comment.value"
            :rules="comment.rule"
            :label="comment.label"
            required
          ></v-text-field>
        </v-container>
      </v-form>
      <div class="submitCommentIcon" @click="postComment">
        <v-mdi class="postComment" name="mdiSend"></v-mdi>
      </div>
    </div>
  </div>
</template>

<script>
import Stars from "../UI/Stars.vue";
import { getString } from "@/language/string.js";
import { apiService } from "@/common/api.service.js";
export default {
  name: "addComment",
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    maxLength: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      userName: "",
      pickedRating: 5,
      valid: false,
      comment: {
        label: getString("addComment", "commentText"),
        rule: [(v) => !!v || getString("addComment", "commentTextError")],
        value: "",
      },
    };
  },
  components: {
    Stars,
  },
  methods: {
    updateRating(value) {
      this.pickedRating = value;
    },
    postComment() {
      this.validate();
      if (this.valid) {
        console.log("trying to post your comment...");
        apiService("/api/projects/" + this.projectId + "/comment/", "POST", {
          content: this.comment.value,
          rating: this.pickedRating,
          project: this.projectId,
        });
        console.log("you posted a comment!");
        this.$emit('new-comment', 'refresh');
        this.clear()
      } else {
        console.log("there were some errors");
      }
    },
    async setUserInfo() {
      this.userName = window.localStorage.getItem("username");
    },
    clear() {
      this.comment.value = "";
      this.reset();
    },
    reset() {
      this.$refs.addCommentForm.reset();
    },
    validate() {
      this.$refs.addCommentForm.validate();
    },
  },
  created() {
    this.setUserInfo();
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
.textarea {
  background-color: #e8e8e8;
  height: 50px;
  padding: 6px 10px;
  width: 100%;
}
</style>
