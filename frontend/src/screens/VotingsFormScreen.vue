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
                {{ getString("votingForm", "title") }}
              </div>
              <!-- <v-app> -->
              <v-menu
                class="p-2 m-3"
                v-model="menu1"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="startDate.value"
                    :label="startDate.label"
                    :rules="startDate.rule"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>

                <v-date-picker
                  color="accent"
                  v-model="startDate.value"
                  @input="menu1 = false"
                  :first-day-of-week="0"
                  :locale="lang"
                ></v-date-picker>
              </v-menu>

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
                  color="accent"
                  :first-day-of-week="0"
                  :locale="lang"
                  v-model="endDate.value"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>

              <v-combobox
                v-model="votingType.value"
                :items="votingTypes"
                :rules="votingType.rule"
                :label="votingType.label"
                item-text="name"
              ></v-combobox>

              <div class="d-flex justify-content-end p-4 buttons">
                <v-dialog v-model="dialog" persistent max-width="500">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      class="mr-4 p-2"
                      @click="submit"
                      v-on="check && on"
                      v-bind="attrs"
                    >
                      {{ getString("votingForm", "submit") }}
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-text
                      style="text-align: center; padding: 20px; font-size: 1.5rem"
                    >
                      {{ getString("votingForm", "success") }}
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="green darken-1"
                        text
                        @click="dialog = false"
                      >
                        {{ getString("votingForm", "stay") }}
                      </v-btn>
                      <v-btn
                        color="green darken-1"
                        text
                        @click="dialog = false"
                      >
                        {{ getString("votingForm", "goToVoting") }}
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-btn @click="clear">
                  {{ getString("votingForm", "clearData") }}
                </v-btn>
              </div>
            </v-container>
          </v-form>
        </div>
        <div class="d-none d-sm-block col-md-2 col-lg-3" />
      </div>
    </div>
    <DialogWithUser
      :title="getString('votingTypeForm', 'success')"
      :desc="getString('votingTypeForm', 'desc')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :object="voting"
    />
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService } from "@/common/api.service.js";
import DialogWithUser from '../components/UI/DialogWithUser.vue';

export default {
  name: "groupScreen",
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      lang: getString("language", "lang"),
      dialog: false,
      voting: {
        startDate: {
          label: getString("votingForm", "startDateLabel"),
          value: "",
        },
        endDate: {
          label: getString("votingForm", "endDateLabel"),
          value: "",
        },
        votingType: {
          label: getString("votingForm", "votingTypeLabel"),
          value: "",
        },
      },
      menu1: false,
      modal: false,
      menu2: false,
      check: false,
      select: { name: "", description: "" },
      startDate: {
        label: getString("votingForm", "startDateLabel"),
        rule: [(v) => !!v || getString("votingForm", "startDateError")],
        value: "",
      },
      endDate: {
        label: getString("votingForm", "endDateLabel"),
        rule: [(v) => !!v || getString("votingForm", "endDateError")],
        value: "",
      },
      votingType: {
        label: getString("votingForm", "votingTypeLabel"),
        rule: [(v) => !!v || getString("votingForm", "votingTypeError")],
        value: "",
      },
      votingTypes2: ["nowy typ glosowania", "cosinnego"],
      votingTypes: {},
      votingTypesNames: [],
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
      this.startDate.value = "";
      this.endDate.value = "";
      this.votingType.value = "";
      this.reset();
    },
    reset() {
      this.$refs.newGroupForm.reset();
    },
    validate() {
      this.$refs.newGroupForm.validate();
    },
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    async submit() {
      this.validate();
      if (this.valid) {
        await apiService("/api/voting/", "POST", {
          start_date: this.startDate.value + "T00:00:00Z",
          end_date: this.endDate.value + "T00:00:00Z",

          voting_type: this.votingType.value.name,
        }).then((data) => {
          if (data == "success") this.check = true;
          console.log(data);
          if (data != "wrong data") {
            this.voting.startDate.value = data.start_date;
            this.voting.endDate.value = data.end_date;
            this.voting.votingType.value = data.voting_type;
            console.log(this.voting)
            this.dialog = true;
          }
        });
      }
    },
    async getTypes(endpoint) {
      await apiService(endpoint).then((data) => {
        return data;
      });
      return null;
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
  created() {
    document.title = this.getString("votingForm", "title");
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `api/voting_type/`;
    let types = [];
    while (endpoint) {
      await apiService(endpoint).then((data) => {
        console.log(data.results);
        for (let type of data.results) {
          types.push(type);
        }
        endpoint = data.next;
      });
    }

    return next((vm) => {
      console.log(types);

      vm.votingTypes = types;
    });
  },
};
</script>

<style scoped>
.groupForm {
  border: solid;
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
.background {
  width: 100%;
  background-color: #c0cfe6;
  margin-top: 150px;
}
.dates {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
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

@media only screen and (max-width: 758px) {
  .background {
    margin-top: 10px;
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
