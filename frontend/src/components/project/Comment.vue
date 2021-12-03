<template>
  <div class="commentContainer">
    <div class="comment-row-1">
      <div class="comment-author">
        <div class="comment-imauthor" v-if="author">
          <div>{{ author }}</div>
          <div
            class="comment-icons"
            v-if="loggedUser == author"
            @click="dialog = true"
          >
            <v-icon>mdi-delete</v-icon>
          </div>
          <div v-if="loggedUser == author" @click="editComment">
            <v-icon>mdi-pencil</v-icon>
          </div>
        </div>
        <div v-else>
          {{ comment.author }}
        </div>
      </div>
      <div class="comment-data">
        <div class="date">
          {{ comment.created_at }}
        </div>
      </div>
    </div>

    <div class="comment-row-1 comment-stars">
      <v-rating
        v-model="comment.rating"
        color="yellow darken-3"
        background-color="grey darken-1"
        empty-icon="$ratingFull"
        half-icon="mdi-star-half"
        half-increments
        hover
        medium
        readonly
      ></v-rating>

      <plus-minus-rating
        :likes="comment.likes_count"
        :dislikes="comment.dislikes_count"
        :userVotedFor="comment.user_has_liked"
      />
    </div>
    <div class="comment-content">
      {{ comment.content }}
    </div>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-text class="text-h6  lighten-2 p-4 ">
          <span class="d-flex justify-content-center">
            {{ getString("projects", "deleteCommnet") }}</span
          >
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog = false">
            {{ getString("projects", "cancel") }}
          </v-btn>
          <v-btn text @click="deleteComment">
            {{ getString("projects", "submit") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog2" width="500">
      <v-card>
        <v-card-text class="text-h6  lighten-2 p-4 ">
          <span class="d-flex justify-content-center">
            {{ getString("projects", "success") }}</span
          >
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog2 = false">
            {{ getString("projects", "ok") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog3" width="500" id="editCommentDialog">
      <v-card>
        <v-card-title class="p1 d-flex justify-content-center">
          <span class="d-flex justify-content-center">
            {{ getString("projects", "edit") }}</span
          >
        </v-card-title>

        <v-card-text>
          <v-form>
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
            <v-textarea
              style=" width: 100%;"
            
              :rules="myComment.rule"
              v-model="myComment.value"
            >
            </v-textarea>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog3 = false">
            {{ getString("projects", "editCancel") }}
          </v-btn>
          <v-btn text @click="editPutComment">
            {{ getString("projects", "editOk") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import PlusMinusRating from "../UI/PlusMinusRating.vue";
import { mdiDelete } from "@mdi/js";
import { apiService } from "@/common/api.service.js";
import { getString } from "@/language/string.js";

export default {
  name: "comment",
  props: ["comment", "ifDelete", "author"],
  data() {
    return {
      loggedUser: "",
      dialog: false,
      dialog2: false,
      dialog3: false,
      rating: 5,
      icons: {
        mdiDelete,
      },
      myComment: {
        label: getString("projects", "editComment"),
        rule: [(v) => !!v || getString("projects", "editCommentError")],
        value: "",
      },
      ratingEdit: 5,
    };
  },
  components: {
    PlusMinusRating,
  },
  methods: {
    getString,
    async setUserInfo() {
      this.loggedUser = window.localStorage.getItem("username");
    },
    async editPutComment() {
      var endpoint = `api/comments/${this.comment.id}/`;
      console.log("edycja");
      await apiService(endpoint, "PUT", {
        content: this.myComment.value,
        rating: this.rating,
        project: this.comment.project,
      }).then(() => {
        this.dialog3 = false;
        this.$emit("deleteUpdate");
      });
    },
    async editComment() {
      this.myComment.value = this.comment.content;
      this.rating = this.comment.rating;
      this.dialog3 = true;
    },
    async deleteComment() {
      this.dialog = false;
      console.log("comment deleted");
      console.log(this.comment.id);
      let endpoint = `api/comments/${this.comment.id}/`;
      await apiService(endpoint, "DELETE").then(() => {
        // this.dialog2 = true;
        this.$emit("deleteUpdate");
      });
    },
  },
  created() {
    this.setUserInfo();
  },
};
</script>

<style scoped>
.commentContainer {
  background-color: var(--v-primary-lighten3);
}
.comment-row-1 {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
}

textarea {
  /* width: 100% */
  width: 400px;
}
.v-text-field {
  width: 400px;
}

.comment-data{
  font-size: 1rem;
}
.comment-author {
  font-weight: 700;
  padding-left: 10px;
  font-size: 1.5em;
}
.comment-imauthor {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.comment-icons {
  margin-left: 20px;
}
.comment-content {
  background: linear-gradient(
    var(--v-primary-lighten4),
    var(--v-secondary-lighten2)
  );
  margin-top: 1em;
  padding: 20px;
  border-radius: 40px;
  font-size: 1.3em;
}

.comment-stars {
  margin: 10px 0;
}

#editCommentDialog textarea {
  justify-self: center;
}
@media only screen and (max-width: 500px) {
  .comment-stars {
    flex-direction: column;
  }
  .comment-row-1 {
    flex-direction: column;
  }
  #editCommentDialog textarea {
    width: 350px !important;
  }
  .commentContainer {
    width: 300px;
  }
}
@media only screen and (max-width: 400px) {
  #editCommentDialog textarea {
    width: 350px !important;
  }
}
</style>
