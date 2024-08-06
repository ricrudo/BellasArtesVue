<script setup>
  import { ref, watch, shallowRef } from 'vue' 
  import Question_2 from '@comp/section2/Q2_1.vue'
  import Question_4_1 from '@comp/section4/Q_4_1/Q_4_1.vue'
  import Question_4_2 from '@comp/section4/Q_4_2/Q_4_2.vue'
  import Question_4_3 from '@comp/section4/Q_4_3/Q_4_3.vue'
  import Question_4_4 from '@comp/section4/Q_4_4/Q_4_4.vue'
  import Question_4_5 from '@comp/section4/Q_4_5/Q_4_5.vue'
  import Question_4_6 from '@comp/section4/Q_4_6/Q_4_6.vue'
  import Question_4_7 from '@comp/section4/Q_4_7/Q_4_7.vue'
  import Question_4_8 from '@comp/section4/Q_4_8/Q_4_8.vue'
  import Question_4_9 from '@comp/section4/Q_4_9/Q_4_9.vue'
  import Question_4_10 from '@comp/section4/Q_4_10/Q_4_10.vue'
  import Question_4_11 from '@comp/section4/Q_4_11/Q_4_11.vue'
  import Question_4_12 from '@comp/section4/Q_4_12/Q_4_12.vue'
  import Question_4_13 from '@comp/section4/Q_4_13/Q_4_13.vue'
  import Question_4_14 from '@comp/section4/Q_4_14/Q_4_14.vue'
  import Question_4_15 from '@comp/section4/Q_4_15/Q_4_15.vue'
  import Question_4_16 from '@comp/section4/Q_4_16/Q_4_16.vue'
  import Question_4_17 from '@comp/section4/Q_4_17/Q_4_17.vue'

  const props = defineProps ({
  question:{
    type:String,
    required:true
  }
  })

  const preguntas = {
  Question_2,
  Question_4_1,
  Question_4_2,
  Question_4_3,
  Question_4_4,
  Question_4_5,
  Question_4_6,
  Question_4_7,
  Question_4_8,
  Question_4_9,
  Question_4_10,
  Question_4_11,
  Question_4_12,
  Question_4_13,
  Question_4_14,
  Question_4_15,
  Question_4_16,
  Question_4_17
  }

// dejo este codigo por si es el que necesito para pasar datos hacia hijos
//const currentQuestion = ref(null)

const currentQuestion = shallowRef(props.question)

// este codigo supuestamente lo hace reactivo a los cambios, pero aun no se prueba y puede que sea innecesario
watch(() => props.question, (newQuestion) => {
  currentQuestion.value = preguntas[newQuestion]
}, { immediate: true })


</script>

<template>
  <component :is="currentQuestion"></component>
</template>

<style scope>
</style>

