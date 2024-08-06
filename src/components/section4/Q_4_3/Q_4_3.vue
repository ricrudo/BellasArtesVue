<script setup>
  import {ref} from 'vue'
  import OrangeBanner from '@comp/elements/orangeBanner.vue'
  import HeaderSection from '@comp/elements/headerSection.vue'
  import radioYesNoGeneral from '@comp/elements/radioYesNoGeneral.vue'
  import SystemCard_A from '@comp/section4/Q_4_3/system_card_A.vue'
  import ButtonAddElement from '@comp/elements/buttonAddElement.vue'


  const showQuestion = ref(false)
  
  const proyects = ref({
    1:{
      id_name: "Proyecto_1"
    },
    2:{
      id_name: "Proyecto_1"
    }
  })

  function handleRadio(value) {
    showQuestion.value = value === 'si' 
  }

  function addCard(){
    
  }

</script>

<template>
  <OrangeBanner
      text="4. FUNCIONES MISIONALES DE INVESTIGACIÓN"
      />

  <form method="POST">
    <div class='form-area '>

      <HeaderSection
          title="4.3 DESARROLLO DE PROYECTOS DE INVESTIGACIÓN O CREACIÓN"
          :descriptions="[
                         'Indica si tienes proyectos de investigación o creación y relaciónalos utilizando el botón &quot;Añadir&quot;'
                         ]"/>


      <!-- RADIO BUTTON YES NO-->
      <radioYesNoGeneral
          @update="handleRadio"
          />


      <SystemCard_A
          v-if="showQuestion"
          v-for="(value, key, index) in proyects"
          :key="key"
          :clave="key"
          :id_name="value.id_name"
          :index="index"
          />

      <ButtonAddElement
          v-if="showQuestion"
          text="+ Añadir proyecto"
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
