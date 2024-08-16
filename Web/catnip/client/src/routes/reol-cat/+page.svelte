<script lang="ts">
	import { goto } from "$app/navigation";
	import { setSessionCookie } from "$lib/cookies/sessionCookie";
	import { loginAPI } from "$lib/services/login";
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	import { getToastStore } from '@skeletonlabs/skeleton';

	const toastStore = getToastStore();

    let username = '';
    let password = '';

    function handleUsernameInput(event: any) {
        username = event.target.value;
    }

    function handlePasswordInput(event: any) {
        password = event.target.value;
    }

    function handleSubmit() {
        if (username.trim() !== '' && password.trim() !== '') {
            loginAPI(username, password).then((data: any) => {
                const token = data.token;
                if (token == undefined || token == null) {
                    const t: ToastSettings = {
                        message: 'Incorrect username or password!',
                        background: 'variant-filled-warning',
                    };
                    toastStore.trigger(t);
                    return
                }
                
                goto('/reol-cat/dashboard')
                const t: ToastSettings = {
                    message: 'Login successful!',
                    background: 'variant-filled-success',
                };
                toastStore.trigger(t);
                setSessionCookie(token) 
                return
            })
        }
    }
</script>

<div class="container h-full mx-auto flex justify-center items-center">
    <div class="space-y-10 text-center flex flex-col items-center">
        <h1 class="h1 mt-9">Admin Dashboard</h1>

        <div class="card p-4">
            <label class="label">
                <span>Username</span>
                <input bind:value={username} on:input={(e) => handleUsernameInput(e)} class="input" type="text" placeholder="Username" />
            </label>

            <label class="label mt-4">
                <span>Password</span>
                <input bind:value={password} on:input={(e) => handlePasswordInput(e)} class="input" type="password" placeholder="Password" />
            </label>

            <button on:click={handleSubmit} class="btn variant-filled mt-4" disabled={username.trim() === '' || password.trim() === ''}>
                Login
            </button>
        </div>

        <a class="anchor" href="/reol-cat/forgot-password">Forgot Password?</a>
    </div>
</div>
