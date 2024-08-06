<script setup>
	import {ref} from 'vue'
	const props = defineProps({
		id_name:{
			type:String,
			required:false
		},
		label:{
			type:String,
			required:false
		},
		content:{
			type:String,
			required:false
		},
		add_info:{
			type:String,
			required:false
		},
		isRequired:{
			type:Boolean,
			default:false
		},
		stackClass:{
			type:Boolean,
			default:false
		}
	})

  const content = ref(props.content)
</script>

<template>
	<div class="form-item" :class="{stack:stackClass}">
		<label :for="id_name">
			<h3 class="label">
				{{label}}
			</h3>
		</label>
		<input
				type="text"
				:name="id_name"
				:id="id_name"
				class="input-text"
				v-model="content"
				:required="isRequired"
				>
				<div class="item-add-info">
					<h5>
						{{add_info}}
					</h5>
				</div>

	</div>
</template>

<style scoped>
</style>
