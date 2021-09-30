<template>
  <div class="area">
    <div class="groupName">
      {{ group.name }}
    </div>
    <div class="sectionsContainer">
      <div class="leftSection">
        <group-info
          :region="region"
          :areaType="areaType"
          :usersNumber="group.count_user"
          :registeredProjects="registeredProjects"
          :activeVotings="activeVotings"
          :yearCosts="yearCosts"
        />
        <div class="voting">
          <voting-list :id="id" />
        </div>
      </div>
      <div class="rightSection">
        <div>
          <Carousel :slides="group.images" :ifRoute="ifRoute" :group="group" :title="group.name"/>{{group.photos}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import VotingList from "../components/groupDetails/VotingList.vue";
import GroupInfo from "../components/groupDetails/GroupInfo.vue";
import Carousel from "../components/UI/Carousel.vue";
import { apiService } from "@/common/api.service.js";

export default {
  name: "groupScreen",
  components: {
    VotingList,
    GroupInfo,
    Carousel,
  },
  props: {
    id: {
      
      required: true,
    },
  },
  data() {
    return {
      region: "Wilda",
      areaType: "osiedle",
      usersNumber: 46,
      activeVotings: 3,
      registeredProjects: 12,
      yearCosts: "34 000 zł",
      loading: true,
      totalImages: 35,
      group:true,
      slides: [
        {
          src:
            "https://martyloose.files.wordpress.com/2019/02/sunrise-wallpapers-28064-5395027.jpg",
          desc: "zdj",
        },
        {
          src:
            "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
          desc: "dd",
        },
        {
          src:
            "https://images.unsplash.com/photo-1612151855475-877969f4a6cc?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aGQlMjBpbWFnZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80",
          desc: "rodzinne okolice",
        },
      ],
      ifRoute: true,
    };
  },
  methods: {
    getString,
    getColor,
  },
  created(){
    document.title = this.groupName;
  },
  async beforeRouteEnter(to, from, next){
        if(to.params.id !== undefined){
            let endpoint = `api/groups/${to.params.id}/`
            let data = await apiService(endpoint)
            console.log(data)
            return next(vm => {
              vm.group = data

        });
        }else{
            return next()
        }
       
    },
};
</script>

<style scoped>
.area {
  background-color: white;
  margin: 30px;
  border-radius: 20px;
  padding-bottom: 50px;
}
.groupName {
  display: flex;
  font-size: 2rem;
  justify-content: center;
  margin: 50px;
  padding-bottom: 30px;
  padding-top: 50px;
  
}
.sectionsContainer {
  display: flex;
  justify-content: space-around;
}
.leftSection {
  padding: 20px;
  font-size: 20px;
  /* margin-left: -100px; */
  width: 1000px;
}

.rightSection {
  padding: 20px;
  font-size: 20px;
  /* width: 1000px; */
  margin-left: 100px;
  max-width: 800px;
}

.galleryTitle {
  display: flex;
  font-size: 25px;
  justify-content: center;
  margin: 20px;
}
.images {
  display: flex;
}
.image {
  width: 600px;
  margin: 20px;
}
.leftArrow,
.rightArrow {
  align-items: center;
  display: flex;
  justify-content: center;
  margin: 10px;
}
.imageDescription,
.imageId,
.totalImages {
  display: flex;
  font-size: 15px;
  justify-content: center;
  margin-top: 10px;
}

@media only screen and (max-width: 1500px) {
  .sectionsContainer {
    flex-direction: column;
    align-content: center;
    align-items: center;
  }

  .voting {
    margin-top: 70px;
  }

  .rightSection{
    margin-left: 0px;
  }
}
@media only screen and (max-width: 750px) {

  .rightSection{
    max-width: 100%;
  }
}
</style>
