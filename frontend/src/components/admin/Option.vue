<template>

  <v-card >
        <div
      class="oneOption"
      style="position:relative"
      @click="
        hidden = !hidden;
        $emit('change');
      "
    >
      <div class="title">
        {{ title }}
      </div>

      <router-link
        :to="{
          name: newAction,
        }"
      >
        <v-card-text
          style=" position: absolute; top: 20px; left: 400px; width: 50px; "
        >
          <v-fab-transition>
            <v-btn v-show="!hidden" color="secondary" dark absolute top right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </router-link>
      <router-link
        :to="{
          name: editAction,
        }"
      >
        <v-card-text
          style=" position: absolute; top: 100px; left: 400px; width: 50px; "
        >
          <v-fab-transition>
            <v-btn v-show="!hidden" color="secondary" dark absolute top right fab>
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </router-link>
      <!-- <router-link
        :to="{
          name: deleteAction,
        }"
      >
        <v-card-text
          style=" position: absolute; top: 150px; left: 400px; width: 50px; "
        >
          <v-fab-transition>
            <v-btn v-show="!hidden" color="secondary" dark absolute top right fab>
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </router-link> -->
    </div>
  </v-card>

</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "adminScreen",
  components: {},
  props: ["title", "newAction", "deleteAction", "editAction"],
  data() {
    return {
      hidden: true,
    };
  },
  methods: {
    getString,
    getColor,
  },
  created() {
    document.title = this.getString("admin", "title");
  },
};
</script>

<style scoped>
.area {
  background-color: white;
  margin: 30px;
  border-radius: 20px;
  padding-bottom: 50px;
}
.title {
  display: flex;
  font-size: 2rem;
  justify-content: center;
  margin: 50px;
  /* padding-bottom: 30px;
  padding-top: 50px; */
}
.oneOption {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
  border-radius: 200px;
  height: 200px;
  border: outset;
  margin: 40px;
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

.oneOption:hover {
  cursor: pointer;
  background-color: #f2f6fa;
}
</style>
