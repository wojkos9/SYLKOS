<template>

  <v-card color="primary darken-1"  v-bind="localAttrs" class="footer-gradient">
    <div class="footer-gradient-transparent"></div> 
    <div
      class="p-3 d-flex justify-content-end"
      style="height: 100px "
    >
      <v-btn color="accent" class="ma-2 p-3" dark @click="footer = true" style="color:black" >
        {{ $t('rules') }}
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
        
          <v-toolbar-title>{{ $t('rules') }}</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card-text class="p-5">
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

export default {
  name: "Footer",
  data() {
    return {
      footer: false,
    };
  },
  methods: {
    showRules() {
      this.footer = true;
    },
    hideRules() {
      this.footer = false;
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

<style scoped>
v-dialog{
  width: 100%;
}

.footer-gradient-transparent {
  width: 100%;
  z-index: 0;
  content: "";
  display: block;
  position: absolute;
  opacity: 0.9;
  top: 0;
  left: 0;
  background: linear-gradient(
    to right,
    rgba(26, 23, 23, 0) 0%,
    var(--v-primary-base) 50%,
    var(--v-primary-base) 100%
  );
  height: 100%;
}

.footer-gradient::before {
  width: 100%;
  content: "";
  display: block;
  position: absolute;
  top: 0;

  left: 0;
  z-index: 0;
  height: 100%;
  background-color: #78909c;
  opacity: 0.5;
  background-image: linear-gradient(
      30deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      150deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      30deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      150deg,
      #00bfa5 12%,
      transparent 12.5%,
      transparent 87%,
      #00bfa5 87.5%,
      #00bfa5
    ),
    linear-gradient(
      60deg,
      var(--v-secondary-darken2) 25%,
      transparent 25.5%,
      transparent 75%,
      var(--v-secondary-darken2) 75%,
      var(--v-secondary-darken2)
    ),
    linear-gradient(
      60deg,
      var(--v-secondary-darken2) 25%,
      transparent 25.5%,
      transparent 75%,
      var(--v-secondary-darken2) 75%,
      var(--v-secondary-darken2)
    );

  background-size: 26px 46px;
  background-position: 0 0, 0 0, 10px 18px, 10px 18px, 0 0, 10px 18px;
  background-repeat: repeat;
}
</style>
