<template>
  <div class="allTitle">
    <div class="nextToGroups">
      <div class="title">
        {{ getString("groups", "groups").toUpperCase() }} ({{
          numberOfAllGroups
        }})
      </div>
    </div>

  <div class="listFlex">
    <div class="myList">
        <div class="list">
          <md-list class="list">
            <md-list-item md-expand>
              <md-icon>sort</md-icon>
              <span class="md-list-item-text">{{
                getString("groups", "sort")
              }}</span>
              <md-list slot="md-expand">
                <md-list-item class="md-inset">{{
                  getString("groups", "name")
                }}</md-list-item>
                <md-list-item class="md-inset">{{
                  getString("groups", "membersNumberSort")
                }}</md-list-item>
              </md-list>
            </md-list-item>
          </md-list>
        </div>
      </div>
      </div>

  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "title",
  props: ["numberOfAllGroups"],
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
  computed: {
    filtrList() {
      return {
        backgroundColor: getColor("navbar"),
      };
    },
  },
};
</script>

<style>
.title {
  font-family: "Playfair Display";
  align-self: center;
  font-size: 32px;
  font-weight: 500;
  margin-bottom: 15px;
  text-align: center;
}

.nextToGroups {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.allTitle {
  margin-top: 50px;
  margin-bottom: 50px;
  width: 100%;
}

.myList {
  background-color: red;
  /* border: solid; */
  margin-right: 50px;
  width: 300px;
  position: absolute;
 
}

.listFlex{
 display: flex;
 flex-direction: row;
justify-content: flex-end;
margin-top: -50px;
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
  .allTitle{
    margin-bottom: 60px;
  }

  .myList {
    /* align-self: center; */
    /* width: 200px; */
    margin-right: 0px;
  }

  .listFlex{
    margin-top:20px;
    justify-content: center;
    /* margin-right: 0px; */
  }
}

@media only screen and (max-width: 700px) {
  .nextToGroups {
    flex-direction: column;
  }


  
}
</style>
