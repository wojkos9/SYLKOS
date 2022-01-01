<template>
  <div class="container">
    <div class="row area">
      <div class="aboutGroup">
        <div>
          <div class="groupTitle">{{ project.name }}</div>
        </div>

        <div class="desc">
          <div v-if="project.description.length > 200">
            <span v-if="showMore2">{{ project.description }} </span>
            <span v-else> {{ project.description.slice(0, 200) }}...</span>
            <div v-if="!showMore2" class="paddingTop-m">
              <v-btn x-small color="primary" dark @click="showMore2 = true">
                {{ $t("expand") }}
              </v-btn>
            </div>
            <div v-else class="paddingTop-m">
              <v-btn
                x-small
                color="primary"
                dark
                v-if="showMore2"
                @click="showMore2 = false"
              >
                {{ $t("unexpand") }}
              </v-btn>
            </div>
          </div>
          <div v-else>
            {{ project.description }}
          </div>  
        </div> 
        <div class="price desc">{{ $t("price") }}: {{ project.budget }} zł</div>
      </div>
      <div class="col center">
        <div class="center">
          <div v-if="project.images.length > 0">
            <img :src="`/media/${project.images[0].image}`" class="image" />
          </div>
          <ProjectWindow :project="project" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProjectWindow from "@/components/project/ProjectWindow.vue";

export default {
  name: "project",
  props: ["project"],
  data() {
    return {
      showMore2: false,
    };
  },
  methods: {},
  components: { ProjectWindow },
};
</script>

<style scoped>
.aboutGroup {
  width: 60%;
  margin-left: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.container{
  max-width: 90%;
}

::v-deep input::-webkit-outer-spin-button,
::v-deep input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.area {
  background-color: var(--v-background-lighten2);
  border: solid 1px black;
  margin-bottom: 30px;
  margin-top: 10px;
  padding: 10px;
}

.groupTitle {
  font-weight: 700;
  font-size: 1.5rem;
  margin-bottom: 10px;
  margin-top: 30px;
  text-align: center;
}

.desc {
  font-size: 1rem;
  font-weight: 400;
  margin-bottom: 10px;
  text-align: justify;
}

.center img {
  height: calc(30vh - 30px);
  width: auto;
  max-height: 150px;
  object-fit: contain;
  margin: 0 auto;
}
@media only screen and (max-width: 1200px) {
  .image {
    height: 300px;
    margin-bottom: 20px;
    width: 300px;
  }
  .center {
    float: none;
    margin: 0 auto;
    width: auto;
  }
  .desc {
    font-size: 0.875rem;
  }
}

@media only screen and (max-width: 1000px) {
  .aboutGroup {
    margin: 0 auto;
    padding: 10px 20px;
  }
  .groupTitle {
    margin: 20px auto;
  }
}

@media only screen and (max-width: 800px) {
  .area {
    margin: 0 auto 50px auto;
  }

  .aboutGroup {
    max-width: 700px;
    padding: 10px;
    width: 90%;
    margin: 10px auto;
  }

  .desc {
    margin-top: 0;
  }

  .center {
    margin-bottom: 20px;
  }
}
</style>
