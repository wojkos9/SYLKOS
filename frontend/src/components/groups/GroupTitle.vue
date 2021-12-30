<template>
  <div class="allTitle">
    <div class="nextToGroups">
      <div class="groupsTitle">
        {{ getString("groups", "groups").toUpperCase() }} ({{
          group.members
        }})
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "groupTitle",
  props: ["numberOfAllGroups"],
  data() {
    return {
      groupName: "",
      title: "Osiedle Kwiatowe",
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
    sendMssg(str) {
      this.$emit("changeSearcgName", str);
    },
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
.groupsTitle {
  align-self: center;
  font-size: 2rem;
  margin-bottom: 15px;
  text-align: center;
}

.nextToGroups {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.allTitle {
  margin-bottom: 50px;
  margin-top: 50px;
  width: 100%;
}
.sortGroups {
  width: 200px;
}

.listFlex {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  /* margin-top: -55px; */
}

@media only screen and (max-width: 1000px) {
  .title {
    font-size: 1.875rem;
  }
}

@media only screen and (max-width: 900px) {
  .title {
    font-size: 1.5rem;
  }
}

@media only screen and (max-width: 800px) {
  .title {
    font-size: 1.25rem;
  }
  .allTitle {
    margin-bottom: 60px;
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
