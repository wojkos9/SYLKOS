<template>
  <div class="allTitle">
    <div class="nextToGroups">
      <div class="title">
        {{ getString("projects", "title").toUpperCase() }} ({{
          numberOfAllProjects
        }})
      </div>
    </div>
    
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "projectsTitle",
  props: ["numberOfAllProjects"],
  data() {
    return {
      groupName: "",
      title: "siatkówka plazowa",
      desc: "Oswietlenie wszystkich zaciemnionych ulic",
      image:
        "https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg",
      mainTitle: "Grupy, do kórych należysz",
      projectsTitle: "Projekty, na które głosowałes",
      sideDrawer: false,
      sortGroups: "",
    };
  },
  methods: {
    getString,
    getColor,
    clearInput() {
      this.groupName = "";
      this.$emit("changeSearcgName", "");
    },
    sendMssg(str){
      console.log('tak')
      this.$emit("changeSearcgName", str);
    }
  },
  computed: {
    filtrList() {
      return {
        backgroundColor: getColor("navbar"),
      };
    },
  },
  watch: {
    groupName: function(val) {
      this.$emit("changeSearcgName", val);
    },
  },
};
</script>

<style scoped>
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
  justify-content: center;
}


.allTitle {
  margin-top: 50px;
  margin-bottom: 50px;
  width: 100%;
}
.sortGroups {
  width: 200px;
}

.myList {
  background-color: red;
  margin-right: 50px;
  width: 300px;
  position: absolute;
}



.listFlex {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-top: -55px;
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
  .allTitle {
    margin-bottom: 60px;
  }

  .myList {
    /* align-self: center; */
    /* width: 200px; */
    margin-right: 0px;
  }

  .listFlex {
    margin-top: 20px;
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
