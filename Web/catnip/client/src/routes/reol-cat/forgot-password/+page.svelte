<script lang="ts">
	import { forgetPasswordAPI } from "$lib/services/forgetPassword";
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	import { getToastStore } from '@skeletonlabs/skeleton';

	const toastStore = getToastStore();
    let email = '';

    function handleEmailInput(event: any) {
        email = event.target.value;
    }

    function handleSubmit() {
        if (email.trim() !== '') {
            forgetPasswordAPI(email).then((data: any) => {
                if (data.results.length <= 0) {
                    const t: ToastSettings = {
                        message: 'Email not found!',
                        background: 'variant-filled-warning',
                    };
                    toastStore.trigger(t);
                    return
                }

                const t: ToastSettings = {
                    message: 'Reset link sent!',
                    background: 'variant-filled-success',
                };
                toastStore.trigger(t);
            }).catch((err: any) => {
                const t: ToastSettings = {
                    message: 'Unknown error occured!',
                    background: 'variant-filled-error',
                };
                toastStore.trigger(t);
            })
        }
    }
</script>

<div class="container h-full mx-auto flex justify-center items-center">
    <div class="space-y-10 text-center flex flex-col items-center">
        <h1 class="h1 mt-9">Reset Password</h1>

        <div class="card p-4">
            <label class="label">
                <span>Email</span>
                <input bind:value={email} on:input={(e) => handleEmailInput(e)} class="input" type="text" placeholder="Account Email" />
            </label>

            <button on:click={handleSubmit} class="btn variant-filled mt-4" disabled={email.trim() === ''}>
                Request Reset
            </button>
        </div>

        <a class="anchor" href="/reol-cat">Login Instead</a>
    </div>
</div>
