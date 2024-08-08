<script setup>

	import {ref, computed} from 'vue'

	const props = defineProps({
		id_name:{
			type:String,
			required:true,
			default:"fileLoader"
		},
		label:{
			type:String,
			required:false,
			default:"Adjunte documentos"
		},
		filename:{
			type:String,
			required:false,
			default:''
		},
		filenameLengthLimit:{
			type:Number,
			required:false,
			default:10
		},
		add_info:{
			type:String,
			required:false
		},
		isRequired:{
			type:Boolean,
			default:false
		},
		stackClass:{
			type:Boolean,
			default:false
		},
		popupText: {
			type:String,
			required:false,
			default:""
		}
	})

	const filename = ref(props.filename)
	const filenameLengthLimit = ref(props.filenameLengthLimit)
	const filenameMessage = computed( () => {
		if (filename.value.length > filenameLengthLimit.value) {
			return "Archivo cargado: " + filename.value.slice(0, filenameLengthLimit.value) + "..."
		} else if (filename.value.length > 0) {
			return "Archivo cargado: " + filename.value
		} else {
			return "Seleccionar archivo"
		}
	})

	function updateFileName(event) {
		if (event.target.files && event.target.files.length > 0) {
				filename.value = event.target.files[0].name;
		} else {
				filename.value = "";
		}
	}

</script>

<template>
	<div class="form-item ">
		<h3 class="label">
			{{label}}
			<span
					v-if="popupText !== ''"
					class="info-icon"
					@click="popupToggleShow">
				ℹ️
			</span>
		</h3>
		<div id="camposNombres">
			<div class="group-multiple-text" id="Q_estudiante_1">
				<div class="file-upload">
					<input 
						class="stack"
						type="file" 
						:id="id_name" 
						:name="id_name" 
						:required="isRequired"
						@change="updateFileName"
					>
					<label :for="id_name">
						<i class="fas fa-upload"></i>
					</label>
					<span class="file-name" id="file-name-estudiante_1">
						{{ filenameMessage	}}
					</span>
				</div>
			</div>
		</div>

	</div>
</template>

<style scoped>
</style>
