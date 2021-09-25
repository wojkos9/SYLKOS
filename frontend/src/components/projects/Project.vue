<template>
  <div class="container">
    <div class="row area">
      <div class="col-lg-12 col-xl-9">
        <div>
          <div class="projectTitle">{{ project.name }}</div>
          <div class="desc">
            {{ project.description }}
          </div>
          <div class="price desc">
            {{ getString("projects", "price") }}: {{ project.budget }} zł
          </div>
        </div>
      </div>
      <div class="col center">
        <div class="center">
         <div v-if="project.images.length > 0">
              <img  :src="`/media/${project.images[0].image}`" class="image" />
          </div>
           <router-link :to="{ name: 'project', params:{id:project.id}}"><div :style="button">{{ getString('userPanel', 'details') }}</div></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "project",
  props: ["project"],
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
        padding: "3px",
        fontWeight: "500",
      };
    },
  },
  components: {},
};
</script>

<style scoped>
.area {
  padding: 10px;
  background-color: white;
  border: solid 1px black;
  margin-top: 10px;
  margin-bottom: 30px;
}

.projectTitle {
  font-weight: 700;
  font-size: 24px;
  margin-bottom: 40px;
  margin-top: 20px;
  text-align: center;
}

.desc {
  font-size: 1rem;
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
    float: none;
    margin: 0 auto;
    width: auto;
  }
  .desc {
    font-size: 0.875rem;
  }
  .title {
    font-size: 1.125rem;
  }
  .myButton {
    width: 300px;
  }
}
</style>
