<template>
    <div class="commentContainer">
        <div class="topSection">
            <div class=leftTopSection>
                <div class="userName">
                    <div v-if="author">
                        {{author}}
                        <!-- {{comment}} -->
                    </div>
                    <div v-else>
                        {{ comment.author }}
                    </div>
                </div>
                <div class="rating">
                    <v-rating
                        v-model="comment.rating"
                        color="yellow darken-3"
                        background-color="grey darken-1"
                        empty-icon="$ratingFull"
                        half-icon="mdi-star-half"
                        half-increments
                        hover
                        small
                        readonly 
                    ></v-rating>
                </div>
            </div>
            
            <div class="rightTopSection">
                <div class="date">
                    {{ comment.created_at }}
                    <div v-if="loggedUser==author" @click="deleteComment">
                        <v-icon>{{ icons.mdiDelete }}</v-icon>
                    </div>
                </div>
                <!-- ? v-if="loggedUser!=comment.author" -->
                <div class="likes">
                    <plus-minus-rating
                        :likes="comment.likes_count"
                        :dislikes="comment.dislikes_count"
                        :userVotedFor="comment.user_has_liked"
                    />
                </div>
            </div>
        </div>
        
        <div class="text">
            {{ comment.content }}
        </div>
    </div>
</template>

<script>
    import PlusMinusRating from '../UI/PlusMinusRating.vue'
    import {mdiDelete} from '@mdi/js'

    export default {
        name: "comment",        
        props: ["comment", "ifDelete", "author"],
        data(){
            return {
                loggedUser: "",
                icons:{
                    mdiDelete
                }
            }
        },
        components:{
                // Stars,
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