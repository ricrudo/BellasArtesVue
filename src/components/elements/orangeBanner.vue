<script setup>

  defineProps({
  text:{type:String,
  required:true}
})

</script>

<template>
  <div class="contenedor_sections_menu">
    <div class="cont-opt-sections bg-orange">
      <p class="opt-sections-text">{{text}}</p>
    </div>
  </div>
</template>


<style scoped>
</style>

