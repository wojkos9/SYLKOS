<template>
  <div>

    <discussion-title />
    <div class="options">
      <Sort :options="sortOptions" />
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
import Sort from '../components/UI/Sort.vue'
import Comment from "../components/project/Comment.vue";
import addComment from "../components/project/AddComment.vue";
import DiscussionTitle from '../components/project/DiscussionTitle.vue';
export default {
  name: "projectOptions",
  //   props: ['userName', 'rating', 'postingDate', 'commentText', 'likes', 'dislikes', 'userVotedFor'],
  props:{
    id: {
            type: Number,
            required: true,
            },
  },
  data() {
    return {
      userName: "Mateusz Kluba",
      rating: "3.5",
      postingDate: "13.09.2021",
      commentText:
        "Świetny pomysł! Sam nieraz widzę potrzebę lepszego oświetlenia naszych alejek. Chciałbym jednak znać więcej szczegółów",
      likes: "0",
      dislikes: "0",
      userVotedFor: "nothing",
      sortOptions: [ 
        [this.getString('commentSorting', 'ratingASC'), this.sortByNameDesc],
        [this.getString('commentSorting', 'ratingDESC'), this.sortByMembersDesc],
        [this.getString('commentSorting', 'newest'), this.sortByMembers],
        [this.getString('commentSorting', 'oldest'), this.sortByMembers]],
  }
  },
  components: {
    Sort,
    Comment,
    addComment,
    DiscussionTitle,
  },
  methods: {
    getString,
    sortByName(){
      console.log("sortByName")
    },
    sortByMembers(){
      console.log("sortByMembers")
    },
    sortByNameDesc(){
      console.log("sortByNameDesc")
    },
    sortByMembersDesc(){
      console.log("sortByMembersDesc")
    }
  },
};
</script>

<style scoped>
.comments {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 50px;
}
.projectTitle {
  font-family: "playfair display";
  font-size: 50px;
}

.projectOptions{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  /* margin-bottom: 100px; */
  /* margin-top: -280px; */
}

@media only screen and (max-width: 1100px) {

.projectOptions{
    margin-top: 15px;
    justify-content: center;
  }
}
</style>
