<template>
    <div class="commentContainer">
        <div class="topSection">
            <div class=leftTopSection>
                <div class="userName">
                    {{ userName }}
                </div>
                <div class="rating">
                    {{ rating }}
                </div>
            </div>
            
            <div class="rightTopSection">
                <div class="date">
                    {{ postingDate }}
                </div>
                <div class="likes">
                    <mdicon name="mdiPlusThick"/>
                </div>
            </div>
        </div>
        
        <div class="text">
            {{ commentText }}
        </div>
    </div>
</template>

<script>
    import { mdiPlusThick } from '@mdi/js'; 
    export default {
        name: "comment",
        props: [],
        data(){
            return {
                userName: 'Mateusz Kluba',
                rating: '4.5/5',
                postingDate: '13.09.2021',
                commentText: 'Świetny pomysł! Sam nieraz widzę potrzebę lepszego oświetlenia naszych alejek. Chciałbym jednak znać więcej szczegółów'
            }
        },
        methods:{
            mdiPlusThick
        }
    }
</script>

<style>
    .commentContainer {
        border: solid 1px black;
        border-radius: 25px;
        height: 150px;
        padding: 20px; 
        width: 400px;
    }
    .topSection {
        display: flex;
        margin-bottom: 20px;
    }
    .leftTopSection {
        flex: 50%;
    }
    .rightTopSection {
        flex: 50%;
        text-align: right;
    }
    .userName {
        margin-bottom: 5px;
    }
    .date {
        
    }
</style>