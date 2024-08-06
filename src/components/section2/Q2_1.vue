<script setup>
  import {ref} from 'vue'
  import OrangeBanner from '@comp/elements/orangeBanner.vue'
  import HeaderSection from '@comp/elements/headerSection.vue'
  import SystemCard from  '@comp/section2/system_card_2_1.vue'
  import ButtonAddElement from '@comp/elements/buttonAddElement.vue'
  import UserCard from '@comp/section2/user_add_card.vue'

  const userCards = ref([])

  function addCard() {
    const maxID = getHighestId();
    const newCard = {id:maxID.toString()};
    userCards.value.push(newCard);
  }

function getHighestId(){
  let maxID = 0;
  userCards.value.forEach(card => {
    const idNumber = Number(card.id);
    if (idNumber > maxID) {
      maxID = idNumber;
    }
  })
  return maxID + 1
  };

function removeUserCard(cardID) {
userCards.value = userCards.value.filter(card => card.id !== cardID);
}


</script>


<template>

  <OrangeBanner
    text="2. FUNCIÓN MISIONAL DE DOCENCIA"
  />

  <form method="POST">
    <div class='form-area '>

      <HeaderSection
      title="2.1 asignaturas en el PTA"
      :descriptions="[
      'A continuación, encontrarás las asignaturas que aparecen en tu Programa de Trabajo Académico (PTA).', 
      'En caso de tener asignaturas adicionales que no figuran en el listado, las podrás añadir manualmente en la sección 2.2'
      ]"/>



      <SystemCard/>
      <SystemCard/>

      <!-- Form Break -->
      <div class="form-break"></div>


      <HeaderSection
      title="2.2 ASIGNATURAS ADICIONALES AL PTA"
      :descriptions="[
      'Si tienes asignaturas adicionales que no están incluidas en el Plan de Trabajo Académico (PTA), por favor, agrégalas aquí:'
      ]"/>


      <!-- USER ADDED CARDS -->
      <UserCard v-for="card in userCards" :key="card.id" 
        :cardID="card.id"
        @cardID="removeUserCard"
      />

        <ButtonAddElement
        text="+ Añadir asignatura"
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
