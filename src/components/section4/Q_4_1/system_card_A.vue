<script setup>

  import { ref } from 'vue'
  import CardHeader from '@comp/elements/cardHeader.vue'
    import DropdownList from '@comp/elements/dropdownList.vue'
    import InputText from '@comp/elements/inputText.vue'
    import LongText from '@comp/elements/textoAmplio.vue'
    import CheckBoxMultiple from '@comp/elements/checkboxMultipleOption.vue'
    
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
                  'Grupo de investigación 1'
          ]"
          @click="handleToggle"
          />

      <div class="card-content toggle_show" v-show="show">

      <DropdownList
        id_name="grupo"
        label="Nombre del grupo"
        :options="[
          {'arte-accion': 'ARTE – ACCIÓN'},
          {'sam': 'Sapiencia, Arte y Música (S.A.M.)'},
          {'feliza': 'Feliza Bursztyn: Redes, Arte, Cultura['},
          {'videns': 'Investigaciones Visuales del Caribe VIDENS'},
          {'tei': 'Teatro, Espacio e Interactividad TEI'}
          ]"
        add_info= ""
        :stackClass="true"
      />

      <DropdownList
        id_name="programa"
        label="Programa"
        :options="[
          {'licenciatura_en_musica': 'Licenciatura en música'},
          {'musica': 'Música'},
          {'arte_dramatico': 'Arte dramático'},
          {'danza': 'Danza'},
          {'artes_plasticas': 'Artes Plásticas'}
          ]"
        add_info= ""
        :stackClass="true"
      />

      <CheckBoxMultiple
        id_name="linea_investiga"
        label="Línea de investigación"
        :options="[
                 {id_name:'musical', text:'Creación musical'},
                 {id_name:'cultura', text:'Desarrollo y cultura'},
                 {id_name:'estetica', text:'Estética'},
                 {id_name:'pedagogia', text:'Pedagogía'},
        ]"
        add_info=""
        :isRequired="true"
        :stackClass="false"
      />


        <LongText
          id_name="actividades"
          label="Actividades"
          content=""
          add_info="Breve descripción de las actividades llevadas a cabo"
          :isRequired="true"
          :stackClass="false"
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

