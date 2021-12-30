<template>
  <div class="container">
    <div class="row">
      <div class="d-none d-sm-block col-md-2 col-lg-3" />
     
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
            <v-container  class="center-all">
              <div class="groupName">
                {{ getString("votingForm", "title") }}
              </div>
                <span class="calendar"> wybierz pierwszy i&nbsp;ostatni<br>
                 dzień głosowania</span>
                <v-date-picker
                  :first-day-of-week="0"
                  :locale="lang"
                  :min="nowDate"
                  v-model="dates"
                  range
                  color="accent"
                  
                ></v-date-picker>

               <v-text-field class="p-4 m-4"
                dense
                v-model="voting.name.value"
                :rules="voting.name.rule"
                :label="voting.name.label"
                required
              ></v-text-field>
         

              <v-combobox
                v-model="voting.votingType.value"
                :items="votingTypes"
                :rules="voting.votingType.rule"
                :label="voting.votingType.label"
                prepend-inner-icon=	'$dropdown'
                item-text="name"
                append-icon=''
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
    <DialogWithUser
      :title="getString('votingForm', 'success')"
      :desc="getString('votingForm', 'desc')"
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
import DialogWithUser from "../components/UI/DialogWithUser.vue";

export default {
  name: "groupScreen",
  components: { DialogWithUser },
  props: ["groupId"],
  data() {
    return {
      valid: false,
      lang: getString("language", "lang"),
      dialog: false,
      dates: [new Date().toISOString().slice(0, 10), new Date(new Date().getTime()+(5*24*60*60*1000)).toISOString().slice(0, 10)],
      voting: {

        name:{
          label: getString("votingForm", "nameLabel"),
          rule: [(v) => !!v || getString("votingForm", "votingNameError")],
          value: ''
        },

        votingType: {
          label: getString("votingForm", "votingTypeLabel"),
          rule: [(v) => !!v || getString("votingForm", "votingTypeError")],
          value: "",
        },
        
        startDate:{
          label: getString("votingForm", "startDateLabel"),
          value: ''
        },
        endDate:{
          label: getString("votingForm", "endDateLabel"),
          value:''
        },
      },
      nowDate: new Date().toISOString().slice(0, 10),
      check: false,
      votingTypes: {},
    };
  },
  methods: {
    getString,
    getColor,
    clear() {
      this.votingType.value = "";
      this.dates = [];
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
        if (this.groupId != null)
          await apiService("/api/voting/", "POST", {
            name: this.voting.name.value,
            start_date: this.dates[0] + "T00:00:00Z",
            end_date: this.dates[1] + "T00:00:00Z",
            voting_type: this.voting.votingType.value.name,
            group: this.groupId,
          }).then((data) => {
            if (data == "success") this.check = true;
            if (data != "wrong data") {
              this.voting.votingType.value = data.voting_type;
              this.voting.startDate.value = data.start_date.slice(0,10);
              this.voting.endDate.value = data.end_date.slice(0,10);
              this.voting.name.value = data.name;
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
    nextFunction() {
      this.dialog = false;
      this.$router.push({ name: "admin" });
    },
    backFunction() {
      this.dialog = false;
    },
  },
  created() {
    document.title = this.getString("votingForm", "title");
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `api/voting_type/`;
    let types = [];
    while (endpoint) {
      await apiService(endpoint).then((data) => {
        for (let type of data.results) {
          types.push(type);
        }
        endpoint = data.next;
      });
    }

    return next((vm) => {
      vm.votingTypes = types;
    });
  },
};
</script>

<style scoped>

.container{
  margin-bottom: 100px;
  padding-top: 0;
}

.groupForm {
  border:solid;
  background-color: var(--v-background-lighten3);
  vertical-align: middle;
  margin: 20px;
  width: 90%;
}
.background {
  width: 100%;
  background-color: #c0cfe6;
  margin-top: 50px;
}
.center-all{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.calendar{
  margin: 0 10px 30px 10px;
  text-align: center;
  font-size: 20px;
  font-weight: 300;
}
.buttons{
  margin-top: 2rem;
}
.groupName {
  font-size: 2rem;
  padding-bottom: 0;
  padding-top: 0;
  text-align: center;
}
@media only screen and (max-width: 758px) {
  .background {
    margin-top: 10px;
  }
  .buttons {
    flex-direction: column;
    margin-bottom: 50px;
  }

  
    .v-btn{
      width: 200px;
      margin-bottom: 20px;
    }


}

@media only screen and (max-width: 400px) {
  .groupForm{
    width: 100%;
    margin: 0;
    padding: 0 !important;
    border: none;
}
.container{ padding-top: 0;
}
.groupName{
  padding: 20px;
  margin: 20px 0 10px 0;
}
}
</style>
