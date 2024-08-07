<script setup>
	import { ref } from 'vue'

  const props = defineProps({
  radioID:{
    type:String,
    required:true
    }
  })

  const selectedValue = ref('')
  const emit = defineEmits(['update'])

  function emitSelection() {
    emit('update', selectedValue.value)
  }
</script>

<template>

	<div class='sub_section_question'>
		<p class="font-size-14">
		</p>
		<div class="radio-btns-cont">
			<div>
				<input type="radio" :name="radioID" value="si" v-model="selectedValue" @change="emitSelection"> Si
			</div>
			<div>
				<input type="radio" :name="radioID" value="no" v-model="selectedValue" @change="emitSelection"> No
			</div>
		</div>
	</div>

</template>

<style scope>
</style>


