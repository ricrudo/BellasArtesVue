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
    options:{
      type:Array,
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

  const options = ref(props.options)
  const popupState = ref(false)

  function popupToggleShow() {
    popupState.value = !popupState.value
  }

</script>

<template>
  <div class="form-item" :class="{stack:stackClass}">
    <h3 class="label">
      {{label}}
      <span
          v-if="popupText !== ''"
          class="info-icon"
          @click="popupToggleShow">
        ℹ️
      </span>
    </h3>
    <div class="checkbox-group" :id="id_name">
      <label
          v-for="(option, index) in options"
          :key="index"
          class="checkbox-item"
          :for="option.id_name"
          >
          <input
              type="checkbox" 
              :id="option.id_name"
              :name="option.id_name"
              :value="option.text"
              >
              {{option.text}}
      </label>
    </div>
        <div class="item-add-info">
          <h5>{{add_info}}</h5>
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
