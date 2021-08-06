<template>
  <div  class="area">
    <div class="nextTo">
        <div class="about">
            <div class="title">siatkówka plażowa</div>
            <div class="desc">Boisko do siatkówki plażowej w miejscu obecnego kamienistego placu przy ulicy Maja</div>
        </div>
        <div class="rightSection">
          <div class="button">
            <img src="https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg" class="image" />
          </div>
          <div class="button"><div :style="text">{{getString('userPanel', 'details')}}</div></div>  
        </div>
    </div>
  </div>
</template>

<script>
import {getString} from '@/language/string.js'
import {getColor} from '@/colors.js'
export default({
    name:"myProject",
    methods: {
      getString,
      getColor
    },
    computed:{
      text(){
      return{
        alignSelf: "center",
        backgroundColor: this.getColor('navbar'),
        borderRadius: "10px",
        height: "25px",
        marginTop: "2%",
        paddingTop: "3px",
        textAlign: "center",
        width: "80%",
      }
    },
    }
})
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    .area {
        background-color: white;
        height: 170px;
        width: 600px;
        border: solid 1px black
    }
    .nextTo{
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
    }
    .title{
      font-weight: 500;
      font-size: 26px;
      margin-bottom: 7%;
      margin-top: 2%;
      font-family: 'Playfair Display', serif;
    }
    .desc{
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      font-weight: 400;
    }
    .about{
      width: 60%;
      padding: 2%;
    }
    .rightSection{
      width: 34%;
      margin-top: 2%;
      margin-right: 2%;
      /* display: flex; */
      align-items: center;
      justify-content: center;
      align-self: center;
    }
    .button{
      display: flex;
      justify-content: center;
      align-items: center;
      /* border: 3px solid green; */
      margin-bottom: 2%;
      align-content: center;
    }
    .text{
      height: 25px;
      text-align: center;
      width: 80%;
      align-self: center;
      background-color: cornflowerblue;
      border-radius: 10px;
      padding-top: 3px;
      margin-top: 10px;
    }
    .image{
      width: 95%;
    }

</style>
