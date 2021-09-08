<template>
    <div class="registration">
        <form>
            <md-card>
                <md-card-header>
                    <div class="md-title">{{ getString('projectRegistration','title') }}</div>
                </md-card-header>
                <md-card-content>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-small-size-100">
                            <md-field class="field">
                                <label for="project-name">{{ getString('projectRegistration','projectName') }}</label>
                                <md-input name="project-name" id="project-name" autocomplete="given-name"/>

                            </md-field>
                        </div>
                    </div>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-small-size-100">
                            <md-field class="field">
                                <label for="project-price">{{ getString('projectRegistration','projectPrice') }}</label>
                                <md-input type="number" name="project-price" id="project-price" autocomplete="given-name" min="0"/>
                            </md-field>
                        </div>
                    </div>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-small-size-100">
                            <md-field class="field">
                                <label for="project-description">{{ getString('projectRegistration','projectDescription') }}</label>
                                <md-input name="project-description" id="project-description" autocomplete="given-name"/>
                            </md-field>
                        </div>
                    </div>

                    <md-card-actions>
                        <md-button type="submit" class="md-primary">{{ getString('projectRegistration','submitProject') }}</md-button>
                    </md-card-actions>
                </md-card-content>
            </md-card>

        </form>    
    </div>    
</template>

<script>
    import { getString } from '@/language/string.js';
    export default {
        name: "projectRegistration",
        methods:{
            getString
        }
    }
</script>

<style>
    .registration {
        border: solid 1px black;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 100px;
    }
    .field{
        width: 500px;
    }
</style> 