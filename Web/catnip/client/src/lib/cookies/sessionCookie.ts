import Cookies from 'js-cookie';

export const getSessionCookie = () => Cookies.get('session_token');

export const setSessionCookie = (sessionToken: string, expireInHours = 1) => {
    const expirationDate = new Date(new Date().getTime() + expireInHours * 60 * 60 * 1000);
    Cookies.set('session_token', sessionToken, { expires: expirationDate, sameSite: 'strict' });
};

export const removeSessionCookie = () => Cookies.remove('session_token', { sameSite: 'strict' });
