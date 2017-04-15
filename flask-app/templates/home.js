angular.module('mpt')
	.config(function($stateProvider) {

	$stateProvider
		.state('app.home', {
			url: '/home',
			templateUrl: '/templates/home.html',
			controller: HomeController,
			controllerAs: 'vm',
			resolve: {
				
			}
		});

	});

function HomeController(){};
