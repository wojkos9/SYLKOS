<template>
  <div class="likes">
    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <div class="plus" >
          <v-btn
            color="transparent"
            dark
            style="box-shadow: none; padding: 0; max-width: 10px"
            width="20"
            v-bind="attrs"
            v-on="on"
          >
            <div v-if="comment.user_has_liked" @click="addedReaction=true">
              <v-mdi name="mdiPlusThick" color="#49e61e"></v-mdi>
            </div>
            <div v-else>
              <div class="plus" @click="check(incrementLikes)">
                <v-mdi name="mdiPlusThick"></v-mdi>
              </div>
            </div>
          </v-btn>
        </div>
      </template>
      <div v-if="comment.user_has_liked"><span>Popieram</span></div>
      <div v-else><span>Wyraź wsparcie</span></div>
    </v-tooltip>

    {{ comment.likes_count }}

    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <div class="plus" >
          <v-btn
            color="transparent"
            dark
            style="box-shadow: none; padding: 0; max-width: 10px"
            width="20"
            v-bind="attrs"
            v-on="on"
          >
            <div v-if="comment.user_has_disliked" @click="addedReaction=true">
              <v-mdi name="mdiMinusThick" color="#ff0015"></v-mdi>
            </div>
            <div v-else>
              <div class="minus" @click="check(changeDislikes)">
                <v-mdi name="mdiMinusThick"></v-mdi>
              </div>
            </div>
          </v-btn>
        </div>
      </template>

      <div v-if="comment.user_has_disliked"><span>Nie zgadzam się</span></div>
      <div v-else><span>Wyraź dezaprobatę</span></div>
    </v-tooltip>

    {{ comment.dislikes_count }}

     <v-snackbar
      v-model="addedReaction"
      :multi-line="multiLine"
    >
     Już zareagowałeś na ten komentarz
    </v-snackbar>
     <v-snackbar
      v-model="newReaction"
      :multi-line="multiLine"
    >
     Reakcja dodana!
    </v-snackbar>
 
  
  </div> 
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "plusMinusRating",
  props: ["comment"],
  data() {
    return {
      newReaction: false,
      addedReaction: false,
    }
  },
  methods: {
    check(funName) {
      if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("unauthorized")
      ) {
        this.$root.$refs.App.ifLogin();
      } else {
        console.log(funName);
        funName();
      }
    },
    async incrementLikes() {
      await apiService(
        `/api/comments/${this.comment.id}/like`,
        "POST",
        {}
      ).then(async (data) => {
        if (data != "wrong data") {
          this.comment.likes_count += 1;
          this.comment.user_has_liked = true;
          this.newReaction = true;
        }
      });
    },
    async changeDislikes() {
      await apiService(
        `/api/comments/${this.comment.id}/dislike`,
        "POST",
        {}
      ).then(async (data) => {
        if (data != "wrong data") {
          // this.comment.likes_count = data.likes_count;
          this.comment.dislikes_count += 1;
          this.comment.user_has_disliked = true;
          this.newReaction = true;
          // this.comment.user_has_liked = data.user_has_liked;
        }
      });
    },
  },
};
</script>

<style link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons" scoped>
.likes {
  /* border: solid 1px black; */
  display: flex;
  font-size: 21px;
  align-items: center;
}
.plus {
  color: green;
  margin-right: 5px;
}
.minus {
  color: red;
  margin-left: 5px;
  margin-right: 5px;
}

.v-btn:not(.v-btn--round).v-size--default {
  max-width: 64px !important;
  min-width: 20px !important;
  width: 10px !important;
  margin-right: 4px;
  margin-left: 6px;
}
</style>