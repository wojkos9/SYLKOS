<template>
  <div>
    <h1>{{ id }}</h1>
    <router-link :to="{ name: 'voting', params:{id:id, vId:1}}"><h3>kliknij zeby zobaczyc glosowanie</h3></router-link>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "groupScreen",
  components: {},
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {};
  },
  methods: {
    getString,
    getColor,
  },
};
</script>
