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
          ></v-rating>
        </div>
      </div>
      <div class="rightTopSection">
        {{ moment(new Date()).format("DD.MM.YYYY") }}
      </div>
    </div>
 
    <div class="bottomSection" id="addComment">
      <v-textarea
        class="addComment"
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

     <v-dialog v-model="dialog3" width="500">
      <v-card>
        <v-card-title
          class="text-h4 grey lighten-2 p-4 d-flex justify-content-center"
        >
          <!-- {{ group.name }} -->
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <span class="d-flex justify-content-center">
            {{ getString("projects", "successAdd") }}</span
          >
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog3 = false">
            {{ getString("projects", "ok") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

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
      dialog3: false,
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
            this.dialog3= true;
            this.$emit("addedComment");
          }
        });
      }
    },
  },
};
</script>

<style
  
>
.commentContainer {
  border: solid 1px black;
  border-radius: 25px;
  /* height: 400px; */
  margin: 20px;
  padding: 20px;
  max-width: 400px;
  width: 400px
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
textarea{
  width: 250px !important;
}
.submitCommentIcon {
  margin-left: 5px;
  cursor: pointer;
}

.postComment {
  width: 40px;
}
.v-input{
  width: 100%
}

textarea {
  background-color: var(--v-primary-lighten4);
  height: 50px;
  padding: 6px 10px;
}

.v-input textarea{
  padding: 10px
}
.userName{
  max-width: 300px;
}

@media only screen and (max-width: 500px) {
#addComment textarea{
  width: 200px !important;
}
.commentContainer {
  width: 300px;
}
}

@media only screen and (max-width: 400px) {

.bottomSection {
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.userName{
  text-align: center;
  order: 1;
}
.rightTopSection{
  text-align: center;
  order:2;
  width: 100%;
}
.rating{
  order:3;
}

.commentContainer {
  border: solid 1px black;
  border-radius: 25px;
  /* height: 400px; */
  margin: 10px;
  padding: 20px;
  max-width: 250px;
  z-index: 10000000;
}

 #addComment textarea{
  width: 200px !important;
}

.topSection {
 flex-wrap: wrap;
}
}
</style>
