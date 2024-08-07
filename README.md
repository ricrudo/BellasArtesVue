# BellasArtes2_frontend

This template should help get you started developing with Vue 3 in Vite.

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

<details>
<summary><b>CUADRO TEXTO</b></summary>

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
    />
    ```
    
    `id_name` El id y nombre del elemento para que reconocerá el formulario
    `label` El texto que muestra en pantalla
    `content` El contenido dentro del cuadro de texto
    `add_info` Información adicional
    `:stackClass` Agrega la clase stack para que se puedan ver dos elementos en un misma linea
</details>
        
<details>
<summary><b>DROPDOWN</b></summary>

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
    />
    
    ```
    
    `id_name` El id y nombre del elemento para que reconocerá el formulario
    
    `label` El título que muestra en pantalla
    
    `options` Las opciones de la lista. Es un array de dicts, donde el key=name y value=texto en pantalla
    
    `add_info` Información adicional
    
    `:stackClass` Agrega la clase stack para que se puedan ver dos elementos en un misma linea
</details>
        
<details>
<summary><b>RADIO MULTIPLE OPTIONS</b></summary>

- Script
    
    ```jsx
    import RadioMultipleOptions from '@comp/elements/radioMultipleOptions.vue'
    ```
    
- Template
    
    ```jsx
    <RadioMultipleOptions
            radioID="esteID"
            title="¿El proyecto fue elegido?"
            :options="[{value:'si', text:'Si'},
            {value:'no', text:'No'},
            {value:'espera', text:'En espera de resultados'}
            ]"
    />
    ```
    

    `radioID` El id y nombre del elemento para que reconocerá el formulario
    `title` El título que muestra en pantalla
    `:options` Las opciones de los radios. Es un array de dicts, donde el value=lo que reconoce el formulario y text=lo que muestra en pantalla
</details>
        
<details>
<summary><b>FORM BREAK</b></summary>
    
- Script
    ```jsx
    <div class="form-break"></div>
    ```
    
</details>
        
<details>
<summary><b>RADIO YES NO (Inside Card)</b></summary>

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
    />
    ```
</details>
        
<details>
<summary><b>MULTIPLES CUADROS DE TEXTO</b></summary>

- Script
    
    ```jsx
    import MultipleInputText from '@comp/elements/multipleInputText.vue'
    ```
    
- Template
    
    ```jsx
    <MultipleInputText
            id_name="esteID"
            textLabel="Lista todos los nombres de los estudiantes con el botón &quot;Añadir&quot;"
            textAddButton="+ Añadir estudiante"/>
    ```
</details>
        
<details>
<summary><b>BOTÓN BORRAR ELEMENTO</b></summary>

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
<summary><b>BOTÓN AGREGAR ELEMENTO</b></summary>

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
<summary><b>DATE INPUT</b></summary>

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
            />
    ```
</details>
        
<details>
<summary><b>RADIO MULTIPLE OPTIONS</b></summary>

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
      />
    ```
        
</details>
        
<details>
<summary><b>LONG TEXT</b></summary>

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
        />
    ```
</details>
        
<details>
<summary><b>CHECKBOX MULTIPLE OPTION</b></summary>

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
      />
    ```
</details>
