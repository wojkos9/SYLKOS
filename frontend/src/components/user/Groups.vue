<template>
  <div class="groups">
    <div class="title">{{ title }}</div>
    <div class="nextToGroupsScreen" style="z-index:-1">
      <div v-for="(group, index) in groups" :key="index">
        <div class="content">
          <div v-if="group.images.length > 0">
            <img :src="`/media/${group.images[0].image}`" class="image" />
          </div>
          <div class="titleIn">
            <div class="text">{{ group.name }}</div>
          </div>
          <div class="desc">{{ group.desc }}</div>
        </div>
      </div>
    </div> 
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "groups",
  props: ["groups"],
  data() {
    return {
      title: getString("userPanel", "myGroups"),
    };
  },
  methods: {
    getString,
    getColor,
  },
  components: {},
};
</script>

<style scoped>
.groups {
  margin-top: 50px;
}
.nextToGroupsScreen {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-self: center;
  justify-content: center;
  max-width: 100%;
}
.title {
  align-self: center;
  text-align: center;
  font-size: 26px;
  font-weight: lighter;
  margin-bottom: 15px;
}
.area {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  /* width: 50%; */
}

.image {
  align-self: center;
  border-radius: 5px;
  height: 160px;
  justify-self: center;
  object-fit: cover;
  width: 160px;
}

@media only screen and (max-width: 1200px) {
  .title {
    font-size: 22px;
  }
}

@media only screen and (max-width: 1000px) {
  .title {
    font-size: 20px;
  }
}
</style>
