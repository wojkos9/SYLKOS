<template>
    <div>
        <form>
            <md-card>
                <md-card-header>
                    <div class="md-title">{{ getString('projectRegistration','title') }}</div>
                </md-card-header>
                <md-card-content>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-small-size-100">
                            <md-field>
                                <label for="first-name">First Name</label>
                                <md-input name="first-name" id="first-name" autocomplete="given-name" v-model="form.firstName"/>
                            </md-field>
                        </div>
                    </div>
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

</style>