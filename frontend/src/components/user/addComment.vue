<template>
  <div class="commentContainer">
    <div class="topSection">
      <div class="leftTopSection">
        <div class="userName">
          {{ userName }}
        </div>
        <div class="rating">
          <stars v-bind:stars="2.5" />
        </div>
      </div>
      <div class="rightTopSection">
          {{ moment(new Date()).format('DD.MM.YYYY') }}
      </div>
    </div>
    <div class="bottomSection">
      <textarea>
                Write a comment..
            </textarea
      >
      <div class="submitCommentIcon" @click="postComment">
        <v-mdi class="postComment" v-style="icon" name="mdiSend"></v-mdi>
      </div>
    </div>
  </div>
</template>

<script>
    import Stars from '../UI/Stars.vue'
    export default {
        name: "addComment",
        props: [],
        data(){
            return {
                userName: 'Mateusz Kluba'
            }
        },
        components:{
            Stars
        },
        methods:{
            postComment(){
              console.log("you posted a comment!")
            }
        }
    }
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
textarea {
  background-color: #e8e8e8;
  height: 50px;
  padding: 6px 10px;
  width: 100%;
}
</style>
