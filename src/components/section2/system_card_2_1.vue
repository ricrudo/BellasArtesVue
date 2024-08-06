<script setup>
  import { ref } from 'vue'

  import CardHeader from '@comp/elements/cardHeader.vue'
  import RadioYesNoCard from '@comp/elements/radioYesNoCard.vue'
  import TextoAmplio from '@comp/elements/textoAmplio.vue'

  const selected = ref('')
  const show = ref(true)

  function handleToggle() {
    show.value = !show.value
  }

  function handleRadio(value) {
    selected.value = value
  }
</script>


<template>

  <div class="system-added-cards">
    <div class="card-item-container" id="materia_1">

      <CardHeader :title="['Técnicas en composición III']"
       :subtitle="['Código: 0974236','Programa: Música']"
        @click="handleToggle"
       />

      <div class="card-content toggle_show" v-show="show">

        <!-- RADIO BUTTON YES NO-->
        <RadioYesNoCard @update="handleRadio"
          radioID="esteRadio"
           title="Indica si la actividad se llevó a cabo" 
           additional_info="Esto lo inventé"
           />


        <TextoAmplio v-if="selected === 'si'"
                     id_name="TextoAmplioObserva"
                     label="Observaciones sobre el desarrollo de las actividades docentes"
                     content=""
                     additional_info="Esto lo inventé"
                     />


        <TextoAmplio v-if="selected === 'si'"
                     id_name="TextoAmplioContenidos"
                     label="Contenidos que abordan temáticas ciudadanas y de responsabilidad social"
                     content="esto es una prueba"
                     additional_info="Por ejemplo, Objetivos del Milenio, Pacto Global, Carta de la Tierra, Decenio de Naciones Unidas de la Educación para el desarrollo sostenible, Convivencia y paz, Responsabilidad social, Ética profesional y cívica, Democracia y sociedad, Pluralidad identidad y valoración de las diferencias, entre otros."
                     />

        <TextoAmplio v-if="selected === 'no'"
                     id_name="TextoAmplioCancelacion"
                     label="Motivo de cancelación"
                     content=""
                     additional_info="Por ejemplo, estudiantes no matriculados o error en datos sacados del PTA"
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
