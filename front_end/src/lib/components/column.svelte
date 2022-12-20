<script lang="ts">
	import type { Column } from '$lib/stores';
	import Fa from 'svelte-fa';
	import { faPencil, faTrash, faSave, faRedo } from '@fortawesome/free-solid-svg-icons';
	import { prevent_default } from 'svelte/internal';
	let isEditing = false;
	export let column: Column = {
		name: '',
		value: '',
		deleted: false
	};
	function toggleEdit(e: Event) {
		e.preventDefault();
		isEditing = !isEditing;
	}
</script>

<li class="py-4">
	<form on:submit={toggleEdit} class="flex items-center space-x-4">
		<div class="min-w-0 flex-1">
			{#if isEditing}
				<div>
					<label for="email" class="block text-sm font-medium text-gray-700">{column.name}</label>
					<div class="mt-1">
						<input
							autofocus
							type="text"
							bind:value={column.value}
							name={column.name}
							id={column.name}
							class="block w-full rounded py-2 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
						/>
					</div>
				</div>
			{:else}
				{column.value}
			{/if}
		</div>
		<div class="inline-flex">
			<button type="submit" class="mx-1">
				{#if isEditing}
					<Fa icon={faSave} />
				{:else}
					<Fa icon={faPencil} />
				{/if}
			</button>
			<button type="button" class="mx-1" on:click={() => (column.deleted = !column.deleted)}>
				{#if column.deleted}
					<Fa icon={faRedo} />
				{:else}
					<Fa icon={faTrash} />
				{/if}
			</button>
		</div>
	</form>
</li>
