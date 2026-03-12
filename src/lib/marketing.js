// Marketing funnel configuration.
// Replace the placeholder URL below with your Brevo hosted sign-up form URL.
// Example: https://123abc.sibforms.com/serve/xxxx
export const BREVO_SIGNUP_URL = 'https://f4c90f0b.sibforms.com/serve/MUIFAAbBH-WyHvhepdhs6G8ul1wze6MjoVvTKJ8hy6wQ2pt2zfKhS72lm7K5SfgHHreybw_QGra18wfbFENLUX33U10YYUe1aPoQOEePElxdHbiM2uGL0Sdsei-N34xBCkoktWbqbtQe1cMW95PLNJ4gd9cZ_YonM0j3W1TrUXhliIJyTXuJ7u4B8pL9aH8uFVKQbzNfUWpWw_ovuA==';

export const FALLBACK_SIGNUP_URL = 'mailto:hello@sovren.software?subject=Esver%20OS%20Launch%20Notification';

export const ESVER_SIGNUP_URL = BREVO_SIGNUP_URL || FALLBACK_SIGNUP_URL;

export const HAS_EMBED_SIGNUP = ESVER_SIGNUP_URL.slice(0, 4) === 'http';
