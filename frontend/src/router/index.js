import Vue from "vue"
import Router from "vue-router"
import MainScreen from '../screens/MainScreen.vue'
import GroupsScreen from '../screens/GroupsScreen'
import ProjectsScreen from '../screens/ProjectsScreen'
import ProjectScreen from '../screens/ProjectScreen'
import GroupScreen from '../screens/GroupScreen'
import VotingScreen from '../screens/VotingScreen'

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
        path:"/groups/:id",
        name:"group",
        component:GroupScreen,
        props: true
    },
    {
        path:"/groups/:id/voting/:vId",
        name:"voting",
        component:VotingScreen,
        props: true
    },
    {
        path:"/projects",
        name:"projects",
        component:ProjectsScreen
    },
    {
        path:"/project/:id",
        name:"project",
        component:ProjectScreen,
        props: true
    }
]
