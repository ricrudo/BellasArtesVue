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
    }
  })
  
  const value = ref(props.value)

</script>

<template>
  <div class="form-item" :class="{stack:stackClass}">
    <label :for="id_name">
      <h3 class="label">
	{{label}}
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
  </div>

</template>

<style scoped>
</style>
