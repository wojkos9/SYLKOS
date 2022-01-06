<template>
    <div class="likes">
        <div class="plus" @click="check(incrementLikes)">
          <v-mdi name="mdiPlusThick"></v-mdi>
        </div>
        {{ comment.likes_count }}
        <div class="minus" @click="check(incrementDislikes)">
          <v-mdi name="mdiMinusThick"></v-mdi>
        </div>
        {{ comment.dislikes_count }}
      </div>
</template>

<script>
    import { apiService } from "@/common/api.service.js";

    export default {
        name: "plusMinusRating",
        props: ['comment'],
        methods:{
            check(funName) {
      if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("unauthorized")
      ) {
        this.$root.$refs.App.ifLogin();
      } else {
        funName();
      }
    },
           async  incrementLikes(){
               
            await apiService(`/api/comments/${this.comment.id}/like`, "POST", {

            }).then(async (data) => {
            if (data != "wrong data") {
                this.comment.likes_count = data.likes_count;
                this.comment.dislikes_count = data.dislikes_count;
                this.comment.user_has_disliked = data.user_has_disliked;
                this.comment.user_has_liked = data.user_has_liked;
            }
            });
                    
            },
            async  incrementDislikes(){
               
            await apiService(`/api/comments/${this.comment.id}/dislike`, "POST", {

            }).then(async (data) => {
            if (data != "wrong data") {
                this.comment.likes_count = data.likes_count;
                this.comment.dislikes_count = data.dislikes_count;
                this.comment.user_has_disliked = data.user_has_disliked;
                this.comment.user_has_liked = data.user_has_liked;
            }
            });
                    
            },
        }
    }
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
</style>