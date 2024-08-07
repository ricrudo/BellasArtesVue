<script setup>

  import { ref } from 'vue'
  import CardHeader from '@comp/elements/cardHeader.vue'
  import InputText from '@comp/elements/inputText.vue'
    import DateInput from '@comp/elements/dateInput.vue'
    import MultipleInputText from '@comp/elements/multipleInputText.vue'
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
                  'Libro o capítulo 1'
          ]"
          @click="handleToggle"
          />

      <div class="card-content toggle_show" v-show="show">

          <InputText
            id_name="titulo"
            label="Título del libro y/o capitulo"
            content=""
            add_info= ""
            :isRequired="true"
            :stackClass="true"
          />

          <DateInput
            id_name="fecha"
            label="Fecha de publicación"
            value=""
            add_info=""
            :isRequired="true"
            :stackClass="true"
          />

          <MultipleInputText
            id_name="autores"
            textLabel="Lista los nombres de los autores y autoras con el botón &quot;Añadir&quot;"
            textAddButton="+ Añadir autor/a"
            :isRequired="true"
          />


          <InputText
            id_name="editorial"
            label="Editorial"
            content=""
            add_info= ""
            :isRequired="true"
            :stackClass="true"
          />

          <InputText
            id_name="issn"
            label="ISSN (International Standard Serial Number)"
            content=""
            add_info= ". Ej.: 1234-5678"
            :isRequired="true"
            :stackClass="true"
          />



      </div>
    </div>
  </div>
</template>

<style scoped>
.card-content {
  width: 100%;
}
</style>

