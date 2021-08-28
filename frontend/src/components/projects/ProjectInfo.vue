<template>
    <div>
        <div class="singleInfo">{{ getString("projectInfo", "price") }}: {{ price }}</div>
        <div class="singleInfo">{{ getString("projectInfo", "votingEndDate") }}: {{ votingEndDate }}</div>
        <div class="singleInfo">{{ getString("projectInfo", "projectUploadDate") }}: {{ projectUploadDate }}</div>
    </div>
</template>

<script>
    import { getString } from "@/language/string.js";
    export default {
        name: "projectInfo",
        props: ["price", 
        "votingEndDate", 
        "projectUploadDate"],
        methods:{
            getString
        }
    }
</script>

<style scoped>
.singleInfo{
  padding: 10px;
}
</style>