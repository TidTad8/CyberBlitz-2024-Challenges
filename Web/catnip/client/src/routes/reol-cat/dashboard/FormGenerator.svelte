<script lang="ts">
	import { generateReportAPI } from '$lib/services/generateReport';
    import { onMount } from 'svelte';
	import type { ToastSettings, ToastStore } from '@skeletonlabs/skeleton';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { goto } from '$app/navigation';

	const toastStore = getToastStore();

    let flag = '';

    let adoptionCenters = [
        'Whisker Haven Adoption Center',
        'Pawsitive Futures Cat Shelter',
        'Feline Friends Adoption Agency',
        'Kitty Kingdom Adoption Center',
        'Meow Manor Adoption Center',
        'Purrfect Pals Cat Sanctuary',
        'Furry Tails Adoption Center',
        "Cat's Cradle Adoption Shelter",
        'Happy Tails Cat Rescue',
        'Cuddle Paws Adoption Center'
    ];

    let selectedCenter = '';
    let catAmount = '';
    let reason = '';
    let generateButtonDisabled = true;

    function handleCenterSelection(event: any) {
        selectedCenter = event.target.value;
        updateGenerateButtonState();
    }

    function handleCatAmountInput(event: any) {
        catAmount = event.target.value;
        updateGenerateButtonState();
    }

    function handleReasonInput(event: any) {
        reason = event.target.value;
        updateGenerateButtonState();
    }

    function updateGenerateButtonState() {
        generateButtonDisabled = !(selectedCenter && catAmount && reason);
    }

    // Function to enable button on mount if inputs are pre-filled
    onMount(() => {
        updateGenerateButtonState();
    });

    function handleSubmit() {
        generateReportAPI(Number(catAmount), selectedCenter, reason).then(async (response: Response) => {
            if (response.ok) {

                const contentType = response.headers.get('Content-Type');
                if (contentType && contentType.includes('application/json')) {
                    const data = await response.json();

                    flag = data.flag
                    return
                }

                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.target = '_blank';
                a.download = 'cat_adoption_request.pdf';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            } else if (response.status === 400) {
                const t: ToastSettings = {
                    message: 'Invalid inputs! Fill up the form properly!',
                    background: 'variant-filled-warning',
                };
                toastStore.trigger(t);
            } else if (response.status === 401) {
                goto('/reol-cat');
                const t: ToastSettings = {
                    message: 'Your session token expired, login again!',
                    background: 'variant-filled-warning',
                };
                toastStore.trigger(t);
            } else {
                const t: ToastSettings = {
                    message: 'Server Error!',
                    background: 'variant-filled-error',
                };
                toastStore.trigger(t);
            }
        })
    }
</script>

<div class="m-9">
    <h1 class="h1 center mb-6">Cat Request Creator</h1>
    <h4 class="h4 center mb-6">Automated document creation for requesting new cats</h4>

    <div class="card p-4">
        <label class="label">
            <span>Adoption Center</span>
            <select class="select" bind:value={selectedCenter} on:change={handleCenterSelection}>
                {#each adoptionCenters as center, i}
                    <option value={center}>{center}</option>
                {/each}
            </select>
        </label>

        <label class="label mt-3">
            <span>Cat Amount</span>
            <input class="input" type="number" placeholder="Number of cats to request" bind:value={catAmount} on:input={handleCatAmountInput} />
        </label>

        <label class="label mt-3">
            <span>Reason</span>
            <textarea class="textarea" rows="8" placeholder="Indicate reason or message for request" bind:value={reason} on:input={handleReasonInput}></textarea>
        </label>
    </div>

    <button type="button" class="btn variant-filled mt-2" disabled={generateButtonDisabled} on:click={handleSubmit}> Generate </button>

    {#if flag}
        <blockquote class="blockquote mt-4">Thanks for getting me access! I found something in the system as well, maybe it will help? 
            <code class="code">
                {flag}
            </code>
        </blockquote>
    {/if}

</div>

<style>
    .center {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
