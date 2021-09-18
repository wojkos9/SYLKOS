<template>
    <v-dialog
      v-model="dialog"
      width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="text-h4">{{ title }}!!</span>
        </v-card-title>
        <v-card-text>
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
             {{getString("votingTypeForm", "next")}}
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="backAction"
          >
             {{getString("votingTypeForm", "back")}}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import { getString } from "@/language/string.js";
export default ({
    name: "DialogWithUser",
    props: ["title", "desc", "object", "nextAction", "backAction", "dialog"],
    data() {
        return {
             
        }
    },
    methods: {
      getString
    }, 
    computed(){
      console.log(this.object)
    } 
})
</script>

