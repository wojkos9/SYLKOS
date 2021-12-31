<template>
  <div :style="button">
    <div>{{ $t("submitMyVote").toUpperCase() }}</div>
  </div>
</template>

<script>
export default {
  name: "buttonSubmitVote",
  data() {
    return {};
  },
  computed: {
    button() {
      return {
        alignItems: "center",
        backgroundColor: getColor("green"),
        borderRadius: "5px",
        color: getColor("white"),
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        padding: "20px",
        fontWeight: "700",
      };
    },
  },
  methods: {
  },
};
</script>

<style scoped></style>
