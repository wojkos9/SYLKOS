import Vue from "vue"
import Router from "vue-router"
import MainScreen from './screens/MainScreen.vue'
import GroupsScreen from './screens/groupsScreen'

Vue.use(Router)

export default new Router({
    mode:"history",
    routes:[
        {
            path:"",
            name:"main",
            component: MainScreen
        },
        {
            path:"/groups",
            name:"groups",
            component:GroupsScreen
        }
    ]
})