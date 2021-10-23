<template>
<div class="container">
  <div class="row" >
    <div class="d-none d-sm-block col-md-2 col-lg-3" />
    <div class="col-sm-12 col-md-8 col-lg-6  d-flex justify-content-center flex-column">

    <div id="backgroundGroupForm" class="background d-flex justify-content-center ">

     
    <v-form
      v-model="valid"
      ref="votingTypeEdit"
      id="votingTypeEdit"
      class="d-flex justify-content-center p-3 groupForm"
      enctype="multipart/form-data"
    >
    
      <v-container>
        <div class="groupName">{{ getString("votingTypeEditForm", "title") }} <br> {{votingType.name.value}}</div>
     
        
          <v-text-field class="p-2 m-3"
            v-model="votingType.description.value"
            :rules="votingType.description.rule"
            :label="votingType.description.label"
            required
          ></v-text-field>
      
        <div class="d-flex justify-content-end p-4 buttons">
          <v-btn class="mr-4 p-2" @click="submit">
            {{ getString("votingTypeEditForm", "submit") }}
          </v-btn>
          <v-btn @click="clear">
            {{ getString("votingTypeEditForm", "cancel") }}
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
      :object="votingType"
    />
      
</div>

</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService} from "@/common/api.service.js";
import DialogWithUser from '../../components/UI/DialogWithUser.vue';

export default {
  name: "votingEditFormScreen",
  props: ["nameId",],
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      dialog: false,
      oldVotingType: [],
      votingType: {
         name:{
           label: getString("votingTypeForm", "votingName"),
           rule: [(v) => !!v || getString("votingTypeForm", "nameError")],
           value: '',
         },
        description:{
          label: getString("votingTypeForm", "votingDesc"),
          rule: [(v) => !!v || getString("votingTypeForm", "descError")],
          value: '',
        },
      },
    };
  },
  methods: {
    getString,
    getColor,
    clear() {
      this.votingType.name.value = this.oldVotingType.name;
      this.votingType.description.value = this.oldVotingType.description;
    },
    reset() {
      this.$refs.votingTypeEdit.reset();
    },
    validate() {
      this.$refs.votingTypeEdit.validate();
    },
    cancel(){
        this.$router.push({name: 'votingsEditList'})
    },
    async submit() {
      this.validate();
      if (this.valid) {

    await apiService(`/api/voting_type/${this.nameId}/`, "PUT", {
          name: this.votingType.name.value,
          description: this.votingType.description.value,
        }).then(async data => {
            console.log("komunikat: ", data)
            if(data != "wrong data"){
              this.dialog = true
              this.votingType.name.value = data.name
              this.votingType.description.value = data.description
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
    }
    
  },
  created(){
    document.title = this.getString("votingTypeEditForm", "title")
  },
  async beforeRouteEnter(to, from, next){
        if(to.params.nameId !== undefined){
            let endpoint = `api/voting_type/${to.params.nameId}/`
            let data = await apiService(endpoint)

            return next(vm => {
              vm.oldVotingType = data;
              vm.votingType.name.value = data.name
              vm.votingType.description.value = data.description
  
        });
        }else{
            return next()
        }
       
    },
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
