<script setup>
  import {ref} from 'vue'

const props = defineProps({
  title: {
    type: Array,
    required: false
  },
  subtitle: {
    type: Array,
    required: false
  },
  state: {
    type:Boolean,
    default: true
  }
})

const emit = defineEmits(['state'])
const state = ref(props.state)


function emitState() {
  state.value = !state.value
  emit('state', state.value)
}
</script>

<template>
  <div class="card-header no-select" :class="{expanded:state}" @click="emitState">

    <h3 class="card-title" v-for="(contentTitle, index) in title" :key="index">
      {{contentTitle}}
    </h3>
    <h3 class="card-subtitle" v-for="(contentSub, index) in subtitle" :key="index">
      {{contentSub}}
    </h3>
  </div>
</template>

<style scope>
</style>

