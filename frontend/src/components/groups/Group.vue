<template>
  <div class="container">
    <div class="row area">
      <div class="aboutGroup">
        <div>
          <div class="groupTitle">{{ group.name }}</div>
        </div>

        <div class="desc">
          <div v-if="group.description.length > 200">
            <span v-if="showMore">{{ group.description }} </span>
            <span v-else> {{ group.description.slice(0, 200) }}...</span>
            <div v-if="!showMore" class="paddingTop-m">
              <v-btn x-small color="primary" dark @click="showMore = true">
                {{ $t('expand') }}
              </v-btn>
            </div>
            <div v-else class="paddingTop-m">
              <v-btn
                x-small
                color="primary"
                dark
                v-if="showMore"
                @click="showMore = false"
              >
                 {{ $t('unexpand') }}
              </v-btn>
            </div>
          </div>
          <div v-else>
            {{ group.description }}
          </div>
        </div>
        <div class="membersNumber desc">
           {{ $t('membersNumber') }} {{ group.count_user }}
        </div>
      </div>
      <div class="col center  paddingTop-l">
        <div class="center">
          <div v-if="group.images.length > 0">
            <img :src="`/media/${group.images[0].image}`" class="image" />
          </div>

          <div class="text-center paddingTop-m">
            <v-dialog v-model="dialog2" width="unset">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on">
                 {{ $t('details') }}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h5 ">
                  <span>{{ group.name }}</span>

                  <span
                    v-if="isMember"
                    :title="$t('leaveGroup')"
                    @click="check(leaveGroup)"
                    class="icon p-2"
                    ><v-icon color="link">person_remove</v-icon> </span
                  ><span v-else @click="check(joinGroup)" class="icon p-2"
                    ><v-icon color="link">person_add</v-icon></span
                  >
                </v-card-title>

                <v-card-text>
                  <div>
                    <div class="projectDesc">
                      <div v-if="group.description.length > 200">
                        <span v-if="showMore2">{{ group.description }} </span>
                        <span v-else>
                          {{ group.description.slice(0, 200) }}...</span
                        >
                        <div v-if="!showMore2" class="paddingTop-m">
                          <v-btn
                            x-small
                            color="primary"
                            dark
                            @click="showMore2 = true"
                          >
                          {{ $t('expand') }}
                          </v-btn>
                        </div>
                        <div v-else class="paddingTop-m">
                          <v-btn
                            x-small
                            color="primary"
                            dark
                            v-if="showMore2"
                            @click="showMore2 = false"
                          >
                            {{ $t('unexpand') }}
                          </v-btn>
                        </div>
                      </div>
                      <div v-else>
                        {{ group.description }}
                      </div>
                    </div>
                  </div>
                </v-card-text>

                <v-divider></v-divider>

                <div v-show="isAdmin" class="icons-section">
                  <div class="icons-3">
                    <div class="single-icon">
                      <router-link
                        :to="{
                          name: 'group',
                          params: { id: group.id, group2: group },
                        }"
                        class="icon-image"
                      >
                        <v-btn class="mx-2" fab dark color="teal">
                          <v-icon dark>
                            mdi-format-list-bulleted-square
                          </v-icon>
                        </v-btn>
                      </router-link>
                      <div class="icon-desc">
                       {{ $t('codeList') }}
                      </div>
                    </div>

                    <div class="single-icon">
                      <div
                        class="icon-image"
                        :title="$t('generate')"
                        @click="generateAccessCode"
                      >
                        <v-btn class="mx-2" fab dark color="indigo">
                          <v-icon dark>
                            mdi-plus
                          </v-icon>
                        </v-btn>
                      </div>
                      <div class="icon-desc">
                       {{ $t('generateCodes') }}
                      </div>
                    </div>

                    <div class="single-icon">
                      <div
                        class="icon-image"
                        :title="$t('generate')"
                        @click="generateAccessCode"
                      >
                        <v-btn class="mx-2" fab dark color="red">
                          <v-icon dark>
                            mdi-minus
                          </v-icon>
                        </v-btn>
                      </div>
                      <div class="icon-desc">
                       {{ $t('removeUser') }}
                      </div>
                    </div>
                  </div>
                </div>

                <div class="animation">
                  <div>
                    <Carousel
                      :slides="group.images"
                      :ifRoute="ifRoute"
                      :group="groupCarousel"
                    />
                  </div>
                </div>

                <div class="votingList">
                  <div v-for="voting in votings" :key="voting.id">
                    <details>
                      <summary>
                        {{ voting.name }} {{ voting.start_date }}
                      </summary>
                      <div class="findLast">
                        <div
                          v-for="(project, index) in voting.projects"
                          :key="`project-${index}`"
                        >
                          <p>{{ project.name }}</p>
                        </div>

                        <div class="single">
                          <router-link
                            :to="{
                              name: 'voting',
                              params: { id: group.id, vId: voting.id },
                            }"
                          >
                            <v-btn color="primary" @click="goToVoting">
                                 {{ $t('goToVoting') }}
                            </v-btn>
                          </router-link>
                        </div>
                      </div>
                    </details>
                  </div>
                </div>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" text @click="dialog2 = false">
                       {{ $t('cancel') }}
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </div>
      </div>
    </div>

    <v-dialog v-model="dialog" width="600">
      <v-card>
        <v-card-title class="text-h4 g p-4 d-flex justify-content-center">
          {{ group.name }}
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <div>
            {{ $t('joinGroup') }}
          </div>

          <v-form
            v-model="valid"
            ref="code"
            :key="codeKey"
            style="margin-top: 30px"
          >
            <v-row class="d-flex justify-content-center">
              <div
                style="padding-left: 20px;  margin: 5px; padding-right:20px; border: solid; border-radius: 20px"
              >
                <v-text-field
                  style="width:170px; font-size: 36px"
                  v-model="myCode"
                  ref="code1"
                  autofocus
                  maxlength="8"
                ></v-text-field>
              </div>
            </v-row>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="clearDialog">
            {{ $t('cancel') }}
          </v-btn>
          <v-btn color="primary" text @click="joinGroupWithAccessCode">
            {{ $t('confirm') }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogLeaveGroup" width="500">
      <v-card>
        <v-card-title class="text-h4 p-4 d-flex justify-content-center">
          {{ group.name }}
        </v-card-title>

        <v-card-text class="text-h6  lighten-2 p-4 ">
          <span class="d-flex justify-content-center">
            {{ $t('leaveGroupQuestion') }}
            </span
          >
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialogLeaveGroup = false">
            {{ $t('cancel') }}
          </v-btn>
          <v-btn color="primary" text @click="check(leaveGroupWithConfirmation)">
            {{ $t('leave') }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

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
            {{ $t('cancel') }}
          </v-btn>
          <v-btn text @click="generateAccessCodes">
            {{ $t('generateConfirm') }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
 
<script>
import { apiService } from "@/common/api.service.js";
import Carousel from "@/components/UI/Carousel.vue";

export default {
  name: "Group",
  props: ["group", "name", "requestUser"],
  data() {
    return {
      showMore: false,
      showMore2: false,
      valid: false,
      loading: true,
      myCode: "",
      count: 1,
      groupCarousel: true,
      image: "",
      codeKey: false,
      dialog: false,
      ifRoute: false,
      dialog2: false,
      dialogLeaveGroup: false,
      dialogGenerateAccessCode: false,
      accessCode: "",
      isMember: false,
      isAdmin: false,
      accessCodeRules: [
        
        (v) => !!v || this.$t('accessCodeRequired'),
        (v) => v.length == 4 || this.$t('accessCodeLength'),
      ],
      votings: [],
    };
  },

  methods: {
    goToVoting() {
      console.log("ide");
    },
    check(funName) {
      if (
        window.localStorage.getItem("username") ==
        window.localStorage.getItem("unauthorized")
      ) {
        this.$root.$refs.App.ifLogin();
      } else {
        funName();
      }
    },
    joinGroup() {
      // if (
      //   window.localStorage.getItem("username") ==
      //   window.localStorage.getItem("unauthorized")
      // ) {
      //   this.$root.$refs.App.ifLogin();
      // } else {
        this.dialog = true;
      // }
    },
    generateAccessCode() {
      this.dialogGenerateAccessCode = true;
    },
    leaveGroup() {
      // if (
      //   window.localStorage.getItem("username") ==
      //   window.localStorage.getItem("unauthorized")
      // ) {
      //   this.$root.$refs.App.ifLogin();
      // } else {
        this.dialogLeaveGroup = true;
      // }
    },
    validate() {
      this.$refs.code.validate();
    },
    clearDialog() {
      this.dialog = false;
      this.code1 = "";
      this.count = 1;
      this.valid = true;
      this.$refs.code.reset();
      this.codeKey = !this.codeKey;
      this.dialogGenerateAccessCode = false;
    },
    async leaveGroupWithConfirmation() {
      await apiService(`/api/groups/${this.group.id}/member/`, "DELETE").then(
        (data) => {
          this.isUserMember(data);
          this.dialogLeaveGroup = false;
        }
      );
    },
    async generateAccessCodes() {
      await apiService(
        `/api/groups/${this.group.id}/genkeys?count=${this.count}`,
        "GET"
      ).then((data) => {
        console.log(data);
      });
    },
    async joinGroupWithAccessCode() {
      this.validate();
      if (this.valid) {
        await apiService(`/api/groups/${this.group.id}/member/`, "POST", {
          key: this.myCode,
        }).then((data) => {
          this.dialog = false;
          this.myCode = "";
          this.isUserMember(data);
          this.code1 = "";
          this.code2 = "";
          this.code3 = "";
          this.code4 = "";
          this.valid = true;
          this.$refs.code.reset();
        });
      }
    },
    isUserMember(data) {
      this.isMember = data.members.includes(this.requestUser);
      this.isAdmin = data.admin_users.includes(this.requestUser);
    },
  },
  components: {
    Carousel,
  },
  async created() {
    if (this.group.image)
      await apiService(`/api/photo/${this.group.image}/`).then((data) => {
        this.image = data.image;
      });
    await apiService(`/api/groups/${this.group.id}/?details=1`).then((data) => {
      this.votings = data.votings;
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
        this.clearDialog();
      }
    },
  },
};
</script>

<style scoped lang="postcss">
.aboutGroup {
  width: 60%;
  margin-left: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.icon:hover {
  cursor: pointer;
}

::v-deep input::-webkit-outer-spin-button,
::v-deep input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.area {
  background-color: var(--v-background-lighten2);

  $stl: 20px;
  border: solid 1px black;
  margin-bottom: 30px;
  margin-top: 10px;
  padding: 10px;
}

.projectDesc {
  font-size: 1.2rem;
  max-width: 500px;
  margin: 20px auto 50px auto;
  min-width: 500px;
  /* color: #000; */
}

.groupTitle {
  font-weight: 700;
  font-size: 1.5rem;
  margin-bottom: 10px;
  margin-top: 30px;
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

.center img {
  height: calc(30vh - 30px);
  width: auto;
  max-height: 150px;
  object-fit: contain;
  margin: 0 auto;
  /* width: 100%; */
}
.animation {
  max-height: 900px;
  padding-bottom: 40px;
  max-width: 600px;
  display: inherit !important;
  margin: 0 auto;
  /* border:solid; */
  -webkit-box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  -moz-box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  box-shadow: 5px 13px 13px 3px rgba(63, 63, 74, 0.26);
  /* transition: opacity 1s ease; */
  transition: all 2s ease;
  margin: 40px;
}
.animation[style*="display: none;"] {
  max-height: 0;
  opacity: 0;
  padding-bottom: 0px;
  pointer-events: none; /* disable user interaction */
  user-select: none; /* disable user selection */
}
.votingList {
  /* background-color: rgb(251, 207, 40); */
  background-image: linear-gradient(
    100deg,
    rgba(224, 232, 255, 0.2) 20%,
    rgba(120, 144, 156, 0.4) 100%
  );
  background-size: auto;
  background-position: right top;
  background-repeat: repeat;
  padding: 2rem;
}

details {
  /* font-family: "Petrona"; */
  padding: 4px 6px;
  width: 15em;
  font-size: 1.7em;
  font-weight: 700;
  border: none;
  box-shadow: 3px 3px 4px rgba(75, 73, 73, 0.534);
  cursor: pointer;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
/* 
details {
  max-width: 500px;
  box-sizing: border-box;
  margin-top: 5px;
  background: white;
  transition: all 1s ease;
} */

summary {
  border: 4px solid transparent;
  outline: none;
  transition: all 1s ease;
  padding: 1rem;
  display: block;
  /* background: rgb(99, 109, 107); */
  color: rgb(73, 50, 50);
  padding-left: 2.2rem;
  position: relative;
  cursor: pointer;
}

details summary::-webkit-details-marker {
  display: none;
  transition: all 1s ease;
}
details[open] > summary:before {
  transform: rotate(90deg);
  transition: all 1s ease;
}
details[open] summary ~ * {
  animation: sweep 1s ease-in-out;
}

@keyframes sweep {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
summary:before {
  content: "";
  border-width: 0.4rem;
  border-style: solid;
  border-color: transparent transparent transparent rgb(73, 50, 50);
  position: absolute;
  top: 1.6rem;
  left: 1rem;
  transform: rotate(0);
  transform-origin: 0.2rem 50%;
  transition: 1s transform ease;
}

/* details  */
details p {
  padding-left: 5px;
  font-size: 1rem;
  padding-top: 4px;
}
details p::before {
  content: "✓ ";
}
details .findLast {
  margin-bottom: 20px;
  margin-top: 20px;
}
.single {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.v-card__title {
  display: flex;
  justify-content: space-between;
}

.v-card__text {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

@media only screen and (max-width: 1200px) {
  .image {
    height: 300px;
    margin-bottom: 20px;
    /* margin-top: 50px; */
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

.icons-section {
  background-image: linear-gradient(
    200deg,
    var(--v-secondary-lighten2) 5%,
    var(--v-secondary-base) 80%,
    var(--v-secondary-darken1) 100%
  );
  padding: 40px 10px 40px 10px;
}
.icons-3 {
  display: flex;
  justify-content: space-around;
  padding: 40px 10px 40px 10px;
  margin: 0 auto;
  margin: 5px;
  align-items: flex-start;
  /* filter: blur(1px) */
  /* border:solid black 3px; */
  filter: contrast(200%);
  filter: drop-shadow(3px 3px 10px var(--v-accent-base)) invert(5%);
  background-color: rgba(255, 255, 255, 0.2);
}

.icons-3 .single-icon {
  flex-basis: 25%;
  display: flex;

  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.single-icon .icon-image {
  max-width: 100px;
  min-width: 60px;
  margin: 0 auto;
}

.single-icon .icon-desc {
  padding: 10px 5px 0px 5px;
  text-align: center;
  margin: 0 auto;
}

@media only screen and (max-width: 1000px) {
  .aboutGroup {
    margin: 0 auto;
    padding: 10px 20px;
  }
  .groupTitle {
    margin: 20px auto;
  }
}

@media only screen and (max-width: 800px) {
  .area {
    margin: 0 auto 50px auto;
  }

  .aboutGroup {
    max-width: 700px;
    padding: 10px;
    width: 90%;
    margin: 10px auto;
  }

  .desc {
    margin-top: 0;
  }

  .center {
    margin-bottom: 20px;
  }
}

@media only screen and (max-width: 550px) {
       .projectDesc{
         min-width: unset;
       }
}
</style>
