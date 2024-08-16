import { API_URL } from '$lib/const';
import { getSessionCookie, removeSessionCookie } from '$lib/cookies/sessionCookie';

export async function logoutAPI() {
	try {
        const token = getSessionCookie();
		const response = await fetch(`${API_URL}logout`, {
			method: 'POST',
			headers: {
                'Authorization': 'Bearer ' + token
			}
		});

		if (response.ok || (response.status >= 400 && response.status < 500)) {
            removeSessionCookie()
			return true 
		} else {
			throw new Error('Logout failed');
		}
	} catch (error) {
		throw new Error('Error logout: ' + (error as Error).message);
	}
}