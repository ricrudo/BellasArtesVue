<script setup>
  import { ref } from 'vue'
  import CardHeader from '@comp/elements/cardHeader.vue'
  import DropdownList from '@comp/elements/dropdownList.vue'
  import InputText from '@comp/elements/inputText.vue'
  import TextoAmplio from '@comp/elements/textoAmplio.vue'
  import ButtonRemove from '@comp/elements/buttonRemove.vue'
  
  const props = defineProps ({
    cardID:{type:String,
    required:true}
  })

  const emit = defineEmits(['cardID'])

  function emitCardID() {
  emit('cardID', props.cardID)
  }

  const show = ref(true)

  function handleToggle(value) {
    show.value = value
  }
</script>

<template>

  <div class="system-added-cards">
    <div class="card-item-container" id="materia_1">

      <CardHeader :title="['Asignatura adicional']"
        @state="handleToggle"
      />

      <div class="card-content toggle_show" v-show="show">


          <DropdownList
              :id_name="cardID"
              :label="'Programa ' + cardID"
              :options="[
                       {'lic': 'Licenciatura en música'},
                       {'musica': 'Música'},
                       {'dram': 'Arte dramático'},
                       {'Danza': 'Danza'},
                       {'plas': 'Artes Plásticas'}
                       ]"
              add_info= "esto lo invente"
              :stackClass="true"
              />

          <InputText
              id_name="esteID"
              label="Nombre de la asignatura"
              content="esto es una prueba"
              add_info= "esto lo invente"
              :stackClass="true"
              />


        <TextoAmplio 
                     id_name="Observaciones_1"
                     label="Observaciones sobre el desarrollo de las actividades docentes"
                     content=""
                     additional_info=""
                     />
        
        <TextoAmplio 
                     id_name="ContenidosEspeciales_1"
                     label="Contenidos que abordan temáticas ciudadanas y de responsabilidad social"
                     content=""
                     additional_info="Por ejemplo, Objetivos del Milenio, Pacto Global, Carta de la Tierra, Decenio de Naciones Unidas de la Educación para el desarrollo sostenible, Convivencia y paz, Responsabilidad social, Ética profesional y cívica, Democracia y sociedad, Pluralidad identidad y valoración de las diferencias, entre otros."
                     />

        <ButtonRemove
        @click="emitCardID"
        text="Borrar"
        />

      </div>
    </div>
  </div>

</template>

<style scoped>
</style>
