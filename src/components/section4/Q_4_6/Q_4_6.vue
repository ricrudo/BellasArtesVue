<script setup>

  import {ref} from 'vue'
  import OrangeBanner from '@comp/elements/orangeBanner.vue'
  import HeaderSection from '@comp/elements/headerSection.vue'
  import radioYesNoGeneral from '@comp/elements/radioYesNoGeneral.vue'
  import SystemCard_A from '@comp/section4/Q_4_6/system_card_A.vue'
  import ButtonAddElement from '@comp/elements/buttonAddElement.vue'

  const showQuestion = ref(false)

  function handleRadio(value) {
    showQuestion.value = value === 'si' 
  }
</script>

<template>
  <OrangeBanner
      text="4. FUNCIONES MISIONALES DE INVESTIGACIÓN"
      />

  <form method="POST">
    <div class='form-area '>

      <HeaderSection
          title="4.6 LIBROS Y /O CAPITULOS DE LIBRO PUBLICADOS RESULTADO DE INVESTIGACIÓN CREACIÓN"
          :descriptions="[
                         'Indica si tienes capítulos o libros publicados (durante este periodo) resultado de investigación creación utilizando el botón “Añadir”'
                         ]"/>


      <!-- RADIO BUTTON YES NO-->
      <radioYesNoGeneral
          @update="handleRadio"
          radioID="bool_publicaciones_libros"
          />


      <SystemCard_A v-if="showQuestion"/>

      <ButtonAddElement
          v-if="showQuestion"
          text="Añdir libro o capítulo"
          @click="addCard"
          />


    </div>

    <!-- Botones de navegación -->
    <div class="form-control-btns-area">
      <div class="cont-atras-sig-btns">
        <button type="submit" name="action" value="back" class="btn-atras btn-general">
          atrás
        </button>
        <button type="submit" name="action" value="next" class="btn-siguiente btn-general">
          siguiente
        </button>
      </div>
    </div>
  </form>
</template>

<style scoped>
</style>


<style scoped>
</style>
