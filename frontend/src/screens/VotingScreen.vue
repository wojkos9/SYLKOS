<template>
    <div >
        <div>
            <voting-header 
            :date="date"
            :group="group"
            />
        </div>
        <div class="projects">
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="userVotedFor"
            />
            
        </div>
        <div class="submitButton">
            <button-submit-vote/>
        </div>
    </div>
</template>

<script>
    import VotingHeader from '../components/voting/VotingHeader.vue';
    import ButtonSubmitVote from '../components/voting/ButtonSubmitVote.vue';
    import VotingProject from '../components/voting/VotingProject.vue';
    export default {
        name: "votingScreen",
        props: {
            id: {
            type: Number,
            required: true,
            },
            vId: {
            type: Number,
            required: true,
            },
        },
        // props: ['date', 'group', 'title', 'description', 'price', 'likes', 'dislikes', 'userVotedFor'],
        data(){
            return {
                date:"24 listopada 2021",
                group:"Osiedle Kwiatowe",
                title:"Łąka przy osiedlowym strumyku",
                description:"Miejsce do relaksu dla mieszkańców osiedla. Obok strumyka przepływającego " +
                "przez osiedle planujemy zasadzić drzewa i kwiaty, postawić ławki i dać możliwość odpoczynku z naturą.",
                price:"10 000",
                likes:"21",
                dislikes:"37",
                userVotedFor:"nothing",
            }
        },
        components: {
            VotingHeader,
            ButtonSubmitVote,
            VotingProject
        }
    }
</script>

<style scoped>
    .projects {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    .submitButton {
        display: flex;
        justify-content: flex-end;
        margin-right: 120px;
        margin-bottom: 40px;
    }
</style>