import { API_URL } from '$lib/const';
import { getSessionCookie } from '$lib/cookies/sessionCookie';

export async function tokenCheckAPI() {
	try {
        const token = getSessionCookie();
		const response = await fetch(`${API_URL}token-check`, {
			method: 'GET',
			headers: {
                'Authorization': 'Bearer ' + token
			}
		});

		if (response.ok || (response.status >= 400 && response.status < 500)) {
			const data = await response.json();
			return data;
		} else {
			throw new Error('Failed check token');
		}
	} catch (error) {
		throw new Error('Error check token: ' + (error as Error).message);
	}
}