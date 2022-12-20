<main class="-mt-24 pb-8">
	<div class="mx-auto max-w-3xl px-4 sm:px-6 lg:max-w-7xl lg:px-8">
		<h1 class="sr-only">Page title</h1>

		<!-- Main 3 column grid -->
		<div class="grid grid-cols-1 items-start gap-4 lg:grid-cols-3 lg:gap-8">
			<!-- Left column -->
			<div class="grid grid-cols-1 gap-4 lg:col-span-2">
				<section aria-labelledby="section-1-title">
					<h2 class="sr-only" id="section-1-title">Main</h2>
					<div class="overflow-auto rounded-lg bg-white shadow h-96">
						<div class="p-2">
							<!-- Your content -->
							<slot name="main" />
						</div>
					</div>
				</section>
			</div>

			<!-- Right column -->
			<div class="grid grid-cols-1 gap-4">
				<section aria-labelledby="section-2-title">
					<h2 class="sr-only" id="section-2-title">Sidebar</h2>
					<div class=" rounded-lg bg-white shadow overflow-auto h-96">
						<div class="p-2">
							<!-- Your content -->
							<slot name="sidebar" />
						</div>
					</div>
				</section>
			</div>
		</div>
	</div>
</main>
