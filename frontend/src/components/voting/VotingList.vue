<template>
<div class="area">
    <ol>
        <li v-for="(voting, index) in votings" v-bind:key="index">
            <votings-list-element
                :votingDetails="voting"
                :id="id"
            />
        </li>
    </ol>
</div>

</template>

<script>
    import VotingsListElement from './VotingsListElement.vue';
    export default {
        name: "VotingList",
        props: {
            id: {
            type: Number,
            required: true,
            },
        },
        data(){
            return {
                votings: [
                    {
                        title: "Inwestycje na rok 2022",
                        expirationDate: "21.12.2021",
                        projects: ["remont placu zabaw", "parking w miejsce łąki", "siłownia na powietrzu"]
                    },
                    {
                        title: "Remonty 2021",
                        expirationDate: "21.11.2021",
                        projects: ["remont placu zabaw", "remont śmietnika", "remont klatki schodowej"]
                    },
                    {
                        title: "Boisko 2021",
                        expirationDate: "21.10.2021",
                        projects: ["boisko do siatkówki", "boisko do piłki nożnej", "boisko do koszykówki"]
                    }]
                }
                    
        },
        components: {
            VotingsListElement
        }
    }

</script>

<style scoped>

</style>