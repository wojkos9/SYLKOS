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
              <div class="projectName">
                {{ $t("projectForm.newProject") }}
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
                  :min="nowDate"
                  v-model="project.finish_date.value"
                  @input="menu = false"
                ></v-date-picker>
              </v-menu>

              <!-- <v-combobox
                class="p-2 m-3"
                v-model="project.group.value"
                :items="groups"
                :rules="project.group.rule"
                :label="project.group.label"
                item-text="name"
              ></v-combobox> -->

              <!-- <v-combobox
               class="p-2 m-3"
                v-model="project.voting.value"
                :items="votings"
               
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
                  {{ $t("projectForm.submit") }}
                </v-btn>
                <v-btn @click="clear">
                  {{ $t("projectForm.clearData") }}
                </v-btn>
              </div>
            </v-container>
          </v-form>
        </div>
        <div class="d-none d-sm-block col-md-2 col-lg-3" />
      </div>
    </div>

    <DialogWithUser
      :title="$t('projectForm.success')"
      :desc="$t('projectForm.desc')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :object="project"
    />
  </div>
</template>

<script>
import { apiService, imageUpload } from "@/common/api.service.js";
import DialogWithUser from "../components/UI/DialogWithUser.vue";

export default {
  name: "projectFormScreen",
  components: { DialogWithUser },
  props: ["groupId", "votingId"],
  data() {
    return {
      lang: this.$t("language.lang"),
      valid: false,
      selectedFiles: [],
      menu: false,
      modal: false,
      dialog: false,
      groups: [],
      votings: [],
      nowDate: new Date().toISOString().slice(0, 10),
      myComment: {},
      project: {
        name: {
          label: this.$t("projectForm.projectNameLabel"),
          rule: [(v) => !!v || this.$t("projectForm.projectNameError")],
          value: "",
        },
        description: {
          label: this.$t("projectForm.projectDescLabel"),
          rule: [(v) => !!v || this.$t("projectForm.projectDescError")],
          value: "",
        },
        budget: {
          label: this.$t("projectForm.projectBudgetLabel"),
          rule: [(v) => !!v || this.$t("projectForm.projectBudgetError")],
          value: 0,
        },
        stage: {
          label: this.$t("projectForm.projectStageLabel"),
          rule: [(v) => !!v || this.$t("projectForm.projectStageError")],
          value: "",
        },
        finish_date: {
          label: this.$t("projectForm.projectFinishLabel"),
          rule: [(v) => !!v || this.$t("projectForm.projectFinishError")],
          value: "",
        },
        group: {
          label: this.$t("projectForm.projectGroupLabel"),
          rule: [(v) => !!v || this.$t("projectForm.projectGroupError")],
          value: "",
        },
        voting: {
          label: this.$t("projectForm.projectVotingLabel"),
          rule: [],
          value: "",
        },
        images: {
          label: this.$t("projectForm.projectPhotoLabel"),
          rule: [],
          value: 0,
        },
      },
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
    async submit() {
      this.validate();
      if (this.valid) {
        await apiService("/api/projects/", "POST", {
          name: this.project.name.value,
          description: this.project.description.value,
          budget: this.project.budget.value,
          stage: "stage",
          finish_date: this.project.finish_date.value + "T00:00:00Z",
          group: this.groupId,
          voting: this.votingId,
          votes: 0,
        }).then(async (data) => {
          if (data != "wrong data") {
            let projectId = data.id;

            this.project.name.value = data.name;
            this.project.description.value = data.description;
            this.project.budget.value = data.budget;
            this.project.stage.value = data.stage;
            this.project.finish_date.value = data.finish_date.slice(0,10);
            this.project.group.value = this.project.group.value.name;
            this.project.voting.value = this.project.voting.value.name;
            this.project.voting.label = this.$t('projectForm.pictures');

            for (var file of this.selectedFiles) {
              let formData = new FormData();
              formData.append("image", file);
              formData.append("project", projectId);
              formData.append("description", "opis zdjęcia");
              await imageUpload(formData).then(() => {
                this.project.images.value++;
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
    },
  },
  created() {
    document.title = this.$t("groupForm.title");
  },
  async beforeRouteEnter(to, from, next) {
    let userEndpoint = `api/user/`;
    let userData = await apiService(userEndpoint);


    let votingsEndpoint = `api/voting/`;
    let votings = [];
    while (votingsEndpoint) {
      await apiService(votingsEndpoint).then((data) => {
        for (let voting of data.results) {
          votings.push(voting);
        }
        votingsEndpoint = data.next;
      });
    }

    return next((vm) => {
      vm.groups = userData.groups;
      vm.votings = votings
    });
  },
};
</script>

<style scoped>
.v-input__control {
  padding-right: 20px;
}

.groupForm {
  border: solid;
  background-color: var(--v-background-lighten3);
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
.projectName {
  font-size: 2rem;
  padding-bottom: 2rem;
  padding-top: 1.5rem;
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
