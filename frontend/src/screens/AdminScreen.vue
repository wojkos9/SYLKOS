<template>
  <div class="areaAdmin">
    <div class="titleAdmin">
      {{ title }}
    </div>

    <div class="options" >
      <div>
        <Option
          :title="group.title"
          :editAction="group.editAction"
          :newAction="group.newAction"
          v-on:change="resetAnother(group.id)"
          :key="group.key"
          class="oneOption"
        />
        <Option
          :title="project.title"
          :editAction="project.editAction"
          :newAction="project.newAction"
          v-on:change="resetAnother(project.id)"
          :key="project.key"
          class="oneOption"
        />
      </div>
      <div>
        <Option
          :title="voting.title"
          :editAction="voting.editAction"
          :newAction="voting.newAction"
          v-on:change="resetAnother(voting.id)"
          :key="voting.key"
          class="oneOption"
        />
        <Option
          :title="votingType.title"
          :editAction="votingType.editAction"
          :newAction="votingType.newAction"
          v-on:change="resetAnother(votingType.id)"
          :key="votingType.key"
          class="oneOption"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import Option from "../components/admin/Option.vue";

export default {
  name: "adminScreen",
  components: { Option },
  data() {
    return {
      rating: 4.5,
      title: "Panel administratora",
      hidden: true,
      group: {
        id: 0,
        title: this.getString("admin", "groups"),
        newAction: "groupNew",
        editAction: "groupsEditList",
        // deleteAction: "groupNew",
        key: 0,
      },
      project: {
        id: 1,
        title: this.getString("admin", "projects"),
        newAction: "projectNew",
        editAction: "projectsEditList",
        // deleteAction: "projectNew",
        key: 2,
      },
      voting: {
        id:2,
        title: this.getString("admin", "votings"),
        newAction: "votingNew",
        editAction: "votingsEditList",
        // deleteAction: "votingNew",
        key: 4,
      },
      votingType: {
        id: 3,
        title: this.getString("admin", "votingTypes"),
        newAction: "votingTypeNew",
        editAction: "votingTypeEditList",
        // deleteAction: "votingTypeNew",
        key: 6,
      },
    };
  },
  methods: {
    getString,
    resetAnother(id){
      if(id != 0) this.group.key = this.group.key == 0 ? 1 : 0
      if(id != 1) this.project.key = this.project.key == 2 ? 3 : 2
      if(id != 2) this.voting.key = this.voting.key == 4 ? 5 : 4
      if(id != 3) this.votingType.key = this.votingType.key == 6 ? 7 : 6
    }
  },
  created() {
    document.title = this.getString("admin", "title");
    var role = window.localStorage.getItem("username");
      if(role != "admin"){
        this.$router.push({name:"home", })
      }
  },
};
</script>

<style scoped>
.areaAdmin {
  margin: 30px;
  background-color: none;
  border-radius: 20px;
  padding-bottom: 50px;
  margin-bottom: 100px;
}
.titleAdmin {
  display: flex;
  font-size: 2rem;
  font-family: "Petrona";
  justify-content: center;
  /* margin: 20px auto 10px auto; */
  /* padding-bottom: 30px; */
  padding: 10px;
  /* padding-top: 50px; */
}
.oneOption {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
  border-radius: 200px;
  /* height: 200px; */
  border: outset;
  margin: 20px;
  font-size: 1.5rem;
  color: black;
}
.options {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-top: 50px;
  justify-content: center;
  align-items: center;
}
</style>
