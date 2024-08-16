import { API_URL } from '$lib/const';
import { getSessionCookie } from '$lib/cookies/sessionCookie';

export async function generateReportAPI(catAmount: number, shelterName: string, bodyContent: string): Promise<Response> {
	try {
		const token = getSessionCookie();
		const response = await fetch(`${API_URL}generate-report`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: 'Bearer ' + token
			},
            body: JSON.stringify({
                'cat_count': catAmount,
                'shelter_name': shelterName,
                'body_content': bodyContent
            })
		});
		return response
	} catch (error) {
		throw new Error('Error Generate Report: ' + (error as Error).message);
	}
}
