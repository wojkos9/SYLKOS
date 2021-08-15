<template>
  <div class="row area">
    <div class="col-lg-12 col-xl-9 ">
      <div class="about">
        <div class="title">siatkówka plażowa</div>
        <div class="desc">
          Boisko do siatkówki plażowej w miejscu obecnego kamienistego placu
          przy ulicy Maja
        </div>
      </div>
    </div>
    <div class="imageBox">
      <img
        src="https://www.gos.pawlowice.pl/fileadmin/repozytorium/GOS/Galeria/boisko_plaza.jpg"
        class="image"
      />
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "myProject",
  methods: {
    getString,
    getColor,
  },
  computed: {},
  components: {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

.area {
  background-color: white;
  border: 1px solid;
  margin-bottom: 20px;
}
.title {
  font-weight: 500;
  font-size: 22px;
  margin-bottom: 12px;
  margin-top: 3px;
  font-family: "Playfair Display", serif;
}
.desc {
  font-family: "Playfair Display", serif;
  font-size: 16px;
  font-weight: 400;
}

.imageBox {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

.image {
  width: 120px;
  height: 120px;
  object-fit: cover;
  align-self: center;
  justify-content: center;
  justify-self: center;
}

.about {
  padding-bottom: 30px;
  padding-top: 30px;
}

@media only screen and (max-width: 1600px) {
  .image {
    width: 110px;
    height: 110px;
  }
}

@media only screen and (max-width: 1500px) {
  .image {
    width: 100px;
    height: 100px;
  }
}

@media only screen and (max-width: 1400px) {
  .image {
    width: 90px;
    height: 90px;
  }

  .title {
    font-size: 20px;
  }
  .desc {
    font-size: 14px;
  }
}

@media only screen and (max-width: 1200px) {
  .image {
    width: 200px;
    height: 200px;
    padding-bottom: 20px;
  }

  .imageBox {
    width: 100%;
  }

  .title {
    font-size: 18px;
  }
  .desc {
    font-size: 12px;
  }
}
</style>
