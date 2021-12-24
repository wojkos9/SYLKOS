<template>
  <div class="area">
    <div class="groupName">{{ group.name }} - panel administratora</div>

    <details>
      <summary> lista uczestników </summary>
      <div v-for="(member, index) in group.members" :key="index">
        <div class="single-user">
          <div class="username">
            {{ member }}
          </div>
          <div v-show="user != member" class="user-remove">
            <v-btn fab color="teal" width="40px" height="40px" @click="removeUserFromGroup(member)">
              <v-icon dark>
                mdi-minus
              </v-icon>
            </v-btn>
          </div>
        </div>
      </div>
      <div class="findLast"></div>
    </details>

    <details>
      <summary> lista głosowań </summary>
      <div class="add-voting">
        <div>dodaj glosowanie</div>
       <router-link :to="{ name: newVotingLink }" class="customBtn"> 
        <v-btn fab color="teal" width="40px" height="40px">
          <v-icon dark>
            mdi-plus
          </v-icon>
        </v-btn>
     </router-link>
      </div>
      
      <div class="exist-votings">istniejące głosowania:</div>
      <div
        v-for="(voting, index) in votings"
        :key="index"
        class="single-voting"
      >
        {{ voting.name }}
        <div
          v-for="(project, index2) in voting.projects"
          :key="index2"
          class="single-project"
        >
          {{ project.name }}
        </div>
      </div>
      <div class="findLast"></div>
    </details>

    <details>
      <summary> klucze </summary>
      <div class="key-option" @click="generatePdfCodes">pobierz wszystkie</div>
      <div class="key-option" @click="dialogGenerateAccessCode = true">
        wygeneruj klucz
      </div>
      <div class="key-option" @click="printKeys">drukuj</div>
      <div class="key-option" @click="showActiveKeys = !showActiveKeys">
        lista aktywnych kluczy ({{ keys.length }})
      </div>
      <div v-show="showActiveKeys" class="all-keys">
        <div v-for="(key, index) in keys" :key="index" class="single-key">
          {{ key.value }}
        </div>
      </div>

      <div class="findLast"></div>
    </details>

    <v-dialog v-model="dialogGenerateAccessCode" width="600">
      <v-card>
        <v-card-title class="text-h4 p-2 d-flex justify-content-center">
          GENERATOR KODÓW DOSTĘPU
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <div>
            ilość kodów do wygenerowania
          </div>

          <v-form
            v-model="valid"
            ref="codeGenerator"
            :key="codeKey"
            style="margin-top: 30px"
          >
            <div
              style="padding-left: 20px;  margin: 5px; padding-right:20px; border: solid; border-radius: 10px"
            >
              <v-text-field
                style="width:100px; font-size: 36px"
                v-model="count"
                type="number"
                min="1"
                max="999"
                ref="code1"
                autofocus
              ></v-text-field>
            </div>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="clearDialog">
            {{ getString("groups", "generateCancel") }}
          </v-btn>
          <v-btn text @click="generateAccessCodes">
            {{ getString("groups", "generateConfirm") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <v-dialog v-model="dialogShowNewCodes" width="600">
      <v-card>
        <v-card-title class="text-h4 p-2 d-flex justify-content-center">
          GENERATOR KODÓW DOSTĘPU
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <div>
            wygenerowane kody:
          </div>
      
        </v-card-text>
          <div class="all-keys">
          <div v-for="(key, index) in newCodes" :key="index" class="single-key">
            {{ key }}
          </div>
        </div>
        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialogShowNewCodes=false">
            {{ getString("groups", "ok") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <v-dialog v-model="dialogRemoveUser" width="600">
      <v-card>
        <v-card-text class="text-h6  lighten-2 p-4 ">
          <div>
          czy na pewno chcesz usunąć użytkownika {{userToRemove}} z grupy?
          </div>
      
        </v-card-text>
        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialogRemoveUser=false">
          nie
          </v-btn>
           <v-btn text @click="removeUserConfirmed()">
          tak
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <div id="print-section">
      <div v-for="(key, index) in keys" :key="index" class="print-key">
        {{ key.value }}
      </div>
    </div>

    <VueHtml2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="true"
      :preview-modal="false"
      :paginate-elements-by-height="1400"
      filename="accessCodes"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a4"
      pdf-orientation="landscape"
      pdf-content-width="800px"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
        <div class="all-keys">
          <div v-for="(key, index) in keys" :key="index" class="single-key">
            {{ key.value }}
          </div>
        </div>
      </section>
    </VueHtml2pdf>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import VueHtml2pdf from "vue-html2pdf";
import { apiService } from "@/common/api.service.js";

export default {
  name: "groupScreen",
  components: {
    VueHtml2pdf,
  },
  props: {
    id: {
      required: true,
    },
    group2: {
      required: true,
    },
  },
  data() {
    return {
      valid: false,
      newVotingLink: "votingNew",
      user: window.localStorage.getItem("username"),
      group:{},
      keys: {},
      votings: {},
      count: 1,
      userToRemove: '',
      dialogGenerateAccessCode: false,
      dialogRemoveUser: false, 
      showActiveKeys: false,
      codeKey: false,
      printMethod: false,
      dialogShowNewCodes: false, 
      newCodes: [],
    };
  },
  methods: {
    getString,
    getColor,
    generatePdfCodes() {
      this.$refs.html2Pdf.generatePdf();
    },
    clearDialog() {
      this.dialogGenerateAccessCode = false;
      this.valid = true;
      this.$refs.code.reset();
      this.codeKey = !this.codeKey;
    },
    printKeys() {
      this.printMethod = true;
      print();
      this.printMethod = false;
    },
    removeUserFromGroup(member){
      console.log(member)
      this.dialogRemoveUser = true;
      this.userToRemove = member;
    },
    async removeUserConfirmed(){
      this.dialogRemoveUser = false;
      console.log(this.group)
      let endpoint = `api/groups/${this.group.id}/`;
           await apiService(endpoint, "PUT", {
          // id: this.group.id,
          // count_user: this.group.count_user,
          members: this.group.members,
          // images: this.group.images,
          admin_users: this.group.admin_users,
          name: this.group.name,
          description: this.group.description,
          // created_at: this.group.created_at,
        }).then(async data => {
            console.log("komunikat: ", data)
            if(data != "wrong data"){
              // this.dialog = true
              console.log(data)
              // this.group.name.value = data.name;
              // this.group.subname.value = data.subname;
              // this.group.desc.value = data.description;
            }
            
        })
    },
     generateAccessCode() {
      this.dialogGenerateAccessCode = true;
      
    },
       async refreshPage(){
      let endpoint = `api/groups/${this.group.id}/keys`;
      let data = await apiService(endpoint);
      var keys = [];
      var cnt = 2;
      var nextPage = data.next != null ? true : false;
      console.log(data);

      while (nextPage) {
        await apiService(endpoint + "?page=" + cnt).then((data) => {
          console.log(data);
          cnt += 1;
          nextPage = data.next != null ? true : false;
          for (var key of data.results) {
            keys.push(key);
          }
        });
      }

      this.keys = keys;
    },
    async generateAccessCodes() {
      await apiService(
        `/api/groups/${this.group.id}/genkeys?count=${this.count}`,
        "GET"
      ).then((data) => {
        this.dialogGenerateAccessCode = false;
        this.dialogShowNewCodes = true;
        console.log(data);
        this.newCodes = data;
         this.refreshPage()
      });
    },
  },
  created() {
    document.title = this.groupName;
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.id !== undefined) {
      let endpoint = `api/groups/${to.params.id}/keys`;
      let groupEndpoint = `api/groups/${to.params.id}/`;
      let data = await apiService(endpoint);
      let groupData = await apiService(groupEndpoint);
      var keys = [];
      var cnt = 2;
      var nextPage = data.next != null ? true : false;
      console.log(data);

      while (nextPage) {
        await apiService(endpoint + "?page=" + cnt).then((data) => {
          console.log(data);
          cnt += 1;
          nextPage = data.next != null ? true : false;
          for (var key of data.results) {
            keys.push(key);
          }
        });
      }

      let data2 = await apiService(`/api/groups/${to.params.id}/?details=1`);

      return next((vm) => {
        vm.group = groupData;
        vm.keys = keys;
        vm.votings = data2.votings;
      });
    } else {
      return next();
    }
  },
};
</script>

<style>
.area {
  margin: 30px;
  border-radius: 20px;
  padding-bottom: 50px;
}
.groupName {
  display: flex;
  font-size: 2rem;
  justify-content: center;
  margin: 50px;
  padding-bottom: 30px;
  padding-top: 50px;
}
.sectionsContainer {
  display: flex;
  justify-content: space-around;
}

.single-user {
  display: flex;
  justify-content: space-between;
  padding: 5px 30px 10px 30px;
  margin: 0 20px 20px 20px;
  border-bottom: solid 1px;
  align-items: center;
}

.rightSection {
  width: 80%;
  margin: 0 auto;
}

.galleryTitle {
  display: flex;
  font-size: 25px;
  justify-content: center;
  margin: 20px;
}
.images {
  display: flex;
}
.image {
  width: 600px;
  margin: 20px;
}
.leftArrow,
.rightArrow {
  align-items: center;
  display: flex;
  justify-content: center;
  margin: 10px;
}
.imageDescription,
.imageId,
.totalImages {
  display: flex;
  font-size: 15px;
  justify-content: center;
  margin-top: 10px;
}

.single-voting {
  margin: 30px 40px;
  font-weight: 600;
  line-height: 2;
}

.single-project {
  margin-left: 20px;
  line-height: 1.4;
  font-size: 0.8em;
}
.single-project::before {
  content: "-";
}

.add-voting {
  margin: 40px;
  display: flex;
  justify-content: space-between;
}

.exist-votings {
  border-bottom: solid 1px;
  padding: 10px 0;
  margin: 20px 40px;
}
.key-option {
  margin: 10px 40px;
  padding: 10px;
}

.key-option:hover {
  background-color: var(--v-primary-lighten1);
}
.all-keys {
  display: flex;
  justify-content: column;
  margin: 0 0 20px 40px;
  padding: 10px;
  flex-wrap: wrap;
}
.single-key {
  margin: 0 10px;
  font-size: 16px;
}

details {
  font-family: "Petrona";
  background-color: var(--v-primary-lighten3);
  opacity: 0.6;
  padding: 4px 6px;
  font-size: 1.7em;
  font-weight: 700;
  border: none;
  box-shadow: 3px 3px 4px rgba(75, 73, 73, 0.534);
  cursor: pointer;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-width: 700px !important;
}

summary {
  border: 4px solid transparent;
  text-transform: uppercase;
  outline: none;
  transition: all 1s ease;
  padding: 1rem;
  display: block;
  padding-left: 2.2rem;
  position: relative;
  cursor: pointer;
}

summary:before {
  content: "";
  border-width: 0.5rem;
  border-style: solid;
  border-color: transparent transparent transparent var(--v-accent-base);
  position: absolute;
  top: 1.6rem;
  left: 1rem;
  transform: rotate(0);
  transform-origin: 0.2rem 50%;
  transition: 1s transform ease;
}

details summary::-webkit-details-marker {
  display: none;
  transition: all 0.5s ease;
}
details[open] > summary:before {
  transform: rotate(90deg);
  transition: all 0.5s ease;
}
details[open] summary ~ * {
  animation: sweep 0.5s ease-in-out;
}

.customBtn{
  transition: all .3s ease-in-out;
  transform: scale(1);
}
.customBtn:hover{
  transition: all .3s ease-in-out;
  transform: scale(1.1);
}

#print-section {
  visibility: hidden;
}

@keyframes sweep {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@media only screen and (max-width: 750px) {
  .rightSection {
    max-width: 100%;
  }
}

@media print {
  body * {
    visibility: hidden;
  }
  #print-section,
  #print-section * {
    visibility: visible;
  }
  #print-section {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
  }

  #print-section .print-key {
    margin: 0 50px;
    color: black;
    padding: 20px;
    border-bottom: black solid 1px;
    text-align: center;
    font-size: 20px;
  }
}
</style>
