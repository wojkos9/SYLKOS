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
                {{ $t("groupForm.newGroup") }}
              </div>

              <v-text-field
                class="p-2 m-3"
                dense
                v-model="name.value"
                :rules="name.rule"
                :label="name.label"
                required
              ></v-text-field>
              <!-- <v-text-field class="p-2 m-3"
            v-model="subname.value"
            :rules="subname.rule"
            :label="subname.label"
            required
          ></v-text-field> -->
              <v-text-field
                class="p-2 m-3"
                v-model="desc.value"
                :rules="desc.rule"
                :label="desc.label"
                required
              ></v-text-field>
              <v-file-input
                class="p-2 m-3"
                :label="photo.label"
                v-model="selectedFiles"
                append-icon="mdi-camera"
                prepend-icon=""
                multiple
              ></v-file-input>
              <div class="d-flex justify-content-end p-4 buttons">
                <v-btn class="mr-4 p-2" @click="submit">
                  {{ $t("groupForm.submit") }}
                </v-btn>
                <v-btn @click="clear">
                  {{ $t("groupForm.clearData") }}
                </v-btn>
              </div>
            </v-container>
          </v-form>
        </div>
        <div class="d-none d-sm-block col-md-2 col-lg-3" />
      </div>
    </div>

    <DialogWithUser
      :title="$t('success')"
      :desc="$t('groupForm.desc')"
      :nextAction="nextFunction"
      :backAction="backFunction"
      :dialog="dialog"
      :object="group"
    />
  </div>
</template>

<script>
import { apiService, imageUpload } from "@/common/api.service.js";
import DialogWithUser from "../components/UI/DialogWithUser.vue";

export default {
  name: "groupScreen",
  components: { DialogWithUser },
  data() {
    return {
      valid: false,
      newName: "costam",
      group: {
        name: {
          label: this.$t("groupForm.groupNameLabel"),
          value: "",
        },
        desc: {
          label: this.$t("groupForm.groupDescLabel"),
          value: "",
        },
        pictures: {
          label: this.$t("groupForm.pictures"),
          value: 0,
        },
      },
      name: {
        label: this.$t("groupForm.groupNameLabel"),
        rule: [(v) => !!v || this.$t("groupForm.groupNameError")],
        value: "",
      },

      desc: {
        label: this.$t("groupForm.groupDescLabel"),
        rule: [(v) => !!v || this.$t("groupForm.groupDescError")],
        value: "",
      },
      photo: {
        label: this.$t("groupForm.groupPhotoLabel"),
        rule: [],
        value: {},
      },

      selectedFiles: [],
      dialog: false,
    };
  },
  methods: {
    clear() {
      this.name.value = "";
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
        await apiService("/api/groups/", "POST", {
          name: this.name.value,
          description: this.desc.value,
          members: [],
          admin_users: []
        }).then(async (data) => {
          if (data != "wrong data") {
            this.dialog = true;
            let groupId = data.id;
            this.group.name.value = data.name;
            this.group.desc.value = data.description;
            for (var file of this.selectedFiles) {
              let formData = new FormData();
              formData.append("image", file);
              formData.append("group", groupId);
              formData.append("description", "opis zdjęcia");
              await imageUpload(formData).then(() => {
                this.group.pictures.value++;
              });
            }
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
};
</script>

<style scoped>
.groupForm {
  border: solid;
  background-color: var(--v-background-lighten3);
  vertical-align: middle;
  margin: 20px;
  width: 90%;
}

.background {
  width: 100%;
  background-color: #c0cfe6;
  margin-top: 150px;
}
.groupName {
  font-size: 2rem;
  padding-bottom: 2rem;
  padding-top: 1.5rem;
  text-align: center;
}
.v-input__control {
  width: 100%;
  max-width: none;
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
