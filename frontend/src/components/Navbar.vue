<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
        <router-link
            :to="{ name: 'home'}"
            class="navbar-brand"
        >Sylkos
        </router-link>
    </div>
    </nav>
</template>

<script>
export default{
    name:"NavbarComponent"
}
</script>

<style>
    .my-navbar{
        border-bottom: 1px solid #DDD ;
    }   
    .navbar-brand{
        font-weight: bold;
        font-size: 130%;
    }

     .navbar-brand:hover{
         color: #DC3545 !important;
     }

</style>