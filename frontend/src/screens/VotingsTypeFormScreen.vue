<template>
<div class="container">
  <div class="row" >
    <div class="d-none d-sm-block col-md-2 col-lg-3" />
    <div class="col-sm-12 col-md-8 col-lg-6  d-flex justify-content-center flex-column">

    <div id="backgroundGroupForm" class="background d-flex justify-content-center ">

  
    <v-form
      v-model="valid"
      ref="newVotingTypeForm"
      id="newVotingTypeForm"
      class="d-flex justify-content-center p-3 groupForm"
      enctype="multipart/form-data"
    >
    
      <v-container>
        <div class="groupName">{{ getString("votingTypeForm", "title") }}</div>
       
        <v-text-field class="p-2 m-3"
        dense
            v-model="name.value"
            :rules="name.rule"
            :label="name.label"
            required
          ></v-text-field>
         
          <v-text-field class="p-2 m-3"
            v-model="desc.value"
            :rules="desc.rule"
            :label="desc.label"
            required
          ></v-text-field>
      
        <div class="d-flex justify-content-end p-4 buttons">
          <v-btn class="mr-4 p-2" @click="submit">
            {{ getString("votingTypeForm", "submit") }}
          </v-btn>
          <v-btn @click="clear">
            {{ getString("votingTypeForm", "clearData") }}
          </v-btn>
        </div>
      </v-container>
      
    </v-form>
    </div>
     <div class="d-none d-sm-block col-md-2 col-lg-3"/>
  </div>
    </div>
      
</div>

</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService } from "@/common/api.service.js";


export default {
  name: "votingTypeScreen",
  components: {},
  data() {
    return {
      valid: false,
      name:
        {
          label: getString("votingTypeForm", "nameLabel"),
          rule: [(v) => !!v || getString("votingTypeForm", "nameError")],
          value: "",
        },
        desc: {
          label: getString("votingTypeForm", "descLabel"),
          rule: [(v) => !!v || getString("votingTypeForm", "descError")],
          value: "",
        },
    };
  },
  methods: {
    getString,
    getColor,
    selectImage(){
      this.photo.value = this.$refs.file.files.item(0);
    },
    clear() {
      this.name.value = "";
      this.desc.value = "";
      this.reset();
    },
    reset() {
      this.$refs.newVotingTypeForm.reset();
    },
    validate() {
      this.$refs.newVotingTypeForm.validate();
    },

    async submit() {
      this.validate();
     
      if (this.valid) {

      await apiService("/api/voting_type/", "POST", {
            name: this.name.value,
            description: this.desc.value,
          }).then(data => {
              console.log(data)
          })
      }
    },
  },
  created(){
    document.title = this.getString("votingForm", "title")
  }
};
</script>

<style scoped>
.groupForm {
  border:solid;
  background-color: white;
  vertical-align: middle;
  margin: 20px;
  width: 90%;
}
.area {
  border: solid;
  margin: 30px;
  border-radius: 20px;
  padding-bottom: 50px;
}
.background{
  width: 100%;
  background-color: #C0CFE6;
  margin-top: 150px;
  /* position: relative; */

}
.groupName {
  font-size: 2rem;
  padding-bottom: 2rem;
  padding-top: 1.5rem;
  font-family: "playfair display";
  text-align: center;
}
.formButtons {
  margin-top: 20px;
}

@media only screen and (max-width: 758px){
  .background{

  margin-top: 10px;
  /* position: relative; */

}
.buttons{
  flex-direction: column;
}
button{
  width: 100%;
  margin-top: 20px;
 
}
.v-btn.v-size--default{
 font-size: 0.7rem
}
}
</style>
