import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const theme = writable('system');

theme.subscribe((value) => {
	if (browser) {
		switchTheme(value);
	}
});

function switchTheme(value: String) {
	// Whenever the user explicitly chooses light mode
	localStorage.theme = value;
	if (value === 'system') {
		// Whenever the user explicitly chooses to respect the OS preference
		localStorage.removeItem('theme');
	}
	// if set via local storage previously
	if (
		localStorage.theme === 'dark' ||
		(!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
	) {
		document.documentElement.classList.add('dark');
	} else {
		document.documentElement.classList.remove('dark');
	}
}

export type Column = {
	name: string;
	value: string;
	deleted: boolean;
};
type CSVStore = {
	columns: Column[];
	rows: { [key: string]: any }[];
};
const csvStore: CSVStore = {
	columns: [],
	rows: []
};

const parserStore = writable(csvStore);

export { theme, parserStore };
