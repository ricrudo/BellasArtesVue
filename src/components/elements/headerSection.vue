<script setup>
	defineProps({
		title: {
		type: String,
		required: false
		},
		descriptions: {
		type: Array,
		required: false
		},
		br:{type:Number,
		required:false,
		default:0}
	})
</script>

<template>

	<div>
		<h6 class="sub_section">{{title}}</h6>
		<p class="general-description" v-for="(content, index) in  descriptions" :key="index">{{content}}</p>

		<div class="my-br" v-for="n in br" :key="n"/>

		</div>
</template>

<style scoped>
</style>
