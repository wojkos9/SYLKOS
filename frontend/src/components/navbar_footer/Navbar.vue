<template>
    <nav :style="myNavbar" >
      <img src="@/assets/logo3.png" class="logo" />
      <div :style="button">{{getString('navbar', 'projects').toUpperCase()}}</div>
      <div :style="button">{{getString('navbar', 'groups').toUpperCase()}}</div>
      <div :style="button">{{getString('navbar', 'addProject').toUpperCase()}}</div>

     <div class="rigthSection">
      <div  class="role" v-if="role === 'admin'">{{getString('navbar', 'admin')}}</div>
      <div :style="button">{{getString('navbar', 'account').toUpperCase()}}</div>
     </div> 
    </nav >
</template>

<script>
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
export default{
  name:"NavbarComponent",
  data() {
    return {
      role:"admin",
    }
  },
  methods: {
    getString,
    getColor,
  },
  mounted() {
      console.log(this.color)
  },
  computed: {
    myNavbar(){
      return{
        backgroundColor: this.getColor('navbar'),
        borderBottom: 1, 
        alignContent: "center",
        display: "flex",
        height: "150px",
        borderBottomRightRadius: "40px",
        borderBottomLeftRadius: "40px",
        width: "100%"
      }
    },
    button(){
      return{
        backgroundColor: this.getColor('backgroundcolor'),
        // height:"50%",
        alignSelf: "center",
        borderRadius: "35px",
        marginLeft: "25px",
        padding:"20px",
        paddingLeft: "26px",
        paddingRight: "26px",
        width: "150px",
        textAlign: "center"
        // fontSize: "4px"

      }
    }
  }
  
}
</script>

<style >
   
   @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
   @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100&display=swap');

  .logo{
    margin-left: 10px;
    margin-top:4px;
    margin-bottom: 4px;
    width:200px;
    height: 100px;
    padding-right: 10px;
    align-self:center;
  }
  .rigthSection{
    margin-left: 440px;
    margin-right: 10px;
    /* margin-left: 700px; */
    align-self: center;
    display: flex;
    align-content: center;
    /* font-size: 6px; */
    /* margin-top: 10; */
    /* font-weight: 300; */
  }

  .role{
    font-size: 36px;
    align-self: center;
    font-weight: 300;
  }
    
</style>