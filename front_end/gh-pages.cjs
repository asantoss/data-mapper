var ghpages = require('gh-pages');

ghpages.publish(
	'build', // path to public directory
	{
		branch: 'gh-pages',
		repo: 'https://github.com/asantoss/data-mapper.git', // Update to point to your repository
		user: {
			name: 'Alexander Santos', // update to use your name
			email: 'alexsantosantana@live.com' // Update to use your email
		}
	},
	() => {
		console.log('Deploy Complete!');
	}
);
