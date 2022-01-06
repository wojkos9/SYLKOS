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
          {{ moment(new Date()).format("YYYY.MM.DD HH:mm") }}
        </div>
      </div>

      <div class="bottomSection" id="addComment">
        <v-textarea
          class="addComment"
          :label="comment.label"
          v-model="comment.value"
        >
        </v-textarea>

        <div class="submitCommentIcon" @click="submit">
          <v-mdi class="postComment" name="mdiSend"></v-mdi>
        </div></div
    ></v-form>
  </div>
</template>

<script>
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
        label: this.$t("writeComment"),
        value: "",
      },
    };
  },
  methods: {
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
            this.$emit("addedComment");
          }
        });
      }
    },
  },
};
</script>

<style scoped>
.commentContainer {
  /* border-radius: 25px; */
  margin: 20px;
  padding: 20px;
  max-width: 450px;
  width: 450px;
  background-color: var(--v-primary-lighten3);
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
textarea {
  width: 250px !important;
}
.submitCommentIcon {
  margin-left: 5px;
  cursor: pointer;
}

.postComment {
  width: 40px;
}
.v-input {
  width: 100%;
}

textarea {
  background-color: var(--v-primary-lighten4);
  height: 50px;
  padding: 6px 10px;
}

.v-input textarea {
  padding: 10px;
}
.userName {
  max-width: 300px;
  font-size: 21px !important;
}

@media only screen and (max-width: 500px) {
  #addComment textarea {
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
  .userName {
    text-align: center;
    order: 1;
  }
  .rightTopSection {
    text-align: center;
    order: 2;
    width: 100%;
  }
  .rating {
    order: 3;
  }

  .commentContainer {
    border: solid 1px black;
    /* border-radius: 25px; */
    /* height: 400px; */
    margin: 10px;
    padding: 20px;
    max-width: 250px;
    z-index: 10000000;
  }

  #addComment textarea {
    width: 200px !important;
  }

  .topSection {
    flex-wrap: wrap;
  }
}
</style>
