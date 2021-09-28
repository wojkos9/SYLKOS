<template>
  <div>
    <div class="row">
      <div class="col-sm-5" />
      <div class="col-sm-2">
        <div class="title">
            {{ title }}
        </div>
      </div>
      <div class="col-sm-3" />
      <div class="col-sm-2">
        <div class="sortList">
          <button-sort 
            v-bind:title="getString('commentSorting', 'sort')"
            v-bind:option1="getString('commentSorting', 'ratingASC')"
            v-bind:option2="getString('commentSorting', 'ratingDESC')"
            v-bind:option3="getString('commentSorting', 'newest')"
            v-bind:option4="getString('commentSorting', 'oldest')"
          />
        </div>
      </div>
    </div>

    <div class="commentSection">
      <div class="comments">
        <add-comment />
        <comment 
        :userName="userName"
        :rating="rating"
        :postingDate="postingDate"
        :commentText="commentText"
        :likes="likes"
        :dislikes="dislikes"
        :userVotedFor="userVotedFor"
        />
        <comment 
        :userName="userName"
        :rating="rating"
        :postingDate="postingDate"
        :commentText="commentText"
        :likes="likes"
        :dislikes="dislikes"
        :userVotedFor="userVotedFor"
        />
        <comment 
        :userName="userName"
        :rating="rating"
        :postingDate="postingDate"
        :commentText="commentText"
        :likes="likes"
        :dislikes="dislikes"
        :userVotedFor="userVotedFor"
        />
        <comment 
        :userName="userName"
        :rating="rating"
        :postingDate="postingDate"
        :commentText="commentText"
        :likes="likes"
        :dislikes="dislikes"
        :userVotedFor="userVotedFor"
        />
        <comment 
        :userName="userName"
        :rating="rating"
        :postingDate="postingDate"
        :commentText="commentText"
        :likes="likes"
        :dislikes="dislikes"
        :userVotedFor="userVotedFor"
        />
        <comment 
        :userName="userName"
        :rating="rating"
        :postingDate="postingDate"
        :commentText="commentText"
        :likes="likes"
        :dislikes="dislikes"
        :userVotedFor="userVotedFor"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import ButtonSort from "./ButtonSort.vue";
import Comment from './Comment.vue';
import addComment from './AddComment.vue';
export default {
  name: "comments",
  props: ['userName', 'rating', 'postingDate', 'commentText', 'likes', 'dislikes', 'userVotedFor'],
  data() {
    return {
      title: getString("userPanel", "discussion"),
    };
  },
  components: {
    ButtonSort,
    Comment,
    addComment
  },
  methods: {
    getString,
  },
};
</script>

<style scoped>
.comments {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
}
.title {
    font-size: 50px;
}
</style>
