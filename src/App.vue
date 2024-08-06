<script setup>
    import { RouterLink, RouterView } from 'vue-router'
import Header from '@comp/commonSections/Header.vue'
import QuestionRender from '@comp/questionRender.vue'
</script>

<template>
    <div class="main-container">
        <Header/>
            <QuestionRender
                    question="Question_4_3"
                    />
    </div>


    <!--<HelloWorld msg="You did it!" />-->

    <!--<nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        </nav>-->


        <!--<RouterView />-->
</template>

<style scoped>
</style>
