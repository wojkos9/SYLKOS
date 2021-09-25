 <template>
 <v-navigation-drawer
      v-model="showSideMenu"
      absolute
      bottom
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
import { getString } from "@/language/string.js";
import { getColor } from "@/colors.js";

export default {
  name: "App",
  props: ["showSideMenu"],
  data() {
    return {
      projects: false,
      groups: false,
      addProject: false,
      group: "",
      routes: {
        addProject: "projectNew",
        projects: "projects",
        groups: "groups",
        mainPage: "main",
      },
    };
  },
  methods: {
    getString,
    getColor,
    isProjectsClicked() {
      this.projects = true;
      this.groups = false;
      this.addProject = false;
    },
    groupsClicked() {
      this.projects = false;
      this.groups = true;
      this.addProject = false;
    },
    newProjectClicked() {
      this.projects = false;
      this.groups = false;
      this.addProject = true;
    },
    settingsClicked() {
      this.projects = false;
      this.groups = false;
      this.addProject = false;
    },
    userPanelClicked() {
      this.projects = false;
      this.groups = false;
      this.addProject = false;
    },
  },
  computed: {
    isiconChecked() {
      return {
        border: 3,
      };
    },
  },
 
};
</script>

<style>
.logo {
  width: 100px;
  height: 50px;
}

</style>
