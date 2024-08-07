<script setup>
	import { ref } from 'vue'

  const props = defineProps({
    radioID:{
      type:String,
      required:true
      },
    title:{
      type: String,
      required: false
      },
    additional_info:{
      type: String,
      required: false
      },
    stackClass:{
      type:Boolean,
      default:false
      },
    popupText:{
      type:String,
      required:false,
      default:""
    }
  })

  const popupState = ref(false)
  const selectedValue = ref('')
  const emit = defineEmits(['update'])

  function popupToggleShow() {
    popupState.value = !popupState.value
  }

  function emitSelection() {
    emit('update', selectedValue.value)
  }

</script>

<template>

	<div class='form-item' :class="{stack:stackClass}">
		<label for="status_done_1">
			<h3 class="label">
				{{title}}
			<span
        v-if="popupText !== ''"
        class="info-icon"
        @click="popupToggleShow">
        ℹ️
      </span>
    </h3>
		</label>

		<div class="radio-options">
			<div class="input-radio">
				<input class="radio-text" type="radio" :name="radioID" value="si" v-model="selectedValue" @change="emitSelection"> Si
			</div>
			<div class="input-radio">
				<input class="radio-text" type="radio" :name="radioID" value="no" v-model="selectedValue" @change="emitSelection"> No
			</div>
		</div>

		<div class="item-add-info">
			<h5>
				{{additional_info}}
			</h5>
		</div>

    <div class="popup" v-if="popupText !== ''" v-show="popupState">
      <span
          class="close-btn"
          @click="popupToggleShow">
        &times;
      </span>
      <p>{{popupText}}</p>
    </div>
  </div>

</template>

<style scope>
</style>


