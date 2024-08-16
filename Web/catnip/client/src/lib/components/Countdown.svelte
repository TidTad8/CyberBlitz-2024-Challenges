<script lang="ts">
	import { onMount, onDestroy } from 'svelte';

	let countdown: {
		days: number;
		hours: number;
		minutes: number;
		seconds: number;
	} = { days: 0, hours: 0, minutes: 0, seconds: 0 };

	let interval: NodeJS.Timeout;

	onMount(() => {
		const launchDate = new Date();
		launchDate.setDate(launchDate.getDate() + 24);

		interval = setInterval(() => {
			const now = new Date();
			const difference = launchDate.getTime() - now.getTime();

			countdown.days = Math.floor(difference / (1000 * 60 * 60 * 24));
			countdown.hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
			countdown.minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
			countdown.seconds = Math.floor((difference % (1000 * 60)) / 1000);
		}, 1000);
	});

	onDestroy(() => {
		clearInterval(interval);
	});
</script>

<div class="text-center">
    <h3 class="mt-2" style="font-size: 2rem;">
        {countdown.days} days, {countdown.hours} hours, {countdown.minutes} minutes, {countdown.seconds}
        seconds until launch
    </h3>
</div>