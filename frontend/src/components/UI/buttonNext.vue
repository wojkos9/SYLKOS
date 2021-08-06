<template>
    <div :style="button">
        <div>{{getString('userPanel', 'more').toUpperCase()}}</div>
    </div>    
</template>

<script>
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'

export default {
  name:"buttonNext",
  methods: {
    getString,
    getColor
  },
  computed:{
    button(){
      return{
          marginRight: "100px",
          borderRadius: "5px",
          width: "100px",
          height: "30px",
          display:"flex",
          flexDirection: "row",
          alignItems:"center",
          justifyContent: "center",
          alignSelf:"flexEnd",
          fontSize: "12px",
          backgroundColor: getColor('white')
      }
    }
  }
}
</script>

<style scoped>

</style>