<template>
    <div class="area">
        <div class="header">
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
            :userVotedFor="nothing"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="nothing"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="nothing"
            />
            <voting-project
            :title="title"
            :description="description"
            :price="price"
            :likes="likes"
            :dislikes="dislikes"
            :userVotedFor="nothing"
            />
            
        </div>
        <div class="submitButton">
            <button-submit-vote/>
        </div>
    </div>
</template>

<script>
    import VotingHeader from '../UI/votingHeader.vue';
    import ButtonSubmitVote from '../UI/buttonSubmitVote.vue';
    import VotingProject from './votingProject.vue';
    export default {
        name: "votingPage",
        props: ['date', 'group', 'title', 'description', 'price', 'likes', 'dislikes', 'userVotedFor'],
        data(){
            return {

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