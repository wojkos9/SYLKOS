import Vue from "vue"
import Router from "vue-router"
import MainScreen from '../screens/MainScreen.vue'
import GroupsScreen from '../screens/GroupsScreen'
import ProjectsScreen from '../screens/ProjectsScreen'
// import ProjectScreen from '../screens/ProjectScreen'
import GroupScreen from '../screens/GroupScreen'
import VotingScreen from '../screens/VotingScreen'
import PhotoScreen from '../screens/PhotoScreen'
import ProjectRegistrationScreen from '../screens/ProjectRegistrationScreen'
import GroupsFormScreen from '../screens/GroupsFormScreen' 
import VotingsFormScreen from '../screens/VotingsFormScreen' 
import VotingsTypeFormScreen from '../screens/VotingsTypeFormScreen' 
import AdminScreen from '../screens/AdminScreen'
import ProjectFormScreen from '../screens/ProjectFormScreen'
import GroupsEditListScreen from '../screens/editForms/GroupsEditListScreen'
import ProjectsEditListScreen from '../screens/editForms/ProjectsEditListScreen'
import VotingsEditListScreen from '../screens/editForms/VotingsEditListScreen'
import VotingsTypeEditListScreen from '../screens/editForms/VotingsTypeEditListScreen'
import GroupEditFormScreen from '../screens/editForms/GroupEditFormScreen'
import ProjectEditFormScreen from '../screens/editForms/ProjectEditFormScreen'
import VotingEditFormScreen from '../screens/editForms/VotingEditFormScreen'
import VotingTypeEditFormScreen from '../screens/editForms/VotingTypeEditFormScreen'
// import GroupEditFormScreen from '../screens/editForms/GroupEditFormScreen'


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
        path:"/newgroup",
        name:"groupNew",
        component:GroupsFormScreen,
    },
    {
        path:"/editGroup/:id",
        name:"groupEdit",
        component:GroupEditFormScreen,
        props: true
    },
    {
        path:"/editProject/:id",
        name:"projectEdit",
        component:ProjectEditFormScreen,
        props: true
    },
    {
        path:"/editVoting/:id",
        name:"votingEdit",
        component:VotingEditFormScreen,
        props: true
    },
    {
        path:"/editVotingType/:nameId",
        name:"votingTypeEdit",
        component:VotingTypeEditFormScreen,
        props: true
    },
    {
        path:"/newproject",
        name:"projectNew",
        component:ProjectFormScreen,
        props: true
    },
    {
        path:"/newvoting/:groupId",
        name:"votingNew",
        component:VotingsFormScreen,
        props: true

    },
    {
        path:"/newvotingtype",
        name:"votingTypeNew",
        component:VotingsTypeFormScreen,
    },
    {
        path:"/groups/:id/voting/:vId",
        name:"voting",
        component:VotingScreen,
        props: true
    },
    {
        path:"/groups_edit_list",
        name:"groupsEditList",
        component:GroupsEditListScreen,
    },
    {
        path:"/voting_type_edit_list",
        name:"votingTypeEditList",
        component:VotingsTypeEditListScreen,
    },
    {
        path:"/votings_edit_list",
        name:"votingsEditList",
        component:VotingsEditListScreen,
    },
    {
        path:"/projects_edit_list",
        name:"projectsEditList",
        component:ProjectsEditListScreen,
    },
    {
        path:"/admin",
        name:"admin",
        component:AdminScreen
    },
    {
        path:"/projects",
        name:"projects",
        component:ProjectsScreen
    },
    // {
    //     path:"/projects/:id",
    //     name:"project",
    //     component:ProjectScreen,
    //     props: true
    // },
    {
        path:"/photo",
        name:"photo",
        component:PhotoScreen,
        props: true
    },
    {
        path:"/registerProject",
        name:"registerProject",
        component:ProjectRegistrationScreen,  
    }
]
