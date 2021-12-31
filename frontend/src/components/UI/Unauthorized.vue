<template>
  <v-dialog v-model="dialog" width="600px"   @click:outside="backAction">
    <v-card>
      <v-card-title>
        {{$t("accesDeniedTitle")}}
      </v-card-title>

      <v-card-text style="flex-direction: column">
        <span style="font-size: 20px"
          >{{$t("accessDenied")}}</span
        ><br />
        <br />
      </v-card-text>
      <v-card-actions> 
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="backAction">
          <span>{{$t("cancel")}}</span>
        </v-btn>
        <v-btn color="green darken-1" text @click="nextAction">
          <span>{{$t("login")}}</span>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "Unauthorized",
  props: ["dialog", "backAction", "nextAction"],
  data() {
    return {
      dialogFropProps: false,
    };
  },
  methods: {
  },
  computed() {
  },
};
</script>
