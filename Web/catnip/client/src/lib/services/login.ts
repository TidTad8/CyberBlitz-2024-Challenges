import { API_URL } from "$lib/const";

export async function loginAPI(username: string, password: string) {
    try {
        const response = await fetch(`${API_URL}login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password,
            })
        });

        if (response.ok || (response.status >= 400 && response.status < 500)) {
            const data = await response.json();
            return data;
        } else {
            throw new Error('Login failed');
        }
    } catch (error) {
        throw new Error('Error login: ' + (error as Error).message);
    }
}
