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
    },
    popupText: {
      type:String,
      required:false,
      default:""
    }
  })

  const content = ref(props.content)
  const popupState = ref(false)

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
