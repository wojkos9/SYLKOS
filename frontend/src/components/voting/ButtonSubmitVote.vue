<template>
    <div :style="button">
        <div>{{ getString('userPanel', 'submitMyVote').toUpperCase() }}</div>
    </div>
</template>

<script>
    import {getString} from '@/language/string.js'
    import {getColor} from '@/colors.js'
    export default {
        name: 'buttonSubmitVote',
        data(){
            return {

            }
        },
        computed:{
          button(){
            return{
                alignItems:"center",
                backgroundColor: getColor('green'),
                borderRadius: "5px",
                color: getColor('white'),
                display: "flex",
                flexDirection: "row",
                justifyContent: "center",
                padding: "20px",
                fontWeight: "700",        
            }
          },  
        },
        methods:{
            getString,
            getColor
        }
    }
</script>

<style scoped>

</style>