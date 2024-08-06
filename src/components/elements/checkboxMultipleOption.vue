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
		}
  })

  const options = ref(props.options)

</script>

<template>
  <div class="form-item" :class="{stack:stackClass}">
    <h3 class="label">{{label}}</h3>
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
  </div>
</template>

<style scoped>
</style>
