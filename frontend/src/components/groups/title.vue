
<template>
  <div class="allTitle">
    <div class="title">{{ getString("groups", "groups") }} ({{numberOfAllGroups}})</div>

      <div class="myList">
    <div class="list">
      <md-list :md-expand-single="expandSingle" class="list">
         <md-list-item md-expand>
          <md-icon>sort</md-icon>
          <span class="md-list-item-text">{{ getString('groups', 'sort')}}</span>

          <md-list slot="md-expand">
            <md-list-item class="md-inset">{{ getString('groups', 'name')}}</md-list-item>
            <md-list-item class="md-inset">{{ getString('groups', 'membersNumberSort')}}</md-list-item>
          </md-list>
        </md-list-item>
      </md-list>
    </div>    
  </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "title",
  props:["numberOfAllGroups"],
  components: {},
  data() {
    return {
      title: "Osiedle Kwiatowe",
      desc: "Oswietlenie wszystkich zaciemnionych ulic",
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
    };
  },
  methods: {
    getString,
    getColor,
  },
  computed:{
    filtrList(){
      return{
      backgroundColor: getColor("navbar"),
    }
    }
    
  }
};
</script>

<style>

.title {
  font-family: "Playfair Display";
  align-self: center;
  font-size: 32px;
  font-weight: 500;
  margin-bottom: 15px;
}

.allTitle{
  margin-top: 50px;
  margin-bottom: 50px;
}

.myList{
  background-color: red;
}


@media only screen and (max-width: 1000px) {
  .title {
    font-size: 27px;
  } 
 }

@media only screen and (max-width: 900px) {
  .title {
    font-size: 24px;
  } 
 }

 @media only screen and (max-width: 800px) {
  .title {
    font-size: 20px;
  } 
 }

</style>
