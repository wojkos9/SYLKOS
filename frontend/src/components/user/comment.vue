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
                    <div class="plus" @click="incrementLikes">
                        <v-mdi v-style="icon" name="mdiPlusThick"></v-mdi>
                    </div>
                    <!-- <button type="button" @click="incrementLikes">Increase By 1</button> -->
                    {{ likes }}
                    <div class="minus" @click="incrementDislikes">
                        <v-mdi v-style="icon" name="mdiMinusThick"></v-mdi>
                    </div>
                    {{ dislikes }}
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
        props: [],
        data(){
            return {
                userName: 'Mateusz Kluba',
                rating: "3.5",
                postingDate: '13.09.2021',
                commentText: 'Świetny pomysł! Sam nieraz widzę potrzebę lepszego oświetlenia naszych alejek. Chciałbym jednak znać więcej szczegółów',
                likes: 0,
                dislikes: 0
            }
        },
        methods:{
            incrementLikes: function(){
                this.likes++;
            },
            incrementDislikes(){
                this.dislikes++;
            }
        },
        components:{
                Stars
        }
    }
</script>

<style link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons" scope>
    
    .commentContainer {
        border: solid 1px black;
        border-radius: 25px;
        /* height: 200px; */
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
        /* align-items: center; */
        /* border: solid 1px black; */
        display: flex;  
        font-family: "playfair display";
        font-size: 25px;
        object-position: 5px 0%;
    }
    .plus {
        color: green;
        margin-right: 5px;
    }
    .minus {
        color: red;
        margin-left: 5px;
        margin-right: 5px;
    }
</style>