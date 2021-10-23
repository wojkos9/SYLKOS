<template>
<div class="container">
  <div class="row" >
    <div class="d-none d-sm-block col-md-2 col-lg-3" />
    <div class="col-sm-12 col-md-8 col-lg-6  d-flex justify-content-center flex-column">

    <div id="backgroundGroupForm" class="background d-flex justify-content-center ">

     
    <v-form
            v-model="valid"
            ref="editVotingForm"
            id="editVotingForm"
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
                    v-model="voting.startDate.value"
                    :label="voting.startDate.label"
                    :rules="voting.startDate.rule"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>

                <v-date-picker
                  color="accent"
                  v-model="voting.startDate.value"
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
                    v-model="voting.endDate.value"
                    :label="voting.endDate.label"
                    :rules="voting.endDate.rule"
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
                  v-model="voting.endDate.value"
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>

              <v-combobox
                v-model="voting.votingType.value"
                :items="votingTypes"
                :rules="voting.votingType.rule"
                :label="voting.votingType.label"
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
                      {{ getString("votingEditForm", "submit") }}
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
                  {{ getString("votingEditForm", "cancel") }}
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
      :object="voting"
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
  props: ["id",],
  components: {DialogWithUser},
  data() {
    return {
      valid: false,
      menu1: false,
      modal: false,
      menu2: false,
      check: false,
      select: { name: "", description: "" },
      newName: 'costam',
      groupId: '',
      votingTypes:{},
      oldVoting: [],
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
      dialog: false,
    };
  },
  methods: {
    getString,
    getColor,
    clear() {
     this.voting.startDate.value = this.oldVoting.startDate
      this.voting.endDate.value = this.oldVoting.endDate
      this.voting.votingType.value = this.oldVoting.votingType
    },
    reset() {
      this.$refs.editVotingForm.reset();
    },
    validate() {
      this.$refs.editVotingForm.validate();
    },
    cancel(){
        this.$router.push({name: 'votingsEditList'})
    },
    async submit() {
      this.validate();
      if (this.valid) {

    await apiService(`/api/voting/${this.votingId}/`, "PUT", {
          start_date: this.voting.startDate.value + "T00:00:00Z",
          end_date: this.voting.endDate.value + "T00:00:00Z",
          voting_type: this.voting.votingType.value,
        }).then(async data => {
            console.log("komunikat: ", data)
            if(data != "wrong data"){
              this.dialog = true
              this.voting.startDate.value = data.start_date.slice(0, data.start_date.indexOf("T00"))
              this.voting.endDate.value = data.end_date.slice(0, data.end_date.indexOf("T00"))
              this.voting.votingType.value = data.voting_type
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
    document.title = this.getString("votingEditForm", "title")
  },
  async beforeRouteEnter(to, from, next){
        if(to.params.id !== undefined){
            let endpoint = `api/voting/${to.params.id}/`
            let data = await apiService(endpoint)

            endpoint = `api/voting_type/`;
            let types = [];
            while (endpoint) {
              await apiService(endpoint).then((data2) => {
                console.log(data2.results);
                for (let type of data2.results) {
                  types.push(type);
                }
                endpoint = data.next;
              });
            }

            return next(vm => {
              console.log(data)
              vm.votingTypes = types;
              vm.oldVoting = data
              vm.votingId = data.id
              vm.voting.startDate.value = data.start_date.slice(0, data.start_date.indexOf("T00"))
              vm.voting.endDate.value = data.end_date.slice(0, data.end_date.indexOf("T00"))
              vm.voting.votingType.value = data.voting_type
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
