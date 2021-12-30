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
            ref="registerProjectForm"
            id="registerProjectForm"
            class="d-flex justify-content-center p-3 projectForm"
            enctype="multipart/form-data"
          >
            <v-container>
              <div class="projectName">
                {{ getString("projectRegistration", "title") }}
              </div>

              <v-text-field
                class="p-2 m-3"
                dense
                v-model="name.value"
                :rules="name.rule"
                :label="name.label"
                required
              ></v-text-field>
              <v-text-field
                class="p-2 m-3"
                v-model="price.value"
                :rules="price.rule"
                :label="price.label"
                required
              ></v-text-field>
              <v-text-field
                class="p-2 m-3"
                v-model="desc.value"
                :rules="desc.rule"
                :label="desc.label"
                required
              ></v-text-field>
              <div class="md-layout-item p-2 m-3">
                <md-field>
                  <label for="group">{{ group.label }}</label>
                  <md-select v-model="group.value">
                    <md-option
                      v-for="(option, index) in group.items"
                      :key="index"
                      :value="option"
                      class="group"
                      >{{ option }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item p-2 m-3">
                <md-field>
                  <label for="voting">{{ voting.label }}</label>
                  <md-select v-model="voting.value">
                    <md-option
                      v-for="(option, index) in voting.items"
                      :key="index"
                      :value="option"
                      class="voting"
                      >{{ option }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <v-menu
                v-model="menu2"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
                class="p-2 m-3"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="endDate.value"
                    :label="endDate.label"
                    :rules="endDate.rule"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  :first-day-of-week="0"
                  :locale="lang"
                  v-model="endDate.value"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>
              <v-file-input
                class="p-2 m-3"
                :label="photo.label"
                v-model="selectedFile"
                append-icon="mdi-camera"
                prepend-icon=""
              ></v-file-input>
              <div class="d-flex justify-content-end p-4 buttons">
                <v-btn class="mr-4 p-2" @click="submit">
                  {{ getString("projectRegistration", "submitProject") }}
                </v-btn>
                <v-btn @click="clear">
                  {{ getString("projectRegistration", "clearData") }}
                </v-btn>
              </div>
            </v-container>
          </v-form>
        </div>
        <div class="d-none d-sm-block col-md-2 col-lg-3" />
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService, imageUpload } from "@/common/api.service.js";

export default {
  name: "ProjectRegistrationScreen",
  components: {},
  data() {
    return {
      valid: false,
      menu2: false,
      name: {
        label: getString("projectRegistration", "projectName"),
        rule: [
          (v) => !!v || getString("projectRegistration", "projectNameError"),
        ],
        value: "",
      },
      price: {
        label: getString("projectRegistration", "projectPrice"),
        rule: [
          (v) => !!v || getString("projectRegistration", "projectPriceError"),
        ],
        value: "",
      },
      desc: {
        label: getString("projectRegistration", "projectDescription"),
        rule: [
          (v) =>
            !!v || getString("projectRegistration", "projectDescriptionError"),
        ],
        value: "",
      },
      group: {
        label: getString("projectRegistration", "projectGroup"),
        rule: [
          (v) => !!v || getString("projectRegistration", "projectGroupError"),
        ],
        items: ["Foo", "Bar", "Fizz", "Buzz"],
        value: "",
      },
      voting: {
        label: getString("projectRegistration", "projectVoting"),
        rule: [
          (v) => !!v || getString("projectRegistration", "projectVotingError"),
        ],
        items: ["Foo", "Bar", "Fizz", "Buzz"],
        value: "",
      },
      endDate: {
        label: getString("votingForm", "endDateLabel"),
        rule: [(v) => !!v || getString("votingForm", "endDateError")],
        value: "",
      },
      photo: {
        label: getString("projectRegistration", "projectPhoto"),
        rule: [],
        value: {},
      },

      selectedFile: null,
    };
  },
  methods: {
    getString,
    getColor,
    selectImage() {
      this.photo.value = this.$refs.file.files.item(0);
    },
    clear() {
      this.name.value = "";
      this.price.value = "";
      this.desc.value = "";
      this.group.value = "";
      this.voting.value = "";
      this.image = "";
      this.reset();
    },
    reset() {
      this.$refs.registerProjectForm.reset();
    },
    validate() {
      this.$refs.registerProjectForm.validate();
    },
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    async submit() {
      this.validate();
      if (this.valid) {
        let formData = new FormData();
        formData.append("image", this.selectedFile);

        var photoId;

        await imageUpload(formData).then((data) => {(photoId = data.data.id), console.log(photoId);});

        await apiService("/api/projects/", "POST", {
          name: this.name.value,
          price: this.price.value,
          description: this.desc.value,
          group: this.group.value,
          voting: this.voting.value,
          image: photoId,
        }).then((data) => {
          this.$router.push({
            name: "project",
            params: { id: data.id },
          });
        });
      }
    },
  },
  created() {
    document.title = this.getString("projectRegistration", "pageTitle");
  },
};
</script>

<style scoped>
.projectForm {
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
.projectName {
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
