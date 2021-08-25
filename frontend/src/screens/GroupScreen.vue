<template>
  <div class="area">
    <div class="groupName">
      {{ groupName }}
    </div>
    <div class="sectionsContainer">
      <div class="leftSection">
        <group-info
        :region="region"
        :areaType="areaType"
        :usersNumber="usersNumber"
        :registeredProjects="registeredProjects"
        :activeVotings="activeVotings"
        :yearCosts="yearCosts"
        />
        <div class="votingsListContainer">
       
         
            <voting-list
              :id="id"
            />
        </div>
        
      </div>
      <div class="rightSection">
        <div class="gallery">
          <div class="galleryTitle">
            {{ getString('groups', 'galleryTitle').toUpperCase() }}
          </div>
          <div class="images">
            <div class="leftArrow" v-if="imageId > 2">
              <v-mdi name="mdiChevronLeftCircle"></v-mdi>
            </div>
            <div class="image">
              <img src="https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg"/>
            </div>
            <div class="rightArrow" v-if="imageId < totalImages">
              <v-mdi name="mdiChevronRightCircle"></v-mdi>
            </div>
          </div>
          <div class="imageDescription">
              {{ imageDescription }}
          </div>
          <div class="imageId">
              {{ imageId }}/{{ totalImages }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import VotingList from "../components/groupDetails/VotingList.vue";
import GroupInfo from '../components/groupDetails/GroupInfo.vue';

export default {
  name: "groupScreen",
  components: {
    VotingList,
    GroupInfo
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      groupName: "Osiedle Kwiatowe",
      region: "Wilda",
      areaType: "osiedle",
      usersNumber: 46,
      activeVotings: 3,
      registeredProjects: 12,
      yearCosts: "34 000 zł",
      imageDescription: "Ulica Leśna 34",
      imageId: 3,
      totalImages: 35
    };
  },
  methods: {
    getString,
    getColor,
  },
};
</script>

<style scoped>
  .groupName{
    display: flex;
    font-family: "playfair display";
    font-size: 35px;
    justify-content: center;
    margin: 50px;
    padding-bottom: 30px;
    padding-top: 10px;
  }
  .sectionsContainer{
    display: flex;
    justify-content: space-around;
  }
  .leftSection {
    padding: 20px;
    font-size: 20px;
  }
  .votingsListContainer{
    margin-top: 20px;
  }
  .votingsListTitle{
    font-family: "playfair display";
    font-weight: 700;
    margin-bottom: 30px;
    margin-top: 30px;
  }
  .galleryTitle{
    display: flex;
    font-family: "playfair display";
    font-size: 25px;
    justify-content: center;
    margin: 20px;
  }
  .images{
    display: flex;
  }
  .image{
    width: 600px;
    margin: 20px;
  }
  .leftArrow, .rightArrow{
    align-items: center;
    display: flex; 
    justify-content: center;
    margin: 10px;
  }
  .imageDescription, .imageId, .totalImages {
    display: flex;
    font-size: 15px;
    justify-content: center;
    margin-top: 10px;
  }
</style>