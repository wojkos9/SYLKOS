<template>
  <v-card>
    <div
      class="oneOption"
      @click="optionChange()">
      <div class="title">
        {{ title }}
      </div>

      <!-- ADD NEW OBJECT -->
      <router-link :to="{ name: newAction }">  
        <v-card-text class="addAction">
          <v-fab-transition>
            <v-btn
              v-show="!hidden"
              color="accent"
              dark
              absolute
              top
              right
              fab
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </router-link> 
 
      <!-- EDIT OBJECT -->
      <router-link :to="{ name: editAction }">
        <v-card-text class="editAction">
          <v-fab-transition>
            <v-btn
              v-show="!hidden"
              color="accent"
              dark
              absolute
              top
              right
              fab
            >
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </router-link>
    </div>
  </v-card>
</template>

<script>

export default {
  name: "adminScreen",
  props: ["title", "newAction", "deleteAction", "editAction"],
  data() {
    return {
      hidden: true,
    };
  },
  methods: {
    optionChange(){
        this.hidden = !this.hidden;
        this.$emit('change');
    }
  },
};
</script>

<style scoped>
.title {
  display: flex;
  font-size: 2rem;
  justify-content: center;
  margin: 50px;
  text-align: center;
  font-family: "Petrona";

}
.oneOption {
  position: relative;
  background-color: var(--v-background);
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
  border-radius: 200px;
  height: 200px;
  border: outset;
  /* margin: 40px; */
  font-size: 1.5rem;
  /* color: black; */
}
.oneOption:hover {
  cursor: pointer;
  background-color:  var(--v-background-lighten3);
}
.addAction {
  position: absolute;
  top: 30px;
  left: 400px;
  width: 50px;
}

.editAction {
  position: absolute;
  top: 100px;
  left: 400px;
  width: 50px;
}

@media only screen and (max-width:600px) {
  .oneOption {
    overflow: hidden;;
    width: 250px;
    height: auto;
    border-radius: 20px;
    text-align: left;

  }
  .title{
    margin: 0
  }
.addAction, .editAction {
  display: none;
}

}
</style>
