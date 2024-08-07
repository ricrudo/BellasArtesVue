<script setup>
  import {ref} from 'vue'

  const props = defineProps({
    id_name:{
      type:String,
      required:true 
    },
    label:{
      type:String,
      required:true 
    },
    value:{
      type:String,
      required:true 
    },
    add_info:{
      type:String,
      required:true 
    },
    isRequired:{
      type:Boolean,
      default:false
    },
    stackClass:{
      type:Boolean,
      default:false
    },
    popupText: {
      type:String,
      required:false,
      default:""
    }
  })

  const popupState = ref(false)
  const value = ref(props.value)

  function popupToggleShow() {
    popupState.value = !popupState.value
  }

</script>

<template>
  <div class="form-item" :class="{stack:stackClass}">
    <label :for="id_name">
      <h3 class="label">
	{{label}}
      <span
        v-if="popupText !== ''"
        class="info-icon"
        @click="popupToggleShow">
        ℹ️
      </span>
    </h3>
    </label>
    <input 
      type="date" 
      :id="id_name" 
      :name="id_name" 
      class="input-text" 
      v-model="value" 
      :required="isRequired"
      >
    <div class="item-add-info">
    <h5></h5>
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

<style scoped>
</style>
