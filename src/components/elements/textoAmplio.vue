<script setup>
	import {ref} from 'vue'

	const props = defineProps({
		id_name:{
			type:String,
			required:false
		},
		label:{
			type: String,
			required: false
		},
		content:{
			type:String,
			required:false
		},
		add_info:{
			type: String,
			required: false
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
		<textarea class="input-text" :id="id_name" :name="id_name" rows="4" required>{{content}}</textarea>
		<div class="item-add-info">
			<h5>
				{{add_info}}
			</h5>
		</div>
	</div>
</template>

<style scoped>
</style>
