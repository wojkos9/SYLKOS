<template>
  <div class="container">
    <div class="row">
      <div class="d-none d-sm-block col-md-2 col-lg-3" />
      <div
        class="col-sm-12 col-md-8 col-lg-6  d-flex justify-content-center flex-column"
      >
        <div
          id="backgroundGroupForm"
          class="background d-flex justify-content-center "
        >
          <v-form
            v-model="valid"
            ref="newGroupForm"
            id="newGroupForm"
            class="d-flex justify-content-center p-3 groupForm"
            enctype="multipart/form-data"
          >
            <v-container>
              <div class="groupName">
                {{ getString("projectForm", "newProject") }}
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
                  {{ getString("groupForm", "submit") }}
                </v-btn>
                <v-btn @click="clear">
                  {{ getString("groupForm", "clearData") }}
                </v-btn>
              </div>
            </v-container>
          </v-form>
        </div>
        <div class="d-none d-sm-block col-md-2 col-lg-3" />
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
import { apiService, imageUpload } from "@/common/api.service.js";
import DialogWithUser from "../components/UI/DialogWithUser.vue";

export default {
  name: "projectFormScreen",
  components: { DialogWithUser },
  data() {
    return {
      lang: getString("language", "lang"),
      valid: false,
      selectedFiles: [],
      menu: false,
      modal: false,
      dialog: false,
      groups: [],
      votings: [],
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
      
    };
  },
  methods: {
    getString,
    getColor,
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
    async submit() {
      this.validate();
      if (this.valid) {
        console.log(this.project.group.value)
        await apiService("/api/projects/", "POST", {
          name: this.project.name.value,
          description: this.project.description.value,
          budget: this.project.budget.value,
          stage: this.project.stage.value,
          finish_date: this.project.finish_date.value + "T00:00:00Z",
          group: this.project.group.value.id,
          voting: 1,
        }).then(async (data) => {
          console.log("komunikat: ", data);
          if (data != "wrong data") {
            
            let projectId = data.id;

            this.project.name.value = data.name;
            this.project.description.value = data.description;
            this.project.budget.value = data.budget;
            this.project.stage.value = data.stage;
            this.project.finish_date.value = data.finish_date;
            this.project.group.value = this.project.group.value.name;
            this.project.voting.value = data.voting;

            console.log(this.selectedFiles)
            for (var file of this.selectedFiles) {
              console.log(file)
              let formData = new FormData();
              formData.append("image", file);
              formData.append("project", projectId);
              formData.append("description", "opis zdjęcia");
              await imageUpload(formData).then((data) => {
                this.project.images.value++;
                console.log("photoId", data);
              });
            }

            this.dialog = true;
          }
        });
      }
    },
    nextFunction() {
      this.dialog = false;
      this.$router.push({ name: "admin" });
    },
    backFunction() {
      this.dialog = false;
      // this.$router.push({name:"votingTypeNew"})
    },
  },
  created() {
    document.title = this.getString("groupForm", "title");
  },
   async beforeRouteEnter(to, from, next) {
    let userEndpoint = `api/user/`;
    let userData = await apiService(userEndpoint)
    
    return next((vm) => {
      console.log(userData.groups);
      vm.groups = userData.groups;
    });
  },
};
</script>

<style scoped>
.groupForm {
  border: solid;
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
.background {
  width: 100%;
  background-color: #c0cfe6;
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

@media only screen and (max-width: 758px) {
  .background {
    margin-top: 10px;
    /* position: relative; */
  }
  .buttons {
    flex-direction: column;
  }
  button {
    width: 100%;
    margin-top: 20px;
  }
  .v-btn.v-size--default {
    font-size: 0.7rem;
  }
}
</style>
