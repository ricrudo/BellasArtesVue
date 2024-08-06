<script setup>

	import {addElement} from '@/utils/utils.js'
  import {ref} from 'vue'

  const props = defineProps({
  text: {
    type: String,
    required: false,
    default: ''
  },
  classes: {
    type: String,
    required: false,
    default: 'add-card-button'
 },
 entries: {
    type:Object,
    required: true 
    },
 keyword: {
    type:String,
    required: true 
    }
})
  const entries = ref(props.entries);
  const keyword = ref(props.keyword);

  function addOtherElement() {
    console.log(entries.value);
    addElement(entries.value,keyword.value)

    console.log(entries.value);
  }
</script>

<template>

  <!--<button class="add-card-button" type="button" onclick="addCard(event, this)">-->
  <div 
    class="button-ROD no-select" 
    :class="classes"
    @click="addOtherElement"
    >
    {{text}}
  </div>
</template>

<style scope>
.button-ROD {
  cursor: pointer;
  font-size:13.333333px;
}

  .classesAddButton-ROD{
    display: inline-block;
  }
</style>
