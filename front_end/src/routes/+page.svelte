<script lang="ts">
	import { parserStore } from '$lib/stores';
	import Column from '$lib/components/column.svelte';
	import CustomLayout from '$lib/components/customLayout.svelte';

	$: cols = $parserStore.columns.map((e) => e.name);
</script>

<CustomLayout>
	<table
		slot="main"
		class="rounded table-auto text-sm border-separate border-spacing-1 border-slate-500"
	>
		<thead>
			<tr>
				{#each $parserStore.columns as col}
					<th class="border-b font-medium p-2 pt-0 pb-3 text-slate-800 text-left truncate">
						{col.name}
					</th>
				{/each}
			</tr>
		</thead>
		<tbody class="bg-white">
			{#each $parserStore.rows as row}
				<tr class="odd:bg-gray-100">
					{#each cols as col}
						<td
							class="border-b border-slate-100 p-2 text-left truncate text-slate-800 overflow-hidden text-ellipsis"
						>
							{row[col]}
						</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>

	<div slot="sidebar" class="">
		<div class="mt-6 flow-root">
			<ul role="list" class="-my-5 divide-y divide-gray-200">
				{#each $parserStore.columns as col}
					<Column column={col} />
				{/each}
			</ul>
		</div>
	</div>
</CustomLayout>

<style>
</style>
