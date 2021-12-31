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
          <div class="desc">{{ group.description.slice(0,100) }}</div>
        </div>
      </div>
    </div> 
  </div>
</template>

<script>

export default {
  name: "groups",
  props: ["groups"],
  data() {
    return {
      title: this.$t("myGroups"),
    };
  },
  methods: {
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
.titleIn{
  text-align: center;
  margin: 0 auto;
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

.content img {
  height: calc(30vh - 30px);
  width: auto;
  max-height: 150px;
  object-fit: contain;
  margin: 0 auto;
  /* width: 100%; */
}

.content{
  display: flex; 
  justify-content: center;
  flex-direction: row-reverse;
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
