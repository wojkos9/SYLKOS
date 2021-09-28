<template>
  <div class="container">
    <div class="row area">
      <div class="col-lg-12 col-xl-9">
        <div>
          <div>
            <div class="groupTitle">{{ group.name }}</div>
            <md-icon>person_add</md-icon><span v-if="isUserMember">członek</span><span v-else>dołącz</span>
          </div>
          
          <div class="desc">
            {{ group.description }}
          </div>
          <div class="membersNumber desc">
            {{ getString("groups", "membersNumber") }} {{ group.count_user }}
          </div>
        </div>
      </div>
      <div class="col center">
        <div class="center">
          <div v-if="group.images.length > 0">
              <img  :src="`/media/${group.images[0].image}`" class="image" />
          </div>
          
          <router-link :to="{ name: 'group', params:{id:group.id}}"><div :style="button">Dowiedz się więcej</div></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";
import { apiService } from "@/common/api.service.js";

export default {
  name: "Group",
  props: ["group", "name", "requestUser"],
  data() {
    return {
      loading: true,
      image: "",
    }
  },

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
        padding: "3px",
        fontWeight: "500",
      };
    },
    isUserMember(){
      return this.group.members.includes(this.requestUser)
    }
  },
  components: {},
  async created(){
    if(this.group.image)
      await apiService(`/api/photo/${this.group.image}/`).then((data) => {
          this.image = data.image;
          this.loading = false
        });
  }

};
</script>

<style scoped>
.area {
  background-color: white;
  border: solid 1px black;
  margin-bottom: 30px;
  margin-top: 10px;
  padding: 10px;
}

.groupTitle {
  font-weight: 700;
  font-size: 1.5rem;
  margin-bottom: 40px;
  margin-top: 20px;
  text-align: center;
}

.desc {
  font-size: 1rem;
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
    font-size: 0.875rem;
  }
  .title {
    font-size: 1.125rem;
  }
  .myButton {
    width: 300px;
  }
}
</style>
