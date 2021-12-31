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
        <div class="groupName">{{ $t("groupsEditForm.title") }}</div>
        <v-text-field class="p-2 m-3"
        dense
            v-model="group.name.value"
            :rules="group.name.rule"
            :label="group.name.label"
            required
          ></v-text-field>
          <v-text-field class="p-2 m-3"
            v-model="group.subname.value"
            :rules="group.subname.rule"
            :label="group.subname.label"
            required
          ></v-text-field>
          <v-text-field class="p-2 m-3"
            v-model="group.desc.value"
            :rules="group.desc.rule"
            :label="group.desc.label"
            required
          ></v-text-field>
      <!-- <v-file-input
      class="p-2 m-3"
        :label="photo.label"
        v-model="selectedFiles"
        append-icon="mdi-camera"
        prepend-icon=""
        multiple
      ></v-file-input> -->
        <div class="d-flex justify-content-end p-4 buttons">
          <v-btn class="mr-4 p-2" @click="submit">
            {{ $t("groupsEditForm.submit") }}
          </v-btn>
          <v-btn @click="cancel">
            {{ $t("groupsEditForm.cancel") }}
          </v-btn>

        </div>
      </v-container>
      
    </v-form>
    </div>
     <div class="d-none d-sm-block col-md-2 col-lg-3"/>
  </div>
    </div>

    <DialogWithUser
      :title="$t('groupForm.success')"
      :desc="$t('groupForm.desc')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :object="group"
    />
      
</div>

</template>

<script>
import { apiService} from "@/common/api.service.js";
import DialogWithUser from '../../components/UI/DialogWithUser.vue';

export default {
  name: "groupScreen",
  props: ["id", "groupData"],
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      newName: 'costam',
      groupId: '',
      group: {
        name: {
          label: this.$t("groupForm.groupNameLabel"),
          rule: [(v) => !!v || this.$t("groupForm.groupNameError")],
          value: "",
        },
        subname: {
          label: this.$t("groupForm.groupSubNameLabel"),
          rule: [],
          value: "",
        },
        desc: {
          label: this.$t("groupForm.groupDescLabel"),
          rule: [(v) => !!v || this.$t("groupForm.groupDescError")],
          value: "",
        },
        pictures: {
          label: this.$t("groupForm.pictures"),
          rule: [],
          value: {},
          count: 0,
        },
        members: {
          value: 0,
        }
      },
        selectedFiles: [],
        dialog: false,
    };
  },
  methods: {
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
    cancel(){
        this.$router.push({name: 'groupsEditList'})
    },
    async submit() {
      this.validate();
      if (this.valid) {

    await apiService(`/api/groups/${this.groupId}/`, "PUT", {
          name: this.group.name.value,
          subname: this.group.subname.value,
          description: this.group.desc.value,
          members: this.group.members.value,
        }).then(async data => {
            if(data != "wrong data"){
              this.dialog = true
              this.group.name.value = data.name;
              this.group.subname.value = data.subname;
              this.group.desc.value = data.description;
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
    document.title = this.$t("groupForm.title")
  },
  async beforeRouteEnter(to, from, next){
        if(to.params.id !== undefined){
            let endpoint = `api/groups/${to.params.id}/`
            let data = await apiService(endpoint)
            return next(vm => {
              vm.groupId = data.id
              vm.group.name.value = data.name
              vm.group.subname.value = data.subname
              vm.group.desc.value = data.description
              vm.group.members.value = data.members

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
  background-color:  var(--v-background-lighten3);;
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
