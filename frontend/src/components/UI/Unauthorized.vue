<template>
  <v-dialog v-model="dialog" width="600px"   @click:outside="backAction">
    <v-card>
      <v-card-title>
        BRAK DOSTĘPU
      </v-card-title>

      <v-card-text style="flex-direction: column">
        <span style="font-size: 20px"
          >Aby uzyskać dostęp do tej sekcji wymagane jest zalogowanie</span
        ><br />
        <br />
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="backAction">
          <span>anuluj</span>
        </v-btn>
        <v-btn color="green darken-1" text @click="nextAction">
          <span>zaloguj się</span>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { getString } from "@/language/string.js";
export default {
  name: "Unauthorized",
  props: ["dialog", "backAction", "nextAction"],
  data() {
    return {
      dialogFropProps: false,
    };
  },
  methods: {
    getString,
  },
  computed() {
  },
};
</script>
