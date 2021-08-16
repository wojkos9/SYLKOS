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
        <comment />
        <comment />
        <comment />
        <comment />
        <comment />
        <comment />
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import ButtonSort from "../UI/buttonSort.vue";
import Comment from './comment.vue';
import addComment from './addComment.vue';
export default {
  name: "comments",
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
    font-family: "playfair display";
    font-size: 50px;
}
</style>
