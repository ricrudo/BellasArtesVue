<script setup>
	import {ref} from 'vue'
	const props = defineProps({
		id_name:{type:String,
		required:false},
		label:{type:String,
		required:false},
		options:{type:Array,
		required:false},
		add_info:{type:String,
		required:false},
		stackClass:{type:Boolean,
		default:false}
	})

	const stackClass = ref(props.stackClass)
</script>

<template>

	<div class="form-item" :class="{stack:stackClass}">
		<label :for="id_name">
			<h3 class="label">
				{{label}}
			</h3>
		</label>
		<select class='input-text' :name="id_name" :id="id_name" required>

			<option v-for="option in options" :key="Object.keys(option)[0]" :value="Object.keys(option)[0]">
			{{ Object.values(option)[0] }}
			</option>

		</select>
		<div class="item-add-info">
			<h5>
				{{add_info}}
			</h5>
		</div>
	</div>
</template>

<style scoped>
</style>
