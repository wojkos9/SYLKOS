<template>
  <v-card color="primary darken-1">
    <div
      cols="12"
      class="p-3 d-flex justify-content-end"
      style="border:solid; height: 100px "
    >
      <v-btn color="primary" class="ma-2 p-3" dark @click="footer = true">
        {{ getString("footer", "rules") }}
      </v-btn>
    </div>

    <v-dialog
      v-model="footer"
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
          <v-toolbar-title>{{ getString("footer", "rules") }}</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text class="m-5">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. In leo orci,
          maximus tristique vestibulum id, viverra ac mi. Integer consectetur,
          ligula at euismod consectetur, orci tellus laoreet ipsum, ac tempor mi
          sem et risus. Vestibulum mi odio, scelerisque vitae turpis
          ullamcorper, mollis sodales lorem. Quisque in facilisis ante. Sed
          rutrum magna est, eget condimentum lectus consectetur in. Aliquam
          gravida porttitor tortor, ac porttitor dolor venenatis sit amet.
          Mauris placerat dapibus magna, id posuere tortor bibendum eget.
          <v-divider></v-divider>
          Integer luctus vel justo quis dictum. Duis ultricies, mauris a
          volutpat molestie, felis justo congue risus, ut malesuada purus arcu
          vel ex. Ut eget tortor dui. Pellentesque aliquam eros vitae dignissim
          aliquet. Vestibulum ante ipsum primis in faucibus orci luctus et
          ultrices posuere cubilia curae; Fusce ut ex sed lacus dignissim
          pharetra sed quis turpis. In rhoncus quis ante at dignissim. Morbi
          maximus, sapien ac fringilla pretium, diam mauris facilisis magna, sed
          dictum nunc neque nec diam. Ut sed dignissim tortor, ut viverra nisl.
          Vestibulum luctus tristique accumsan. Donec ac vehicula arcu. Etiam
          venenatis, felis quis venenatis placerat, metus tellus dictum mi, sed
          feugiat dui ex eu ipsum. Etiam porttitor mi a purus finibus dignissim.
          Nullam euismod ex ipsum, quis ultricies nisi blandit vitae.
          <v-divider></v-divider>
          Maecenas luctus egestas nulla sit amet tincidunt. Suspendisse potenti.
          Sed placerat, felis at auctor blandit, metus neque lacinia sapien, eu
          congue diam leo finibus turpis. Sed quis tellus maximus, volutpat eros
          sed, gravida felis. Mauris et dolor convallis, fringilla tellus et,
          suscipit libero. Mauris porttitor vel augue ac feugiat. Donec sed
          felis ipsum. In nec mollis urna. Sed a pellentesque tellus. Integer
          vulputate, tortor id semper congue, quam purus viverra mi, ac pulvinar
          orci felis venenatis tellus.
          <v-divider></v-divider>
          In hac habitasse platea dictumst. Fusce venenatis erat eget tortor
          vehicula placerat. Sed eget tortor ut nunc pellentesque auctor. Donec
          pellentesque justo sit amet elit rhoncus, a ullamcorper arcu
          fringilla. Sed sed varius velit. Mauris ornare massa sem, et tempus
          nisl blandit sit amet. Phasellus vel imperdiet ex.
          <v-divider></v-divider>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce dictum
          ac sapien at malesuada. Etiam sed dolor sed justo consectetur
          efficitur. Vestibulum ante ipsum primis in faucibus orci luctus et
          ultrices posuere cubilia curae; Vivamus semper lacinia magna. Duis ut
          tincidunt quam, sit amet vestibulum nisi. Proin auctor eleifend neque
          in fringilla. Mauris sit amet fringilla tellus. Proin in est
          convallis, condimentum lectus eu, rhoncus urna. Ut sollicitudin semper
          ultrices. Quisque tempor lacinia lectus at rutrum.
        </v-card-text>

        <div style="flex: 1 1 auto;"></div>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { getString } from "@/language/string.js";

export default {
  name: "Footer",
  data() {
    return {
      footer: false,
    };
  },
  methods: {
    getString,
    showRules() {
      this.footer = true;
    },
    hideRules() {
      this.footer = false;
    },
  },
};
</script>

<style></style>
