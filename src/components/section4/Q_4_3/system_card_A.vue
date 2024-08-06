<script setup>

  import { ref } from 'vue'
  import CardHeader from '@comp/elements/cardHeader.vue'
  import InputText from '@comp/elements/inputText.vue'
  import DropdownList from '@comp/elements/dropdownList.vue'
  import RadioMultipleOptions from '@comp/elements/radioMultipleOptions.vue'
  import RadioYesNoCard from '@comp/elements/radioYesNoCard.vue'
  import MultipleInputText from '@comp/elements/multipleInputText.vue'
  import ButtonRemove from '@comp/elements/buttonRemove.vue'

  const showSemilleros = ref(false)
  const show = ref(true)

  const props = defineProps({
    clave:{
        type:Number,
        required:true
        },
    id_name:{
        type:String,
        required: true
        },
    index:{
        type:Number,
        required:true
    }
  })

  function handleToggle() {
    show.value = !show.value
  }


  function handleSemilleros(value) {
    showSemilleros.value = value === 'si' 
  }

</script>


<template>
  <div class="system-added-cards">
    <div class="card-item-container" id="materia_1">

      <CardHeader 
          :title="['Proyecto 1']"
          @click="handleToggle"
          />

      <div class="card-content toggle_show" v-show="show">


        <InputText
            :id_name="esteID"
            label="Nombre del proyecto"
            content=""
            add_info= ""
            :isRequired="false"
            :stackClass="true"
            />

        <InputText
            :id_name="esteID"
            label="Código de radicado"
            content=""
            add_info= ""
            :isRequired="true"
            :stackClass="true"
            />

        <DropdownList
            :id_name="cardID"
            label="Tipo de convocatoria"
            :options="[
                      {'interna': 'Interna'},
                      {'externa': 'Externa'}
                      ]"
            add_info= ""
            :stackClass="true"
            />

        <InputText
            :id_name="esteID"
            label="Nombre de la convocatoria"
            content=""
            add_info= ""
            :isRequired="true"
            :stackClass="true"
            />

        <DropdownList
            :id_name="cardID"
            label="Tipo de participación"
            :options="[
                      {'principal': 'Investigador/a principal'},
                      {'co-investigador': 'Co-investigador/a'}
                      ]"
            add_info= ""
            :stackClass="true"
            />

        <InputText
            :id_name="esteID"
            label="Entidad financiadora"
            content=""
            add_info= ""
            :isRequired="true"
            :stackClass="true"
            />

        <RadioMultipleOptions
            :radioID="esteID"
            title="¿El proyecto fue elegido?"
            :options="[{value:'si', text:'Si'},
                      {value:'no', text:'No'},
                      {value:'espera', text:'En espera de resultados'}
                      ]"
            />


        <!-- Form Break -->
        <div class="form-break"></div>

        <RadioYesNoCard 
             @update="handleSemilleros"
             :radioID="esteRadio"
             title="¿El proyecto cuenta con la participación algún semillero de investigación?" 
             additional_info=""
             :stackClass="true"
             />


        <InputText
            v-if="showSemilleros"
            :id_name="esteID"
            label="Nombre del semillero"
            content=""
            add_info= ""
            :isRequired="true"
            :stackClass="true"
            />

        <MultipleInputText
            v-if="showSemilleros"
            :id_name="esteID"
            textLabel="Lista todos los nombres de los estudiantes con el botón &quot;Añadir&quot;"
            textAddButton="+ Añadir estudiante"
            />

        <!-- Form Break -->
        <div class="form-break"></div>

        <RadioYesNoCard 
             :radioID="esteRadio"
             title="¿El proyecto aporta a los ODS?" 
             additional_info=""
             :stackClass="false"
             />

        <RadioYesNoCard 
             :radioID="esteRadio"
             title="¿Incluye desarrollo de software para la creación artística?" 
             additional_info=""
             :stackClass="false"
             />


        <RadioYesNoCard 
             :radioID="esteRadio"
             title="¿Es un proyecto I+D+I5?" 
             additional_info=""
             :stackClass="false"
             />


        <ButtonRemove
            @click="emitCardID"
            text="Borrar proyecto"
            v-if="index>0"
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
