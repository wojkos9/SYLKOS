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
        <div class="groupName">{{ $t( "votingTypetitle") }}</div>
       
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
            {{ this.this.$t("submit") }}
          </v-btn>
          <v-btn @click="clear">
            {{ $t("votingTypesubmit") }}
          </v-btn>
        </div>
      </v-container>
      
    </v-form>
    </div>
     <div class="d-none d-sm-block col-md-2 col-lg-3"/>
  </div>

  <DialogWithUser 
  :title="$t('success')"
  :desc="$t('desc')"
  :nextAction="nextFunction"
  :backAction="backFunction"
  :dialog="dialog"
  :object="votingType" />
    </div>
      
</div>

</template>

<script>
import { apiService } from "@/common/api.service.js";
import DialogWithUser from '../components/UI/DialogWithUser.vue';


export default {
  name: "votingTypeScreen",
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      dialog: false,
      votingType: {
        name:{
          label: this.this.$t("name"),
          value: '',
        },
        description:{
          label: this.this.$t("desc"),
          value: '',
        },
      },
      name:
        {
          label: this.this.$t("votingTypenameLabel"),
          rule: [(v) => !!v || this.this.$t("votingTypenameError")],
          value: "",
        },
        desc: {
          label: this.this.$t("desc"),
          rule: [(v) => !!v || this.this.$t("votingTypedescError")],
          value: "",
        },
    };
  },
  methods: {
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
              if(data != "wrong data"){
              this.votingType.name.value = data.name;
              this.votingType.description.value = data.description;
              this.dialog = true
            }
          })
      }
    },
    nextFunction(){
      this.dialog = false
      this.$router.push({name:"admin"})
    },
    backFunction(){
      this.dialog = false
      // this.$router.push({name:"votingTypeNew"})
    }
  },
  created(){
    document.title = this.this.this.$t("votingForm", "title")
  }
};
</script>

<style scoped>
.groupForm {
  border:solid;
  background-color: var(--v-background-lighten3);
  vertical-align: middle;
  margin: 20px;
  width: 90%;
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
