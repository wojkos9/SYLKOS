<template>
  <div class="area">
    <div class="leftSection">
        <div class="title">
            {{ title }}
        </div>
        <div class="description">
            {{ description }}
        </div>
        <div class="price">
            {{ getString('userPanel', 'price') }} : {{ price }}
        </div>
    </div>
    <div class="rightSection">
      <div class="likes">
        <plus-minus-rating
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
        />
      </div>
      <div class="gallery">
            <div class="leftArrow">
                <v-mdi  name="mdiChevronLeft"></v-mdi>
            </div>
            <div class="galleryImage">
                <img src="https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg">
            </div>
            <div class="rightArrow">
                <v-mdi  name="mdiChevronRight"></v-mdi>
            </div>
      </div>
      <div class="commentSectionRedirectButton">
          <router-link :to="{ name: 'project', params:{id:1}}"> {{ getString('userPanel', 'seeDiscussion') }}</router-link> 
      </div>
      <div class="voteForProject">
          <label>
              <b>{{ getString('userPanel', 'voteForThisProject') }}</b>
              <input type="radio" style="margin-left: 5px">
          </label>
      </div>
    </div>
  </div>
</template>

<script>
    import { getString } from "@/language/string.js";
import plusMinusRating from '../UI/PlusMinusRating.vue';
    export default {
  components: { plusMinusRating },
        name: "votingProject",
        props: ['title', 'description', 'price','likes', 'dislikes', 'userVotedFor'],
        data(){
            return {
                
            }
        },
        methods:{
            getString
        }
    }
</script>

<style link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons" scoped>
    .area {
        border: solid 1px black;
        border-radius: 25px;
        display: flex;
        margin: 40px;
        padding: 20px;
        width: 700px;
    }
    .title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 20px;
        margin-top: 20px;
        
    }
    .description {
        margin-bottom: 20px;
    }
    .likes {
        /* border: solid 1px black; */
        display: flex;  
        font-family: "playfair display";
        font-size: 25px;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
    .gallery {
        display: flex;
        margin-bottom: 10px;
    }
    .leftArrow, .rightArrow {
        align-items: center;
        display: flex; 
        justify-content: center;
    }
    .galleryImage {
        width: 300px;
    }   
    .commentSectionRedirectButton, .voteForProject {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 10px;
        margin-right: 10px;
    }
    @media only screen and (max-width: 1300px) {
        .galleryImage{
        width: 500px;
        }
        .area{
            flex-direction: column;
        }
    }
</style>