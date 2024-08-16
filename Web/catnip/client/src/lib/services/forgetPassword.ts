import { API_URL } from '$lib/const';

export async function forgetPasswordAPI(email: string) {
	try {
		const response = await fetch(`${API_URL}forgot-password`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email: email
			})
		});

		if (response.ok || (response.status >= 400 && response.status < 500)) {
			const data = await response.json();
			return data;
		} else {
			throw new Error('Forgot Password failed');
		}
	} catch (error) {
		throw new Error('Error Forgot Password: ' + (error as Error).message);
	}
}
