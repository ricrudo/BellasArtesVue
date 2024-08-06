<script setup>

  import { ref } from 'vue'
  import CardHeader from '@comp/elements/cardHeader.vue'
  const show = ref(true)

  function handleToggle() {
    show.value = !show.value
  }

</script>


<template>
  <div class="system-added-cards">
    <div class="card-item-container" id="materia_1">

      <CardHeader
          :title="[
                  'Proyecto 1'
          ]"
          @click="handleToggle"
          />

      <div class="card-content toggle_show" v-show="show">





      </div>
    </div>
  </div>
</template>

<style scoped>
.card-content {
  width: 100%;
}
</style>
