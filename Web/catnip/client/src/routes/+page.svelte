<script lang="ts">
	import CatGallery from '$lib/components/CatGallery.svelte';
	import Countdown from '$lib/components/Countdown.svelte';
	import { Avatar } from '@skeletonlabs/skeleton';
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex flex-col items-center">
		<h1 class="h1 mt-9">Welcome to Cat Cafe</h1>

		<Countdown />
		<CatGallery />

		<h1 class="h1 mt-4">Meet our Staff</h1>
			<div class="grid grid-cols-2 grid-rows-2 gap-y-4 w-full">
				<div class="row-start-1 col-start-1 col-span-1 row-span-1" style="width: 90%;">
					<div class="card card-hover">
						<header class="card-header text-center">
							<center>
								<Avatar src="/staffpicture/cappo.png" width="w-16" rounded="rounded-xl" />
								<h4 class="h4 text-center">
									Cappo
								</h4>
							</center>
						</header>
						<section class="p-4">
							Cappo, our cat-loving manager, oversees the operations of this delightful cafe dedicated to feline enthusiasts!
						</section>
					</div>
				</div>
				<div class="row-start-2 col-start-1 col-span-1 row-span-1" style="width: 30%;">
					<div class="m4" style="height: 50px;">
					</div>
				</div>
				<div class="row-start-1 col-start-2 col-span-1 row-span-2">
					<div class="m4" style="height: 50px;">
					</div>
						<div class="card card-hover">
							<header class="card-header">
								<center>
									<Avatar src="/staffpicture/pointyCatt.png" width="w-16" rounded="rounded-xl" />
									<h4 class="h4 text-center">
										Pointy Catt
									</h4>
								</center>
							</header>
							<section class="p-4">
								Pointy Catt, our cat powered programmer, is the manager and owner of the Cat Cafe website!
							</section>
							<footer class="card-footer">
								<button class="chip variant-filled hover:variant-ghost-primary">
									<a rel="me" href="https://mastodon.social/@pointyCatt" target="_blank">Mastodon</a>
								</button>
							</footer>
						</div>
				</div>
			</div>
	</div>
</div>
