<template>
    <div class="likes">
        <div class="plus" @click="incrementLikes">
          <v-mdi name="mdiPlusThick"></v-mdi>
        </div>
        {{ likes }}
        <div class="minus" @click="incrementDislikes">
          <v-mdi name="mdiMinusThick"></v-mdi>
        </div>
        {{ dislikes }}
      </div>
</template>

<script>
    export default {
        name: "plusMinusRating",
        props: ['likes', 'dislikes', 'userVotedFor'],
        methods:{
            incrementLikes(){
                if(this.userVotedFor == "minus"){
                    this.likes++;
                    this.dislikes--;
                } else if(this.userVotedFor == "nothing"){
                    this.likes++;
                }
                this.userVotedFor = "plus";
            },
            incrementDislikes(){
                if(this.userVotedFor == "nothing"){
                    this.dislikes++;
                }
                else if(this.userVotedFor == "plus" ){
                    this.dislikes++;
                    this.likes--;
                } 
                this.userVotedFor = "minus";
            }
        }
    }
</script>

<style link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons" scoped>
    .likes {
        /* border: solid 1px black; */
        display: flex;  
        font-size: 25px;
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