import Vue from "vue"
import Router from "vue-router"
import MainScreen from '../screens/MainScreen.vue'
import GroupsScreen from '../screens/GroupsScreen'
import ProjectsScreen from '../screens/ProjectsScreen'

Vue.use(Router)

export const routes = [{
        path:"/",
        name:"main",
        component: MainScreen
    },
    {
        path:"/groups",
        name:"groups",
        component:GroupsScreen
    },
    {
        path:"/projects",
        name:"projects",
        component:ProjectsScreen
    }
]
