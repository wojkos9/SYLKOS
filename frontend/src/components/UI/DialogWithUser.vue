<template>
    <v-dialog
      v-model="dialog"
      width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="text-h4">{{ title }}<span v-show="title">!!</span></span>
        </v-card-title>
        <v-card-text style="flex-direction: column">
          <span style="font-size: 20px">{{desc}}</span><br> <br>
           <div v-for="(obj, index) in object" :key="index">
             <b>{{obj.label}}</b> {{obj.value}}
           </div>
          
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="nextAction"
          >
             <span v-if="yes">{{yes}}</span><span v-else>{{$t("next")}}</span>
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="backAction"
          >
              <span v-if="no">{{no}}</span><span v-else>{{$t("back")}}</span>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default ({
    name: "DialogWithUser",
    props: ["title", "desc", "object", "nextAction", "backAction", "dialog", "yes", "no"],
    data() {
        return {
             
        }
    },
    methods: {
    }, 
    computed(){
    } 
})
</script>

