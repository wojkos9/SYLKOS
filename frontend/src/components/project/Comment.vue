<template>
    <div class="commentContainer">
        <div class="topSection">
            <div class=leftTopSection>
                <div class="userName">
                    {{ userName }}
                </div>
                <div class="rating">
                    <stars v-bind:rating="rating"/>
                </div>
            </div>
            
            <div class="rightTopSection">
                <div class="date">
                    {{ postingDate }}
                    <div v-if="loggedUser==userName" @click="deleteComment">
                        <v-mdi name="mdiDelete"></v-mdi>
                    </div>
                </div>
                <div class="likes" v-if="loggedUser!=userName">
                    <plus-minus-rating
                        :likes="likes"
                        :dislikes="dislikes"
                        :userVotedFor="userVotedFor"
                    />
                </div>
            </div>
        </div>
        
        <div class="text">
            {{ commentText }}
        </div>
    </div>
</template>

<script>
    import PlusMinusRating from '../UI/PlusMinusRating.vue'
    import Stars from '../UI/Stars.vue'
    // import { apiService } from "@/common/api.service.js";
    export default {
        name: "comment",        
        props: {
            projectId: {
            type: Number,
            required: true,
            },
            userName: {
            type: Text,
            required: true,
            },
            rating: {
            type: Number,
            required: true,
            },
            postingDate: {
            type: Text,
            required: true,
            },
            commentText: {
            type: Text,
            required: true,
            },
            likes: {
            type: Number,
            required: true,
            },
            dislikes: {
            type: Number,
            required: true,
            },
            userVotedFor: {
            type: Text,
            required: true,
            },
        },
        data(){
            return {
                loggedUser: ""
            }
        },
        components:{
                Stars,
                PlusMinusRating
        },
        methods:{
            async setUserInfo() {
                this.loggedUser = window.localStorage.getItem("username");
            },
            deleteComment(){
                console.log("comment deleted")
                // apiService("/api/projects/"+this.projectId+"")
            }
        },
        created() {
            this.setUserInfo();
        },
    }
</script>

<style link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons" scoped>
    
    .commentContainer {
        border: solid 1px black;
        border-radius: 25px;
        margin: 20px;
        padding: 20px; 
        width: 400px;
    }
    .topSection {
        display: flex;
        margin-bottom: 10px;
    }
    .leftTopSection {
        flex: 50%;
    }
    .rightTopSection {
        align-items: flex-end;
    }
    .userName {
        margin-bottom: 5px;
    }
    .date {
        margin-bottom: 10px;
        display: flex;
    }
    .likes {
        /* border: solid 1px black; */
        display: flex;  
        font-size: 25px;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
</style>