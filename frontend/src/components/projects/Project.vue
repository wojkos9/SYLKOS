<template>
  <div class="container">
    <div class="row area">
      <div class="col-lg-12 col-xl-9">
        <div>
          <div class="projectTitle">{{ name }}</div>
          <div class="desc">
            {{ desc }}
          </div>
          <div class="membersNumber desc">
            {{ getString("groups", "membersNumber") }} {{ members }}
          </div>
        </div>
      </div>
      <div class="col center">
        <div class="center">
          <img :src="picture" class="image" />
          <router-link :to="{ name: 'project', params:{id:id}}"><div :style="button">{{ getString('userPanel', 'details') }}</div></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "group",
  props: ["id", "name", "desc", "members", "picture"],
  methods: {
    getString,
    getColor,
  },
  computed: {
    button() {
      return {
        backgroundColor: getColor("navbar"),
        width: "160px",
        marginTop: "5px",
        borderRadius: "5px",
        textAlign: "center",
        fontFamily: "Playfair Display",
        padding: "3px",
        fontWeight: "500",
      };
    },
  },
  components: {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");
.area {
  padding: 10px;
  background-color: white;
  border: solid 1px black;
  margin-top: 10px;
  margin-bottom: 30px;
  /* width: 70%; */
}

.projectTitle {
  font-weight: 700;
  font-size: 24px;
  margin-bottom: 40px;
  margin-top: 20px;
  font-family: "Playfair Display", serif;
  text-align: center;
}

.desc {
  font-family: "Playfair Display", serif;
  font-size: 16px;
  font-weight: 400;
  margin-bottom: 10px;
  text-align: justify;
}

.membersNumber {
  margin-top: 30px;
}

.myButton {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image {
  width: 160px;
  height: 160px;
  object-fit: cover;
  align-self: center;
  justify-self: center;
  border-radius: 5px;
}
.center {
  /* display: flex; */
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
}

@media only screen and (max-width: 1200px) {
  .image {
    width: 300px;
    height: 300px;
    margin-top: 50px;
    margin-bottom: 20px;
  }
  .center {
    /* width: 100% !important; */
    /* border: red 1px solid; */
    float: none;
    margin: 0 auto;
    width: auto;
  }
  .desc {
    font-size: 14px;
  }
  .title {
    font-size: 18px;
  }
  .myButton {
    width: 300px;
  }
}
</style>
