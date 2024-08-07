<script setup>
	import {ref} from 'vue'
	import {addElement} from '@/utils/utils.js'
	import ButtonAddElement from '@comp/elements/buttonAddElement.vue'

	const props = defineProps ({
		entries:{
			type:Object,
			required:false,
			default: () =>({1:{id_name:'entry_1',content:''}})
			},
		keyword:{
			type:String,
			required:true,
			default:'entry'
			},
		textLabel:{
			type:String,
			required:false
			},
		textAddButton:{
			type:String,
			required:false
			},
		classesAddButton:{
			type:String,
			required:false,
			default:"add-multiple-text-button"
			},
		isRequired:{
			type:Boolean,
			default:false
    },
    popupText: {
      type:String,
      required:false,
      default:""
    }
	})

	const entries = ref(props.entries)
  const popupState = ref(false)

  function popupToggleShow() {
    popupState.value = !popupState.value
  }

</script>

<template>
	<div class="form-item">
		<p class="label">{{textLabel}}
			<span
				v-if="popupText !== ''"
				class="info-icon"
				@click="popupToggleShow">
				ℹ️
			</span>
		</p>
		<div>
			<div v-for="(value, key) in entries" :key="key" class="group-multiple-text group-multiple-text-ROD">
				<input
						class="input-multiple-text" 
						type="text" 
						:id="value.id_name" 
						:name="value.id_name" 
						v-model="entries[key].content"
						:required="isRequired"
						@click="console.log(entries)"
						>
						<div
							v-if="key>1"
							@click="delete entries[key]"
							class="delete-multiple-entry-button multiple-entry-button-ROD"
							>
							<i class="fas fa-trash-alt"></i>
						</div>
			</div>
		</div>
		<div class="popup" v-if="popupText !== ''" v-show="popupState">
			<span
					class="close-btn"
					@click="popupToggleShow">
				&times;
			</span>
			<p>{{popupText}}</p>
		</div>

		<ButtonAddElement
				text="textAddButton"
				classes="add-multiple-text-button"
				:entries="entries"
				:keyword="keyword"
				/>
	</div>

</template>

<style scoped>
.multiple-entry-button-ROD {
	cursor: pointer;
	font-size:13.333333px;
	width: 28px;
	display: flex;
	justify-content: center;
	align-items: center;
	height: 28px;
	align-content: center;
}


.multiple-entry-button-ROD:hover {
	transform: scale(1.03);
}


.group-multiple-text-ROD {
	margin: 5px;
	display: flex;
	align-items: center;
}
</style>
