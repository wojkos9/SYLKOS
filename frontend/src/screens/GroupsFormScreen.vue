<template>
<div class="container">
  <div class="row" >
    <div class="d-none d-sm-block col-md-2 col-lg-3" />
    <div class="col-sm-12 col-md-8 col-lg-6  d-flex justify-content-center flex-column">

    <div id="backgroundGroupForm" class="background d-flex justify-content-center ">

  
    <v-form
      v-model="valid"
      ref="newGroupForm"
      id="newGroupForm"
      class="d-flex justify-content-center p-3 groupForm"
      enctype="multipart/form-data"
    >
    
      <v-container>
        <div class="groupName">{{ getString("groupForm", "newGroup") }}</div>
       
        <v-text-field class="p-2 m-3"
        dense
            v-model="name.value"
            :rules="name.rule"
            :label="name.label"
            required
          ></v-text-field>
          <v-text-field class="p-2 m-3"
            v-model="subname.value"
            :rules="subname.rule"
            :label="subname.label"
            required
          ></v-text-field>
          <v-text-field class="p-2 m-3"
            v-model="desc.value"
            :rules="desc.rule"
            :label="desc.label"
            required
          ></v-text-field>
      <v-file-input
      class="p-2 m-3"
        :label="photo.label"
        v-model="selectedFiles"
        append-icon="mdi-camera"
        prepend-icon=""
        multiple
      ></v-file-input>
        <div class="d-flex justify-content-end p-4 buttons">
          <v-btn class="mr-4 p-2" @click="submit">
            {{ getString("groupForm", "submit") }}
          </v-btn>
          <v-btn @click="clear">
            {{ getString("groupForm", "clearData") }}
          </v-btn>
          <v-btn @click="proba">
            proba
          </v-btn>
        </div>
      </v-container>
      
    </v-form>
    </div>
     <div class="d-none d-sm-block col-md-2 col-lg-3"/>
  </div>
    </div>

    <DialogWithUser
      :title="getString('groupForm', 'success')"
      :desc="getString('groupForm', 'desc')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :object="group"
    />
      
</div>

</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService, imageUpload} from "@/common/api.service.js";
import DialogWithUser from '../components/UI/DialogWithUser.vue';

export default {
  name: "groupScreen",
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      newName: 'costam',
      group: '',
      name:
        {
          label: getString("groupForm", "groupNameLabel"),
          rule: [(v) => !!v || getString("groupForm", "groupNameError")],
          value: "",
        },
        subname: {
          label: getString("groupForm", "groupSubNameLabel"),
          rule: [],
          value: "",
        },
        desc: {
          label: getString("groupForm", "groupDescLabel"),
          rule: [(v) => !!v || getString("groupForm", "groupDescError")],
          value: "",
        },
  
      photo: {
          label: getString("groupForm", "groupPhotoLabel"),
          rule: [],
          value: {},
        },

        selectedFiles: [],
        dialog: false,
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
      this.subname.value = "";
      this.desc.value = "";
      this.members = [];
      this.image = "";
      this.reset();
    },
    reset() {
      this.$refs.newGroupForm.reset();
    },
    validate() {
      this.$refs.newGroupForm.validate();
    },
    onFileSelected(event){
      this.selectedFile = event.target.files[0]
    },
    async proba(){
      let formData = new FormData();
      for (var file of this.selectedFiles){
         formData.append("image", file);
      formData.append("costam", "costam")
      await imageUpload(formData).then((data) => {console.log("wynik proby " ,data)})
      }
     
    },
    async submit() {
      this.validate();
      console.log(this.photo.value)
      if (this.valid) {
        // let formData = new FormData();
        // formData.append("image", this.selectedFile);
        
      // var photoId = []
      


    

    await apiService("/api/groups/", "POST", {
          name: this.name.value,
          subname: this.subname.value,
          description: this.desc.value,
          members: [],
        }).then(async data => {
            console.log("komunikat: ", data)
            if(data != "wrong data"){
              this.dialog = true
              let groupId = data.id
                for (var file of this.selectedFiles){

              let formData = new FormData();
              formData.append("image", file);
              formData.append("product", groupId);
              formData.append("description", "opis zdjęcia");
              await imageUpload(formData).then((data) => {console.log("phtoId" ,data)})
                }
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
    document.title = this.getString("groupForm", "title")
  }
};
</script>

<style scoped>
.groupForm {
  border:solid;
  background-color: white;
  /* display: inline-block; */
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
