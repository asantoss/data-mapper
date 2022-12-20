<script lang="ts">
	import '../app.css';
	import { env as public_env } from '$env/dynamic/public';
	import { parserStore } from '$lib/stores';
	import { theme } from '$lib/stores';
	export const prerender = true;
	const apiUrl = public_env.PUBLIC_API_URL ?? '';
	let fileInput: HTMLInputElement;
	async function handleSubmit(event: Event) {
		event.preventDefault();
		if (event.target) {
			const { files } = <HTMLInputElement>event?.target;
			if (!files) return;
			const body = new FormData();
			body.append('file', files[0]);
			const response = await fetch(apiUrl + '/file', {
				method: 'POST',
				body
			});
			const data = await response.json();

			$parserStore = {
				...data,
				columns: data.columns.map((e: string) => ({
					name: e,
					value: e,
					deleted: false
				}))
			};
		}
	}

	async function processFile() {
		if (fileInput?.files) {
			const body = new FormData();
			const file = fileInput.files[0];
			body.append('file', file);
			body.append('data', JSON.stringify($parserStore));
			const response = await fetch(apiUrl + '/file/process', {
				method: 'POST',
				body
			});
			const blob = await response.blob();
			var url = window.URL.createObjectURL(blob);
			var a = document.createElement('a');
			a.href = url;
			a.download = `${file.name.replace(/\.\w+/gi, '')}_mapped.csv`;
			document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
			a.click();
			a.remove(); //afterwards we remove the element again
		}
	}
</script>

<div class="min-h-full">
	<header class="bg-indigo-600 pb-24">
		<div class="mx-auto max-w-3xl px-4 sm:px-6 lg:max-w-7xl lg:px-8">
			<div class="relative flex items-center justify-center py-5 lg:justify-between">
				<!-- Logo -->
				<div class="absolute left-0 flex-shrink-0 lg:static">
					<div class="ml-auto">
						<select bind:value={$theme}>
							<option value="system">System</option>
							<option value="light">Light</option>
							<option value="dark">Dark</option>
						</select>
					</div>
				</div>

				<!-- Menu button -->
				<div class="absolute right-0 flex-shrink-0 lg:hidden">
					<!-- Mobile menu button -->
					<button
						type="button"
						class="inline-flex items-center justify-center rounded-md bg-transparent p-2 text-indigo-200 hover:bg-white hover:bg-opacity-10 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
						aria-expanded="false"
					>
						<span class="sr-only">Open main menu</span>
						<!--
              Heroicon name: outline/bars-3

              Menu open: "hidden", Menu closed: "block"
            -->
						<svg
							class="block h-6 w-6"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							aria-hidden="true"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
							/>
						</svg>
						<!--
              Heroicon name: outline/x-mark

              Menu open: "block", Menu closed: "hidden"
            -->
						<svg
							class="hidden h-6 w-6"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							aria-hidden="true"
						>
							<path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
						</svg>
					</button>
				</div>
			</div>
			<div class="hidden border-t border-white border-opacity-20 py-5 lg:block">
				<div class="grid grid-cols-3 items-center gap-8">
					<div class="col-span-2">
						<input
							bind:this={fileInput}
							type="file"
							on:change={handleSubmit}
							name="file"
							accept="csv"
						/>
					</div>
					<div class="ml-auto w-full max-w-md flex">
						<div>
							<label for="mobile-search" class="sr-only">Search</label>
							<div class="relative text-white focus-within:text-gray-600">
								<div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
									<!-- Heroicon name: mini/magnifying-glass -->
									<svg
										class="h-5 w-5"
										xmlns="http://www.w3.org/2000/svg"
										viewBox="0 0 20 20"
										fill="currentColor"
										aria-hidden="true"
									>
										<path
											fill-rule="evenodd"
											d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
											clip-rule="evenodd"
										/>
									</svg>
								</div>
								<input
									id="mobile-search"
									class="block w-full rounded-md border border-transparent bg-white bg-opacity-20 py-2 pl-10 pr-3 leading-5 text-gray-900 placeholder-white focus:border-transparent focus:bg-opacity-100 focus:placeholder-gray-500 focus:outline-none focus:ring-0 sm:text-sm"
									placeholder="Search"
									type="search"
									name="search"
								/>
							</div>
						</div>
						<button
							type="button"
							on:click={processFile}
							class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
							>Process</button
						>
					</div>
				</div>
			</div>
		</div>
	</header>

	<slot />
	<footer>
		<div class="mx-auto max-w-3xl px-4 sm:px-6 lg:max-w-7xl lg:px-8">
			<div class="border-t border-gray-200 py-8 text-center text-sm text-gray-500 sm:text-left">
				<span class="block sm:inline">&copy; 2021 Your Company, Inc.</span>
				<span class="block sm:inline">All rights reserved.</span>
			</div>
		</div>
	</footer>
</div>
