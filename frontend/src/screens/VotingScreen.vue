<template>
  <div>
    <div v-if="!response">
      <div class="votingTitle" style="text-transform: touppercase">
        404 - NOT FOUND
      </div>
    </div>
    <div v-else>
      <div class="votingTitle">
        <div v-if="response">
          <div v-if="voting.status == 'finished'">
            {{ $t("votingScreen.ended") }}
          </div>
          <div v-else-if="voting.status == 'active'">
            {{ $t("votingScreen.voting") }}
          </div>
          <div v-else>
            {{ $t("votingScreen.votingNewProjects") }}
          </div>
          {{ voting.name }}
          <div>
            {{ $t("votingScreen.startDate") }}:
            {{ voting.start_date.slice(0, 10) }}
          </div>
          <div>
            {{ $t("votingScreen.endDate") }}: {{ voting.end_date.slice(0, 10) }}
          </div>
        </div>
        <div v-else style="text-transform: touppercase">404 - NOT FOUND</div>
      </div>
      <div v-if="voting.status == 'finished'">
        <div v-if="voting.voting_type != 'borda'">
          <div v-for="(project, index) in projectsVotes" :key="index">
            <VotingProjectSelectOne
              v-bind:project="project"
              v-on:change="setUserVotedFor($event)"
              :ifUserCanVote="!alreadyVoted"
              :myChoice="alreadyVoted"
            />
          </div>
        </div>
        <div v-else style="margin-top: 20px;">
           <div v-for="project in voting.projects" :key="project.id">
              <VotingProject v-bind:project="project" :showPoints="show" />
            </div>
        </div>
      </div>
      <div v-else-if="voting.status == 'active'">
        <!--{{response}}-->
        <div v-if="alreadyVoted" class="alreadyVotedSection">
          <div v-if="voting.voting_type == 'majority'">
            <div class="alreadyVotedSelectedProject">
              {{ $t("votingScreen.projectYouVotedFor") }}
            </div>
            <VotingProjectSelectOne
              v-bind:project="myChoice"
              v-on:change="setUserVotedFor($event)"
              :ifUserCanVote="!alreadyVoted"
              :myChoice="alreadyVoted"
            />

            <div class="alreadyVotedSelectedProject">
              {{ $t("votingScreen.restOfProjects") }}
            </div>
            <div v-for="project in voting.projects" :key="project.id">
              <div v-show="project.id != myChoice.id">
                <VotingProjectSelectOne
                  v-bind:project="project"
                  v-on:change="setUserVotedFor($event)"
                  :ifUserCanVote="!alreadyVoted"
                  :myChoice="!alreadyVoted"
                />
              </div>
            </div>
          </div>

          <div v-else-if="voting.voting_type == 'borda'">
            <div class="alreadyVotedSelectedProject">
              {{ $t("votingScreen.projectsQueue") }}
            </div>
            <div v-for="project in myBordaChoice" :key="project.id">
              <VotingProject
                v-bind:project="project"
                v-on:change="setUserVotedFor($event)"
              />
            </div>
          </div>

          <div v-else-if="voting.voting_type == 'approval'">
            <div class="alreadyVotedSelectedProject">
              {{ $t("votingScreen.projectsYouVotedFor") }}
            </div>
            <div v-for="project in myApprovalChoice" :key="project.id">
              <div v-show="project.id != myChoice.id">
                <VotingProjectSelectOne
                  v-bind:project="project"
                  v-on:change="setUserVotedFor($event)"
                  :ifUserCanVote="!alreadyVoted"
                  :myChoice="true"
                />
              </div>
            </div>
            <div class="alreadyVotedSelectedProject">
              {{ $t("votingScreen.restOfProjects") }}
            </div>
            <div v-for="project in notMyApprovalChoice" :key="project.id">
              <VotingProjectSelectOne
                v-bind:project="project"
                v-on:change="setUserVotedFor($event)"
                :ifUserCanVote="!alreadyVoted"
                :myChoice="!alreadyVoted"
              />
            </div>
          </div>
        </div>
        <!--borda-->
        <div v-else>
          <div v-if="voting.voting_type == 'borda'">
            <div class="voting_type_desc">
              {{ $t("votingScreen.bordaRules") }}
            </div>
            <div class="draggable">
              <draggable
                v-model="voting.projects"
                group="votings"
                @start="drag = true"
                @end="drag = false"
              >
                <div v-for="project in voting.projects" :key="project.id">
                  <VotingProject v-bind:project="project" />
                </div>
              </draggable>
            </div>
          </div>
          <!--majority-->
          <div v-else-if="voting.voting_type == 'majority'">
            <div class="voting_type_desc">
              {{ $t("votingScreen.majorityRules") }}
            </div>
            <div v-for="project in voting.projects" :key="project.id">
              <VotingProjectSelectOne
                v-bind:project="project"
                v-on:change="setUserVotedFor($event)"
                :clicked="userVotedFor == project.id"
                :ifUserCanVote="!alreadyVoted"
              />
            </div>
          </div>
          <div v-else-if="voting.voting_type == 'approval'">
            <div class="voting_type_desc">
              {{ $t("votingScreen.approvalRules") }}
            </div>
            <div v-for="(project, index) in voting.projects" :key="index">
              <VotingProjectSelectOne
                v-bind:project="project"
                v-on:change="setUserVotedForApproval(index)"
                :clicked="approval[index]"
                :ifUserCanVote="!alreadyVoted"
                :key="changeKey"
              />
            </div>
          </div>
          <div v-else-if="response">
            {{ $t("votingScreen.newType") }}
            {{ voting.voting_type }}
          </div>
          <!--jeden wybor-->

          <!-- <div class="submitButton" @click="submitVote">
    
    </div> -->
          <div class="buttonSubmit" v-if="response">
            <v-btn
              color="accent"
              class="p-3"
              style="color: black"
              @click="dialogSubmitVote = true"
            >
              {{ $t("buttonSubmitVote.submitMyVote").toUpperCase() }}
            </v-btn>
          </div>
        </div>
      </div>

      <div v-else-if="voting.status == 'announced'">
        <router-link
          :to="{
            name: routes.addProject,
            params: { groupId: voting.group, votingId: voting.id },
          }"
        >
          <div class="add-project-icon">
            <v-btn color="accent" width="90px" height="90px" small fab>
              <v-icon style="text-decoration: none" color="primary" x-large
                >mdi-plus</v-icon
              >
            </v-btn>
          </div>
        </router-link>

        <div class="alreadyVotedSelectedProject">
          {{ $t("votingScreen.alProjects") }}
        </div>

        <div v-for="(project, index) in projectsVotes" :key="index">
          <VotingProjectSelectOne
            v-bind:project="project"
            v-on:change="setUserVotedFor($event)"
            :ifUserCanVote="!alreadyVoted"
            :myChoice="alreadyVoted"
          />
        </div>
      </div>

      <v-dialog
        v-model="dialogSubmitVote"
        width="500"
        class="secondary lighten-3"
      >
        <v-card>
          <v-card-title>
            <span class="text-h4">{{ $t("votingScreen.attention") }}!!</span>
          </v-card-title>
          <v-card-text>
            {{ $t("votingScreen.warningTitle") }}
            <br />
            {{ $t("votingScreen.warningDesc") }}
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="dialogSubmitVote = false">
              {{ $t("cancel") }}
            </v-btn>
            <v-btn text @click="submitVote">
              {{ $t("votingScreen.confirm") }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
// import VotingHeader from "../components/voting/VotingHeader.vue";
import VotingProject from "../components/voting/VotingProject.vue";
import VotingProjectSelectOne from "../components/voting/VotingProjectSelectOne.vue";
import { apiService } from "@/common/api.service.js";
import draggable from "vuedraggable";

export default {
  name: "votingScreen",
  props: {
    id: {
      required: true,
    },
    vId: {
      required: true,
    },
  },

  data() {
    return {
      active: true,
      previousUserVote: 0,
      userVotedFor: 0,
      voting: {},
      alreadyVoted: false,
      show: true,
      myChoice: {},
      myBordaChoice: [],
      myApprovalChoice: [],
      notMyApprovalChoice: [],
      dialogSubmitVote: false,
      approval: [],
      changeKey: true,
      response: {},
      projectsVotes: {},
      routes: {
        addProject: "projectNew",
      },
    };
  },
  methods: {
    async submitVote() {
      var choice = [];
      this.dialogSubmitVote = false;

      if (this.voting.voting_type == "majority") {
        for (var project of this.voting.projects) {
          if (project.id == this.userVotedFor)
            choice.push({ project: project.id, points: 1 });
          else {
            choice.push({ project: project.id, points: 0 });
          }
        }
      } else if (this.voting.voting_type == "borda") {
        var points = this.voting.projects.length - 1;
        for (project of this.voting.projects) {
          choice.push({ project: project.id, points: points });
          points -= 1;
        }
      } else if (this.voting.voting_type == "approval") {
        for (var projectId in this.voting.projects) {
          choice.push({
            project: this.voting.projects[projectId].id,
            points: this.approval[projectId] == true ? 1 : 0,
          });
        }
      }

      console.log(choice);
      await apiService("/api/vote/", "POST", {
        voting: this.voting.id,
        choice: choice,
      }).then((data) => {
        if (data != "wrong data") {
          console.log("tak");
        }
      });
      await this.refreshVotingStatus();
    },
    setUserVotedForApproval(index) {
      this.approval[index] = !this.approval[index];
      this.changeKey = this.changeKey == true ? false : true;
    },
    setUserVotedFor(projectId) {
      if (this.previousUserVote == 0) this.previousUserVote = projectId;
      else this.previousUserVote = this.userVotedFor;
      this.userVotedFor = projectId;
    },
    async refreshVotingStatus() {
      let endpoint = `/api/voting/${this.voting.id}/`;
      let data = await apiService(endpoint);
      this.voting = data;
      this.myChoice = {};
      this.alreadyVoted = data.users_votes.length > 0 ? true : false;
      if (this.alreadyVoted && data.voting_type == "majority") {
        for (var project of data.projects) {
          for (var projectVoted of data.users_votes) {
            if (
              project.id == projectVoted.project &&
              projectVoted.points == 1
            ) {
              this.myChoice = project;
              break;
            }
          }
        }
      } else if (this.alreadyVoted && data.voting_type == "borda") {
        var sortedValues = data.users_votes.sort(function (a, b) {
          return -(a.points - b.points);
        });
        var projects = data.projects;
        this.myBordaChoice = [];
        for (var project1 of sortedValues) {
          for (var project2 of projects) {
            if (project1.project == project2.id) {
              this.myBordaChoice.push(project2);
              break;
            }
          }
        }
        // for (var i in data.projects) {
        //   vm.myChoice.append( )
        // }
      } else if (this.voting.voting_type == "approval") {
        var sortedValues2 = data.users_votes.sort(function (a, b) {
          return a.project - b.project;
        });

        var projects2 = data.projects;
        this.myApprovalChoice = [];
        this.notMyApprovalChoice = [];

        for (var projectIndex in sortedValues2) {
          if (sortedValues2[projectIndex].points == 1) {
            this.myApprovalChoice.push(projects2[projectIndex]);
          } else {
            this.notMyApprovalChoice.push(projects2[projectIndex]);
          }
        }
      }
    },
  },
  components: {
    VotingProjectSelectOne,
    VotingProject,
    draggable,
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/voting/${to.params.vId}/`;
    let data = await apiService(endpoint);

    return next((vm) => {
      vm.response = data;

      if (data) {
        vm.voting = data;
        vm.projectsVotes = data.projects.sort(function (a, b) {
          return -(a.votes - b.votes);
        });
        vm.alreadyVoted = data.users_votes.length > 0 ? true : false;
        if (vm.alreadyVoted && data.voting_type == "majority") {
          for (var project of data.projects) {
            for (var projectVoted of data.users_votes) {
              if (
                project.id == projectVoted.project &&
                projectVoted.points == 1
              ) {
                vm.myChoice = project;
                break;
              }
            }
          }
        } else if (vm.alreadyVoted && data.voting_type == "borda") {
          // vm.myChoice = "cos tam "
          var sortedValues = data.users_votes.sort(function (a, b) {
            return -(a.points - b.points);
          });
          var projects = data.projects;
          for (var project1 of sortedValues) {
            for (var project2 of projects) {
              console.log(project1.project, " ", project2.id);
              if (project1.project == project2.id) {
                vm.myBordaChoice.push(project2);
                break;
              }
            }
          }
        } else if (vm.voting.voting_type == "approval") {
          var sortedValues2 = data.users_votes.sort(function (a, b) {
            return a.project - b.project;
          });

          var projects2 = data.projects;
          vm.myApprovalChoice = [];
          vm.notMyApprovalChoice = [];

          for (var projectIndex in sortedValues2) {
            if (sortedValues2[projectIndex].points == 1) {
              vm.myApprovalChoice.push(projects2[projectIndex]);
            } else {
              vm.notMyApprovalChoice.push(projects2[projectIndex]);
            }
          }
        }
        vm.approval = new Array(data.projects.length).fill(false);
      }
    });
  },
};
</script>

<style scoped>
.projects {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
}

.votingTitle {
  margin-top: 50px;
  font-size: 24px;
  text-align: center;
  margin-bottom: 30px;
  font-family: "Petrona";
}

.add-project-icon {
  margin: 20px auto;
  text-align: center;
  max-width: 90px;
  transition: all 0.5s ease;
}
.add-project-icon:hover {
  transform: scale(1.2);
}

.draggable {
  max-width: 1000px;
  margin: 0 auto;
  /* border: solid; */
}
.buttonSubmit {
  display: flex;
  justify-content: flex-end;
  margin: 50px 10% 50px auto;
}

.voting_type_desc {
  max-width: 700px;
  text-align: center;
  font-size: 20px;
  line-height: 1.3;
  margin: 1em auto;
}

.alreadyVoted {
  max-width: 800px;
  background-color: var(--v-primary-lighten1);
  margin: 50px auto;
  padding: 50px;
}

.alreadyVotedSection {
  margin-bottom: 100px;
}

.alreadyVotedSelectedProject {
  max-width: 800px;
  margin: 50px auto 0 auto;
  font-size: 2em;
  border-bottom: 1px solid var(--v-link-base);
}

@media only screen and (max-width: 800px) {
  .votingTitle,
  .alreadyVotedSelectedProject {
    font-size: 20px;
    padding: 0 10px;
    text-align: center;
  }
}
</style>
