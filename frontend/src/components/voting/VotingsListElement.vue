<template>
    <div class="area">
        <div class="topSection">
            <div class="votingName">
                {{ votingDetails.title }}
            </div>
            <div class="expandIcon" style="color: #93abc4" @click="changeDisplay" v-if="!showDetails">
                <v-mdi name="mdiPlusBox"></v-mdi>
            </div>
            <div class="expandIcon" style="color: red" @click="changeDisplay" v-else>
                <v-mdi name="mdiMinusBox"></v-mdi>
            </div>
            
        </div>
        <div class="bottomSection" v-if="showDetails">
            <div class="expirationDate">
                {{ getString('groups', 'expirationDate') }}: {{ votingDetails.expirationDate }}
            </div>
            <div class="projectsList">
                <ul>
                    <li v-for="(project, index) in votingDetails.projects" v-bind:key="index">
                        {{ project }}
                    </li>
                </ul>
            </div>
            <div class="goToVotingLink">
                <router-link :to="{ name: 'voting', params:{id:id, vId:1}}"><h3>{{ getString('groups', 'goToVoting') }}</h3></router-link>
            </div>
        </div>
        <div class="bottomSection" v-else>

        </div>


    </div>    
</template>

<script>
    import { getString } from "@/language/string.js";
    export default {
        name: "VotingsListElement",
        props: ['votingDetails', 'id'],
        data(){
            return {
                showDetails: false
            }
        },
        methods: {
            getString,
            changeDisplay(){
                this.showDetails = !this.showDetails
                console.log(this.showDetails)
            }
        }
    }
</script>
<style link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons" scoped>
    .area{
        /* border: solid 1px black; */
        margin-bottom: 10px;
    }
    .topSection{
        display: flex;  
        padding: 10px;
    }
    .votingName{
        font-family: Arial, Helvetica, sans-serif;
        font-size: 20px;
        width: 250px;

    }
    .bottomSection{
        align-items: flex-start;
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
    .expirationDate, .goToVotingLink{
        margin: 10px;
        padding-left: 10px;
    }
</style>