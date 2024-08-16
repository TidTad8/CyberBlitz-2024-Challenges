<script lang="ts">
	import { AppRail, AppRailTile, AppRailAnchor } from '@skeletonlabs/skeleton';
	import Icon from '@iconify/svelte';
	import CatTable from './CatTable.svelte';
	import FormGenerator from './FormGenerator.svelte';
	import { onMount } from 'svelte';
	import { getSessionCookie, removeSessionCookie } from '$lib/cookies/sessionCookie';
	import { goto } from '$app/navigation';

	import type { ToastSettings, ToastStore } from '@skeletonlabs/skeleton';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { tokenCheckAPI } from '$lib/services/tokenCheck';
	import { logoutAPI } from '$lib/services/logout';

	const toastStore = getToastStore();

	let currentTile: number = 0;
	let loggedInUsername: string = ""
	let flagValue: string = ""

	onMount(() => {
		const revokeSessionAndPromptLogin = () => {
			removeSessionCookie()
			goto('/reol-cat')
			const t: ToastSettings = {
				message: 'Session token expired, please login again!',
				background: 'variant-filled-warning',
			};
			toastStore.trigger(t);
		}

		const currentCookie = getSessionCookie()

		if (currentCookie === undefined || currentCookie.trim() === "") {
			revokeSessionAndPromptLogin()
			return
		}

		tokenCheckAPI().then((data: any) => {
			try {
				loggedInUsername = data.username;
				flagValue = data.flag
			} catch (err) {
				revokeSessionAndPromptLogin()
			}
		}).catch((_) => {
			revokeSessionAndPromptLogin()
		})
	})
</script>

<div class="h-full grid grid-cols-[auto_1fr] w-full">
	<AppRail>
		<AppRailTile bind:group={currentTile} name="tile-1" value={0} title="tile-1">
			<svelte:fragment slot="lead">
				<div class="center">
					<Icon icon="hugeicons:analytics-down" />
				</div>
			</svelte:fragment>
			<span>Dashboard</span>
		</AppRailTile>
		<AppRailTile bind:group={currentTile} name="tile-2" value={1} title="tile-2">
			<svelte:fragment slot="lead">
				<div class="center">
					<Icon icon="codicon:file-pdf" />
				</div>
			</svelte:fragment>
			<span>Request Creator</span>
		</AppRailTile>
		<!-- --- -->

		<svelte:fragment slot="trail">
			<AppRailAnchor href="#" on:click={() => {
				removeSessionCookie();
				logoutAPI().then(() => {
					goto('/');
					toastStore.trigger({
						message: 'Logout successful!',
						background: 'variant-filled-success',
					});
				}).catch((_) => {
					toastStore.trigger({
						message: 'Logout failed!',
						background: 'variant-filled-error',
					});
				});
			}} title="Logout">
				<svelte:fragment slot="lead">
					<div class="center">
						<Icon icon="material-symbols:logout-sharp" />
					</div>
				</svelte:fragment>
				<span> Logout </span>
			</AppRailAnchor>
		</svelte:fragment>
	</AppRail>


	{#if loggedInUsername === ""}
		<div class="m-9">
			<h1 class="h1 m=2">Not Authorized</h1>
		</div>
	{:else}
		<!-- Actual Contents -->
		{#if currentTile == 0}
			<!--Dashboard-->
			<div class="m-9">
				<h1 class="h1 m=2">Welcome Back, {loggedInUsername}</h1>
				<h4 class="h4 m-4">Flag: {flagValue}</h4>
				<h4 class="h2 center mb-6 mt-6">Owned Cats</h4>
				<CatTable />
			</div>
		{:else}
			<FormGenerator/>
		{/if}
	{/if}
</div>

<style>
	.center {
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
