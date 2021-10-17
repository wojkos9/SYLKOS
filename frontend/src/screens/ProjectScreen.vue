<template>
  <div class="area">
    <div class="projectDetails">
      <div class="row">
        <div class="col-sm-5" />
        <div class="col-sm-4">
          <div class="projectTitle">
            {{ projectName }}
          </div>
        </div>
        <div class="col-sm-3">
          <div class="groupName">({{ groupName }})</div>
        </div>
      </div>
      <div class="projectDescription">
        {{ projectDescription }}
      </div>
      <div class="projectInfoAndGallery">
        <div class="projectInfo">
          <project-info
            :price="price"
            :votingEndDate="votingEndDate"
            :projectUploadDate="projectUploadDate"
          />
        </div>
        <div class="gallery">
          <Carousel
            :slides="slides"
            :ifRoute="ifRoute"
            :group="group"
            :title="groupName"
          />
        </div>
      </div>

      <div class="commentSection">
        <discussion-title />
        <div class="options">
          <Sort :options="sortOptions" />
        </div>
        <div class="comments">
          <add-comment
            :maxLength="maxCommentLength"
            :projectId="id"
            v-on:new-comment="updateComments"
          />
          <div v-for="comment in comments" :key="comment.id">
            <Comment
              v-bind:userName="comment.author"
              v-bind:rating="rating"
              v-bind:postingDate="comment.created_at"
              v-bind:commentText="comment.content"
              v-bind:likes="comment.likes_count"
              v-bind:dislikes="comment.dislikes_count"
              v-bind:userVotedFor="userVotedFor"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import Sort from "../components/UI/Sort.vue";
import Comment from "../components/project/Comment.vue";
import addComment from "../components/project/AddComment.vue";
import DiscussionTitle from "../components/project/DiscussionTitle.vue";
import projectInfo from "../components/projects/ProjectInfo.vue";
import Carousel from "../components/UI/Carousel.vue";
import { apiService } from "@/common/api.service.js";

export default {
  name: "projectOptions",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      userName: "Mateusz Kluba",
      rating: 3.5,
      postingDate: "13.09.2021",
      commentText:
        "Świetny pomysł! Sam nieraz widzę potrzebę lepszego oświetlenia naszych alejek. Chciałbym jednak znać więcej szczegółów",
      likes: "0",
      dislikes: "0",
      userVotedFor: "nothing",
      sortOptions: [
        [this.getString("commentSorting", "ratingASC"), this.sortByNameDesc],
        [
          this.getString("commentSorting", "ratingDESC"),
          this.sortByMembersDesc,
        ],
        [this.getString("commentSorting", "newest"), this.sortByMembers],
        [this.getString("commentSorting", "oldest"), this.sortByMembers],
      ],
      price: "20 000zł",
      votingEndDate: "23.09.2022",
      projectUploadDate: "21.08.2022",
      groupName: "Osiedle Kwiatowe",
      group: true,
      comments: [],
      commentsCount: "",
      maxCommentLength: 1000,
      slides: [
        {
          src: "https://martyloose.files.wordpress.com/2019/02/sunrise-wallpapers-28064-5395027.jpg",
          desc: "zdj",
        },
        {
          src: "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
          desc: "dd",
        },
        {
          src: "https://images.unsplash.com/photo-1612151855475-877969f4a6cc?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aGQlMjBpbWFnZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80",
          desc: "rodzinne okolice",
        },
      ],
      ifRoute: true,
      projectName: "Oświetlenie uliczek",
      projectDescription:
        "Ulice naszego osiedla są bardzo ciemne. Nocą w drodze do domu nie da się przejść przez żadną w żadną z nich w pełni oświetloną. Dlatego nasza propozycja to oświetlenie ulic. Zadbajmy o to, aby każdy mieszkaniec osiedla mógł czuć się bezpiecznie!",
    };
  },
  components: {
    Sort,
    Comment,
    addComment,
    DiscussionTitle,
    projectInfo,
    Carousel,
  },
  methods: {
    getString,
    sortByName() {
      console.log("sortByName");
    },
    sortByMembers() {
      console.log("sortByMembers");
    },
    sortByNameDesc() {
      console.log("sortByNameDesc");
    },
    sortByMembersDesc() {
      console.log("sortByMembersDesc");
    },
    async getAllComments() {
      const data = await apiService("/api/projects/" + this.id + "/comments/");
      this.commentsCount = data["count"];
      for (var comment of data["results"]) {
        this.comments.push(comment);
      }
    },
    updateComments(text) {
      this.getAllComments();
      console.log(text);
      this.$forceUpdate();
    },
  },
  created() {
    this.getAllComments();
    console.log(this.commentsCount);
  },
};
</script>

<style scoped>
.row {
  margin-bottom: 50px;
  margin-top: 50px;
}

.projectTitle {
  font-size: 40px;
}

.groupName {
  font-size: 30px;
}
.projectDescription {
  font-size: 20px;
  padding-left: 100px;
  padding-right: 100px;
}
.projectInfoAndGallery {
  display: flex;
  justify-content: space-around;
}
.projectInfo {
  align-items: center;
  display: flex;
  font-size: 30px;
  justify-content: center;
}
.gallery {
  width: 800px;
}
.comments {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 50px;
}

@media only screen and (max-width: 1100px) {
  .projectOptions {
    margin-top: 15px;
    justify-content: center;
  }
}
</style>
