<script setup>

  import { ref } from 'vue'
  import CardHeader from '@comp/elements/cardHeader.vue'
    import InputText from '@comp/elements/inputText.vue'
    import DropdownList from '@comp/elements/dropdownList.vue'
    import DateInput from '@comp/elements/dateInput.vue'
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
                  'Producto 1'
          ]"
          @click="handleToggle"
          />

      <div class="card-content toggle_show" v-show="show">

      <DropdownList
        id_name="tipo_producto"
        label="Tipo de producto"
        :options="[
          {'gnc': 'Generación de nuevo conocimiento'},
          {'dti': 'Desarrollo tecnológico e innovación'},
          {'asc': 'Apropiación social del conocimiento'},
          {'frh': 'Formación de Recurso Humano en CTeI'},
          ]"
        add_info= "Características de la actividad de la cual el producto es resultado"
        :isRequired="true"
        :stackClass="false"
      />



      <InputText
        id_name="nombre_producto"
        label="Nombre del producto"
        content=""
        add_info= ""
        :isRequired="true"
        :stackClass="true"
      />

      <InputText
        id_name="institucion"
        label="Institución"
        content=""
        add_info= "Institución donde fue exhibido o presentado"
        :isRequired="true"
        :stackClass="true"
      />

      <DropdownList
        id_name="alcance"
        label="Alcance"
        :options="[
          {'local': 'Local'},
          {'regional': 'Regional'},
          {'nacional': 'Nacional'},
          {'internacional': 'Internacional'},
          ]"
        add_info= ""
        :isRequired="true"
        :stackClass="true"
      />



      <DateInput
        id_name="fecha"
        label="Fecha"
        value=""
        add_info=""
        :isRequired="true"
        :stackClass="true"
      />

      <InputText
        id_name="institucion"
        label="Link de difusión o nombre del catálogo"
        content=""
        add_info= "Link de difusión del evento/obra o nombre del catálogo si lo hubiera"
        :isRequired="true"
        :stackClass="true"
      />

      

      <DropdownList
        id_name="categoria"
        label="Categoría de reconocimiento"
        :options="[
          {'tipo_a': 'Tipo A'},
          {'tipo_b': 'Tipo B'},
          {'no_responde': 'No ha sido reconocido'},
          ]"
        add_info= ""
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

<style scoped>
.card-content {
  width: 100%;
}
</style>
