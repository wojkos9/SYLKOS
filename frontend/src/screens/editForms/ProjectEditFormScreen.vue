<template>
<div class="container">
  <div class="row" >
    <div class="d-none d-sm-block col-md-2 col-lg-3" />
    <div class="col-sm-12 col-md-8 col-lg-6  d-flex justify-content-center flex-column">

    <div id="backgroundGroupForm" class="background d-flex justify-content-center ">

  
   <v-form
            v-model="valid"
            ref="editProjectForm"
            id="newGroupForm"
            class="d-flex justify-content-center p-3 groupForm"
            enctype="multipart/form-data"
          >
            <v-container>
              <div class="projectName">
                {{ getString("projectEditForm", "title") }}
              </div>

              <v-text-field
                class="p-2 m-3"
                dense
                v-model="project.name.value"
                :rules="project.name.rule"
                :label="project.name.label"
                required
              ></v-text-field>
              <v-text-field
                class="p-2 m-3"
                v-model="project.description.value"
                :rules="project.description.rule"
                :label="project.description.label"
                required
              ></v-text-field>
              <v-text-field
                class="p-2 m-3"
                v-model="project.budget.value"
                :rules="project.budget.rule"
                :label="project.budget.label"
                type="number"
                required
              ></v-text-field>
              <v-text-field
                class="p-2 m-3"
                v-model="project.stage.value"
                :rules="project.stage.rule"
                :label="project.stage.label"
               
                required
              ></v-text-field>

                <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
                class="p-2 m-3"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="project.finish_date.value"
                    :label="project.finish_date.label"
                    :rules="project.finish_date.rule"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  color="accent"
                  :first-day-of-week="0"
                  :locale="lang"
                  v-model="project.finish_date.value"
                  @input="menu = false"
                ></v-date-picker>
              </v-menu>

               <v-combobox
               class="p-2 m-3"
                v-model="project.group.value"
                :items="groups"
                :rules="project.group.rule"
                :label="project.group.label"
                item-text="name"
              ></v-combobox>

               <!-- <v-combobox
               class="p-2 m-3"
                v-model="project.voting.value"
                :items="votingTypes"
                :rules="project.voting.rule"
                :label="project.voting.label"
                item-text="name"
              ></v-combobox> -->

              <v-file-input
                class="p-2 m-3"
                :label="project.images.label"
                v-model="selectedFiles"
                append-icon="mdi-camera"
                prepend-icon=""
                multiple
              ></v-file-input>

              <div class="d-flex justify-content-end p-4 buttons">
                <v-btn class="mr-4 p-2" @click="submit">
                  {{ getString("projectEditForm", "submit") }}
                </v-btn>
                <v-btn @click="clear">
                  {{ getString("projectEditForm", "cancel") }}
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
      :object="project"
    />
      
</div>

</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService} from "@/common/api.service.js";
import DialogWithUser from '../../components/UI/DialogWithUser.vue';

export default {
  name: "projectEditFormScreen",
  props: ["id"],
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      projectId: '',
      oldProject: null,
      groups: [],
      project: {
        name: {
          label: getString("projectForm", "projectNameLabel"),
          rule: [(v) => !!v || getString("projectForm", "projectNameError")],
          value: "",
        },
        description: {
          label: getString("projectForm", "projectDescLabel"),
          rule: [(v) => !!v || getString("projectForm", "projectDescError")],
          value: "",
        },
        budget: {
          label: getString("projectForm", "projectBudgetLabel"),
          rule: [(v) => !!v || getString("projectForm", "projectBudgetError")],
          value: 0,
        },
        stage: {
          label: getString("projectForm", "projectStageLabel"),
          rule: [(v) => !!v || getString("projectForm", "projectStageError")],
          value: "",
        },
        finish_date: {
          label: getString("projectForm", "projectFinishLabel"),
          rule: [(v) => !!v || getString("projectForm", "projectFinishError")],
          value: "",
        },
        group: {
          label: getString("projectForm", "projectGroupLabel"),
          rule: [(v) => !!v || getString("projectForm", "projectGroupError")],
          value: "",
        },
        voting: {
          label: getString("projectForm", "projectVotingLabel"),
          rule: [],
          value: "",
        },
        images: {
          label: getString("projectForm", "projectPhotoLabel"),
          rule: [],
          value: 0,
        },
      },
        selectedFiles: [],
        dialog: false,
    };
  },
  methods: {
    getString,
    getColor,
    clear() {

      this.project.name.value = this.oldProject.name;
      this.project.name.value = this.oldProject.name
      this.project.description.value = this.oldProject.description
      this.project.budget.value = this.oldProject.budget
      this.project.stage.value = this.oldProject.stage
      this.project.finish_date.value = this.oldProject.finish_date
      this.project.group.value = this.oldProject.group
      this.project.voting.value = this.oldProject.voting
    },
    reset() {
      this.$refs.editProjectForm.reset();
    },
    validate() {
      this.$refs.editProjectForm.validate();
    },
    cancel(){
        this.$router.push({name: 'projectsEditList'})
    },
    async submit() {
      this.validate();
      if (this.valid) {

    await apiService(`/api/projects/${this.projectId}/`, "PUT", {
          name: this.project.name.value,
          description: this.project.description.value,
          budget: this.project.budget.value,
          stage: this.project.stage.value,
          finish_date: this.project.finish_date.value + "T00:00:00Z",
          group: this.project.group.value,
          voting: this.project.voting.value,
          // stage: this.group.members.value,
        }).then(async data => {
            console.log("komunikat: ", data)
            if(data != "wrong data"){ 
              this.dialog = true
              this.project.projectId = data.id
              this.project.name.value = data.name
              this.project.description.value = data.description
              this.project.budget.value = data.budget
              this.project.stage.value = data.stage
              this.project.finish_date.value = data.finish_date 
              this.project.group.value = data.group
              // this.project.images.value = this.oldProject.images
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
    document.title = this.getString("projectEditForm", "title")
  },
  async beforeRouteEnter(to, from, next){
        if(to.params.id !== undefined){
            let endpoint = `api/projects/${to.params.id}/`
            let data = await apiService(endpoint)

            let userEndpoint = `api/user/`;
            let userData = await apiService(userEndpoint)
    
            return next(vm => {
              vm.oldProject = data
              vm.projectId = data.id
              vm.project.name.value = data.name
              vm.project.description.value = data.description
              vm.project.budget.value = data.budget
              vm.project.stage.value = data.stage
              vm.project.finish_date.value = data.finish_date.slice(0, data.finish_date.indexOf("T00"))
              vm.project.group.value = data.group
              vm.project.voting.value = data.voting
              vm.groups = userData.groups
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
.projectName {
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
