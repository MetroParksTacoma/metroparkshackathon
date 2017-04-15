
angular.module('mpt', ['ui.router', 'ngResource'])
	.config(function($stateProvider, $urlRouterProvider) {

		$urlRouterProvider.otherwise('/app/home');

		$stateProvider
			.state('app', {
				url: '/app',
				templateUrl: '/templates/app.html',
				abstract: true
			})
			.state('app.home', {
                                parent: 'app',
				url: '/home',
				templateUrl: '/templates/home.html',
				controller: HomeController,
				controllerAs: 'vm',
		         })
			.state('app.activities', {
                                parent: 'app',
				url: '/activities',
				templateUrl: '/templates/activities.html',
				controller: ActivitiesController,
				controllerAs: 'vm',
		         })
			.state('app.parks', {
                                parent: 'app',
				url: '/parks',
				templateUrl: '/templates/parks.html',
				controller: ParksController,
				controllerAs: 'vm',
		         });
	});

function HomeController(){};
function ActivitiesController(){};
function ParksController(){};
