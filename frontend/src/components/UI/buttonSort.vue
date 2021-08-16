<template>
    <div>
        <md-list>
            <md-list-item md-expand>
            <span class="md-list-item-text">{{ title }}</span>

            <md-list slot="md-expand">
                <md-list-item class="md-inset" >{{ option1 }}</md-list-item>
                <md-list-item class="md-inset">{{ option2 }}</md-list-item>
                <md-list-item class="md-inset">{{ option3 }}</md-list-item>
                <md-list-item class="md-inset">{{ option4 }}</md-list-item>
            </md-list>
            </md-list-item>
        </md-list>
    </div>
</template>

<script>
    import {getString} from '@/language/string.js';
    export default {
        name: "buttonSort",
        props: ["title", "option1", "option2", "option3", "option4"],
        data(){
            return {
                
            }
        },
        methods: {
            getString
        }
    }
</script>

<style>

</style>