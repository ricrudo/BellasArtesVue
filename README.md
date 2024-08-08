# BellasArtes2_frontend

Este archivo describe por un lado los procesos posibles con VUE que son útiles para el desarrollo y por otro líneas de codigo que se pueden pegar en un archivo de aquellos elementos que la app necesita

<details>
<summary>

# NPM, VUE and NODE configuration and process 

</summary>

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Documentacion básica
</details>

<details>
<summary>

### CUADRO TEXTO

</summary>

- Script
    
    ```jsx
      import InputText from '@comp/elements/inputText.vue'
    ```
    
- Template
    
    ```jsx
    <InputText
        id_name="esteID"
        label="Nombre de la asignatura"
        content="esto es una prueba"
        add_info= "esto lo invente"
        :stackClass="true"
        popupText=""
    />
    ```
    
    `id_name` El id y nombre del elemento para que reconocerá el formulario

    `label` El texto que muestra en pantalla

    `content` El contenido dentro del cuadro de texto

    `add_info` Información adicional

    `:stackClass` Agrega la clase stack para que se puedan ver dos elementos en un misma linea
</details>
        
<details>
<summary>

### LONG TEXT
</summary>

- script
    
    ```jsx
    import LongText from '@comp/elements/textoAmplio.vue'
    ```
    
- template
    
    ```jsx
    <LongText
        id_name="id_name"
        label="label"
        content="value"
        add_info=""
        :isRequired="true"
        :stackClass="true"
        popupText=""
    />
    ```
</details>

<details>
<summary>

### DATE INPUT
</summary>

- script
    
    ```jsx
      import DateInput from '@comp/elements/dateInput.vue'
    ```
    
- template
    
    ```jsx
    <DateInput
        id_name="id_name"
        label="el label"
        value="el value"
        add_info="la add info"
        :isRequired="true"
        :stackClass="true"
        popupText=""
    />
    ```
</details>

<details>
<summary>

### DROPDOWN

</summary>

- Script
    
    ```jsx
      import DropdownList from '@comp/elements/dropdownList.vue'
    ```
    
- Template
    
    ```jsx
    <DropdownList
        id_name="cardID"
        label="'Programa ' + cardID"
        :options="[
            {'lic': 'Licenciatura en música'},
            {'musica': 'Música'},
            {'dram': 'Arte dramático'},
            {'Danza': 'Danza'},
            {'plas': 'Artes Plásticas'}
        ]"
        add_info= "esto lo invente"
        :stackClass="true"
        popupText=""
    />
    
    ```
    
    `id_name` El id y nombre del elemento para que reconocerá el formulario
    
    `label` El título que muestra en pantalla
    
    `options` Las opciones de la lista. Es un array de dicts, donde el key=name y value=texto en pantalla
    
    `add_info` Información adicional
    
    `:stackClass` Agrega la clase stack para que se puedan ver dos elementos en un misma linea
</details>
        
<details>
<summary>

### RADIO MULTIPLE OPTIONS

</summary>

- Script
    
    ```jsx
    import RadioMultipleOptions from '@comp/elements/radioMultipleOptions.vue'
    ```
    
- Template
    
    ```jsx
    <RadioMultipleOptions
        radioID="esteID"
        title="¿El proyecto fue elegido?"
        :options="[
            {value:'si', text:'Si'},
            {value:'no', text:'No'},
            {value:'espera', text:'En espera de resultados'}
        ]"
        popupText=""
    />
    ```
    

    `radioID` El id y nombre del elemento para que reconocerá el formulario

    `title` El título que muestra en pantalla

    `:options` Las opciones de los radios. Es un array de dicts, donde el value=lo que reconoce el formulario y text=lo que muestra en pantalla
</details>
        
<details>
<summary>

### RADIO YES NO (Inside Card)
</summary>

- Script
    
    ```jsx
    import RadioYesNoCard from '@comp/elements/radioYesNoCard.vue'
    ```
    
- Template
    
    ```jsx
    <RadioYesNoCard 
        @update="handleRadio"
        radioID="esteRadio"
        title="¿El proyecto cuenta con la participación algún semillero de investigación?" 
        additional_info=""
        :stackClass="true"
        popupText=""
        />
    ```
</details>
        
<details>
<summary>

### RADIO MULTIPLE OPTIONS
</summary>

- script
    
    ```jsx
      import RadioMultipleOptions from '@comp/elements/radioMultipleOptions.vue'
    ```
    
- template
    
    ```jsx
    <RadioMultipleOptions
        radioID="esteID"
        title="¿El proyecto fue elegido?"
        :options="[
        {value:'si', text:'Si'},
        {value:'no', text:'No'},
        {value:'espera', text:'En espera de resultados'}
        ]"
        additional_info="info"
        :isRequired="true"
        :stackClass="true"
        popupText=""
    />
    ```
        
</details>

<details>
<summary>

### CHECKBOX MULTIPLE OPTION
</summary>

- script
    
    ```jsx
      import CheckBoxMultiple from '@comp/elements/checkboxMultipleOption.vue'
    ```
    
- template
    
    ```jsx
    <CheckBoxMultiple
        id_name="esteID"
        label="este checkbox"
        :options="[
        {id_name:'id1', text:'opt1'},
        {id_name:'id2', text:'opt2'},
        ]"
        add_info=""
        :isRequired="true"
        :stackClass="true"
        popupText=""
    />
    ```
</details>

<details>
<summary>

### MULTIPLES CUADROS DE TEXTO
</summary>

- Script
    
    ```jsx
    import MultipleInputText from '@comp/elements/multipleInputText.vue'
    ```
    
- Template
    
    ```jsx
    <MultipleInputText
        id_name="esteID"
        textLabel="Lista todos los nombres de los estudiantes con el botón &quot;Añadir&quot;"
        textAddButton="+ Añadir estudiante"
        popupText=""
    />
    ```
</details>
        
<details>
<summary>

### BOTÓN BORRAR ELEMENTO
</summary>

- Script
    
    ```jsx
    import ButtonRemove from '@comp/elements/buttonRemove.vue'
    ```
    
- Template
    
    ```jsx
    <ButtonRemove
        @click="emitCardID"
        text="Borrar proyecto"
    />
    ```
    
    `text` El texto del botón
</details>
        
<details>
<summary>

### BOTÓN AGREGAR ELEMENTO
</summary>

- script
    
    ```jsx
    import ButtonAddRemove from '@comp/elements/buttonAddElement.vue'
    ```
    
- Template
    
    ```jsx
    <ButtonAddElement
        text="textAddButton"
        classes="add-multiple-text-button"
        entries="entries"
        keyword="keyword"
    />
    ```
    
    `text` el texto del botón
    
    `classes` generalmente es la clase `add-multiple-text-button` que es para cuando el botón esta dentro de una card
    
    `entries` el Objeto del que recibe la información de la que depende la creación. 
    
    `keyword` el keyword para el ID del nuevo objeto. 
</details>
        
<details>
<summary>

### BOTÓN CARGAR DOCUMENTO/ARCHIVO
</summary>

- script
    
    ```jsx
  import UploadBox from '@comp/elements/uploadButton.vue'
    ```
    
- Template
    
    ```jsx
    <UploadBox
        id_name="id_name"
        label=""
        filename=""
        :filenameLengthLimit="90"
        add_info=""
        :isRequired="true"
        :stackClass="false"
        popupText=""
    />
    ```
    
    `id_name` el id del elemento
    
    `label` El texto que va en el label el elemento
    
    `filename` el nombre del archivo si la base de datos lo carga 
    
    `filenameLengthLimit` cuantas letras máximo muestra del nombre del archivo 

    `add_info` el bloque de información adicional debajo del elemento

    `isRequired` Indica si es un campo obligatorio. "true" o "false" son las unicas opciones

    `stackClass` Indica si el elemento se presenta en stack. "true" o "false" son las unicas opciones 

    `popupText` El texto de es que lleva un popup. Si esta campo esta vació no se mostrará la opción de popup
</details>
<details>
<summary>

### FORM BREAK
</summary>
    
- Script
    ```jsx
    <div class="form-break"></div>
    ```
    
</details>
