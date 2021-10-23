<template>
  <div class="container">
    <div class="row area">
      <div class="col-lg-12 col-xl-9">
        <div>
          <div>
            <div class="groupTitle">{{ group.name }}</div>
            <span
              v-if="isMember"
              :title="getString('groups', 'leaveGroup')"
              @click="leaveGroup"
              ><md-icon>person_remove</md-icon> członek</span
            ><span v-else @click="joinGroup"
              ><md-icon>person_add</md-icon>dołącz</span
            >
          </div>

          <div class="desc">
            {{ group.description }}
          </div>
          <div class="membersNumber desc">
            {{ getString("groups", "membersNumber") }} {{ group.count_user }}
          </div>
        </div>
      </div>
      <div class="col center">
        <div class="center">
          <div v-if="group.images.length > 0">
            <img :src="`/media/${group.images[0].image}`" class="image" />
          </div>

          <router-link :to="{ name: 'group', params: { id: group.id } }"
            ><div :style="button">Dowiedz się więcej</div></router-link
          >
        </div>
      </div>
    </div>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title
          class="text-h4 grey lighten-2 p-4 d-flex justify-content-center"
        >
          {{ group.name }}
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <span class="d-flex justify-content-center">
            {{ getString("groups", "joinGroup") }}</span
          >

    
          <v-form v-model="valid" ref="code" :key="codeKey" style="margin-top: 30px">
            <v-row class="d-flex justify-content-center">
              <div
                style="padding-left: 10px;  margin: 5px; padding-right:10px; border: solid; border-radius: 10px"
              >
                <v-text-field
                  style="width:25px; fontSize: 36px"
                  v-model="code1"
                  :rules="codeRule"
                  ref="code1"
                  autofocus
                  maxlength="1"
                ></v-text-field>
              </div>
              <div
                style="padding-left: 10px; padding-right:10px;  margin: 5px; border: solid; border-radius: 10px"
              >
                <v-text-field
                  style="width:25px; fontSize: 36px"
                  ref="code2"
                  :rules="codeRule"
                  v-model="code2"
                  maxlength="1"
                ></v-text-field>
              </div>
              <div
                style="padding-left: 10px;  margin: 5px;  padding-right:10px; border: solid; border-radius: 10px"
              >
                <v-text-field
                  style="width:25px; fontSize: 36px"
                  ref="code3"
                  :rules="codeRule"
                  maxlength="1"
                  v-model="code3"
                ></v-text-field>
              </div>
              <div
                style="padding-left: 10px;  margin: 5px; padding-right:10px; border: solid; border-radius: 10px"
              >
                <v-text-field
                  style="width:25px; fontSize: 36px"
                  ref="code4"
                  :rules="codeRule"
                  maxlength="1"
                  v-model="code4"
                ></v-text-field>
              </div>
            </v-row>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="clearDialog">
            {{ getString("groups", "cancel") }}
          </v-btn>
          <v-btn color="primary" text @click="joinGroupWithAccessCode">
            {{ getString("groups", "confirm") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogLeaveGroup" width="500">
      <v-card>
        <v-card-title
          class="text-h4 grey lighten-2 p-4 d-flex justify-content-center"
        >
          {{ group.name }}
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <span class="d-flex justify-content-center">
            {{ getString("groups", "leaveGroupQuestion") }}</span
          >
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialogLeaveGroup = false">
            {{ getString("groups", "cancel") }}
          </v-btn>
          <v-btn color="primary" text @click="leaveGroupWithConfirmation">
            {{ getString("groups", "leave") }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService } from "@/common/api.service.js";

export default {
  name: "Group",
  props: ["group", "name", "requestUser"],
  data() {
    return {
      valid: false,
      loading: true,
      code1: "",
      code2: '',
      code3: '',
      code4: '',
      image: "",
      codeKey: false,
      dialog: false,
      dialogLeaveGroup: false,
      accessCode: "",
      isMember: false,
      accessCodeRules: [
        (v) => !!v || getString("groups", "accessCodeRequired"),
        (v) => v.length == 4 || getString("groups", "accessCodeLength"),
      ],
      codeRule:[
         (v) => !!v ,
      ]
    };
  },

  methods: {
    getString,
    getColor,
    joinGroup() {
      this.dialog = true;
    },
    leaveGroup() {
      this.dialogLeaveGroup = true;
    },
    validate() {
      this.$refs.code.validate();
    },
    clearDialog() {
      this.dialog = false;
      this.code1 = '';
      this.code2 = '';
      this.code3 = '';
      this.code4 = '';
      this.valid = true;
      this.$refs.code.reset();
      this.codeKey = !this.codeKey
      
    },
    async leaveGroupWithConfirmation() {
      await apiService(`/api/groups/${this.group.id}/member/`, "DELETE").then(
        (data) => {
          this.isUserMember(data);
          this.dialogLeaveGroup = false;
        }
      );
    },
    async joinGroupWithAccessCode() {
      this.validate();
      if (this.valid) {
        await apiService(`/api/groups/${this.group.id}/member/`, "POST").then(
          (data) => {
            this.dialog = false;
            this.isUserMember(data);
            console.log(data);
            this.code1 = '';
            this.code2 = '';
            this.code3 = '';
            this.code4 = '';
            this.valid = true
            this.$refs.code.reset();
          }
        );
      }
    },
    isUserMember(data) {
      this.isMember = data.members.includes(this.requestUser);
    },
  },

  computed: {
    button() {
      return {
        backgroundColor: getColor("navbar"),
        width: "160px",
        marginTop: "5px",
        borderRadius: "5px",
        textAlign: "center",
        padding: "3px",
        fontWeight: "500",
      };
    },
  },
  components: {},
  async created() {
    if (this.group.image)
      await apiService(`/api/photo/${this.group.image}/`).then((data) => {
        this.image = data.image;
        this.loading = false;
      });
    this.isUserMember(this.group);
  },
  watch: {
    code1(value) {
      if (value != "") {
        this.$refs.code2.focus();
      }
    },
    code2(value) {
      if (value != "") {
        this.$refs.code3.focus();
      }
    },
    code3(value) {
      if (value != "") {
        this.$refs.code4.focus();
      }
    },
    dialog(value) {
      if (value == false) {
        this.clearDialog()
      }
    },
  },
};
</script>

<style scoped>
.area {
  background-color: white;
  border: solid 1px black;
  margin-bottom: 30px;
  margin-top: 10px;
  padding: 10px;
}

.groupTitle {
  font-weight: 700;
  font-size: 1.5rem;
  margin-bottom: 40px;
  margin-top: 20px;
  text-align: center;
}

.desc {
  font-size: 1rem;
  font-weight: 400;
  margin-bottom: 10px;
  text-align: justify;
}

.membersNumber {
  margin-top: 30px;
}

.myButton {
  align-items: center;
  display: flex;
  justify-content: center;
}

.image {
  align-self: center;
  border-radius: 5px;
  height: 160px;
  justify-self: center;
  object-fit: cover;
  width: 160px;
}

.center {
  align-content: center;
  align-items: center;
  justify-content: center;
  justify-items: center;
}

@media only screen and (max-width: 1200px) {
  .image {
    height: 300px;
    margin-bottom: 20px;
    margin-top: 50px;
    width: 300px;
  }
  .center {
    float: none;
    margin: 0 auto;
    width: auto;
  }
  .desc {
    font-size: 0.875rem;
  }
  .title {
    font-size: 1.125rem;
  }
  .myButton {
    width: 300px;
  }
}
</style>
