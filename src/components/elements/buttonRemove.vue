<script setup>
	defineProps ({
		text:{type:String,
		required:false,
		default:"Borrar"}
	})
</script>

<template>
	<div class="delete-button button-ROD no-select">
		<i class="fas fa-trash-alt"></i> {{text}}
	</div>
</template>

<style scoped>
.button-ROD {
	cursor: pointer;
	font-size:13.333333px;
}
</style>
