<template>
    <div class="commentContainer">
        <div class="topSection">
            <div class=leftTopSection>
                <div class="userName">
                    {{ userName }}
                </div>
                <div class="rating">
                    <stars v-bind:stars="rating"/>
                </div>
            </div>
            
            <div class="rightTopSection">
                <div class="date">
                    {{ postingDate }}
                </div>
                <div class="likes">
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
    import Stars from '../UI/Stars.vue'
    export default {
        name: "comment",
        props: ['userName', 'rating', 'postingDate', 'commentText', 'likes', 'dislikes', 'userVotedFor'],
        data(){
            return {
                
            }
        },
        components:{
                Stars
        }
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
    }
    .likes {
        /* border: solid 1px black; */
        display: flex;  
        font-family: "playfair display";
        font-size: 25px;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
</style>