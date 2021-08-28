<template>
  <div class="container">
    <div class="row area">
      <div class="col-lg-12 col-xl-9">
        <div>
          <div>
            <div class="groupTitle">{{ name }}</div>
            <md-icon>person_add</md-icon><span v-if="isUserMember">członek</span><span v-else>dołącz</span>
          </div>
          
          <div class="desc">
            {{ desc }}
          </div>
          <div class="membersNumber desc">
            {{ getString("groups", "membersNumber") }} {{ members }}
          </div>
        </div>
      </div>
      <div class="col center">
        <div class="center">
          <img :src="picture" class="image" />
          <router-link :to="{ name: 'group', params:{id:id}}"><div :style="button">Dowiedz się więcej</div></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "Group",
  props: ["name", "desc", "members", "picture", "id", "requestUser", "allMembers"],
  methods: {
    getString,
    getColor,
  },
  computed: {
    button() {
      return {
        backgroundColor: getColor("navbar"),
        width: "160px",
        marginTop: "5px",
        borderRadius: "5px",
        textAlign: "center",
        fontFamily: "Playfair Display",
        padding: "3px",
        fontWeight: "500",
      };
    },
    isUserMember(){
      return this.allMembers.includes(this.requestUser)
    }
  },
  components: {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");
.area {
  background-color: white;
  border: solid 1px black;
  margin-bottom: 30px;
  margin-top: 10px;
  padding: 10px;
}

.groupTitle {
  font-family: "Playfair Display", serif;
  font-weight: 700;
  font-size: 24px;
  margin-bottom: 40px;
  margin-top: 20px;
  text-align: center;
}

.desc {
  font-family: "Playfair Display", serif;
  font-size: 16px;
  font-weight: 400;
  margin-bottom: 10px;
  text-align: justify;
}

.membersNumber {
  margin-top: 30px;
}

.myButton {
  align-items: center;
  display: flex;
  justify-content: center;
}

.image {
  align-self: center;
  border-radius: 5px;
  height: 160px;
  justify-self: center;
  object-fit: cover;
  width: 160px;  
}

.center {
  align-content: center;
  align-items: center;
  justify-content: center;
  justify-items: center;
}

@media only screen and (max-width: 1200px) {
  .image {
    height: 300px;
    margin-bottom: 20px;
    margin-top: 50px;
    width: 300px;
  }
  .center {
    float: none;
    margin: 0 auto;
    width: auto;
  }
  .desc {
    font-size: 14px;
  }
  .title {
    font-size: 18px;
  }
  .myButton {
    width: 300px;
  }
}
</style>
