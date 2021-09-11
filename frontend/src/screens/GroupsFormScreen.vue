<template>
  <div class="d-flex justify-content-center m-5">
    <div id="backgroundGroupForm" class="background">

  
    <v-form
      v-model="valid"
      ref="newGroupForm"
      id="newGroupForm"
      class="d-flex justify-content-center p-3 groupForm"
    >
    
      <v-container>
        <div class="groupName">{{ getString("groupForm", "newGroup") }}</div>
        <div v-for="(field, index) in fields" :key="index" class="p-2 m-3">
          <v-text-field
            v-model="field.value"
            :rules="field.rule"
            :label="field.label"
            required
          ></v-text-field>
        </div>
        <div class="d-flex justify-content-end p-4">
          <v-btn class="mr-4 p-2" @click="submit">
            {{ getString("groupForm", "submit") }}
          </v-btn>
          <v-btn @click="clear">
            {{ getString("groupForm", "clearData") }}
          </v-btn>
        </div>
      </v-container>
      
    </v-form>
  </div>
    </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService } from "@/common/api.service.js";

export default {
  name: "groupScreen",
  components: {},
  data() {
    return {
      valid: false,
      fields: [
        {
          label: getString("groupForm", "groupNameLabel"),
          rule: [(v) => !!v || getString("groupForm", "groupNameError")],
          value: "",
        },
        {
          label: getString("groupForm", "groupSubNameLabel"),
          rule: [],
          value: "",
        },
        {
          label: getString("groupForm", "groupDescLabel"),
          rule: [(v) => !!v || getString("groupForm", "groupDescError")],
          value: "",
        },
      ],
    };
  },
  methods: {
    getString,
    getColor,
    clear() {
      for(var field  of this.fields){
          field.value = ""
      }
      this.reset();
    },
    reset() {
      this.$refs.newGroupForm.reset();
    },
    validate() {
      this.$refs.newGroupForm.validate();
    },
    async submit() {
      this.validate();
      if (this.valid) {
        await apiService("/api/groups/", "POST", {
          name: this.fields[0].value,
          subname: this.fields[1].value,
          description: this.fields[2].value,
          members: [],
        }).then((data) => {
          console.log(data);
        });
        this.clear();
        this.reset();
      }
    },
    setPositions(){
      // var background = document.getElementById("backgroundGroupForm")
      // var form = document.getElementById("newGroupForm")
    }
  },
  created(){
    this.setPositions()
  }
};
</script>

<style scoped>
.groupForm {
  background-color: white;
  display: inline-block;
  vertical-align: middle;
  margin: 20px
}
.area {
  border: solid;
  margin: 30px;
  border-radius: 20px;
  padding-bottom: 50px;
}
.background{
  width: 55%;
  background-color: #C0CFE6;
  position: relative;

}
.groupName {
  font-size: 2rem;
  padding-bottom: 2rem;
  padding-top: 1.5rem;
}
.formButtons {
  margin-top: 20px;
}
</style>
