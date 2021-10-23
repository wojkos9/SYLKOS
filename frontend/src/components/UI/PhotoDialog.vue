<template>

  <v-card color="primary darken-1"  v-bind="localAttrs">
    <div
      cols="12"
      class="p-3 d-flex justify-content-end"
      style="border:solid; height: 100px "
    >
      <v-btn color="secondary" class="ma-2 p-3" dark @click="footer = true" style="color:black">
        {{ title }}
      </v-btn>
    </div>

    <v-dialog
      v-model="photoDialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
      scrollable
    >
      <v-card tile>
        <v-toolbar flat dark color="primary">
          <v-btn icon dark @click="footer = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>{{ title }}</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text class="m-5">
          <Carousel :slides="slides" :ifRoute="ifRoute"  :group="group" :title="title"/>
        </v-card-text>

        <div style="flex: 1 1 auto;"></div>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { getString } from "@/language/string.js";

export default {
  name: "photoDialog",
  props: ["slides", "title", "group"],
  data() {
    return {
      photoDialog: false,
    };
  },
  methods: {
    getString,
    showRules() {
      this.photoDialog = true;
    },
    hideRules() {
      this.photoDialog = false;
    },
  },
  computed: {
      localAttrs () {
        const attrs = {}


          attrs.absolute = true


        return attrs
      }
    },
};
</script>

<style></style>
