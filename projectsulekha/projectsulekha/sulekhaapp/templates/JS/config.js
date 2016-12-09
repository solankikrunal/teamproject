sulekha.config(function($stateProvider,$urlRouterProvider){
		$urlRouterProvider.otherwise('/index');
		$stateProvider
			.state('index', {			//By default Home page
				url:'/index',
				templateUrl: 'index.html',
				//controller:'homeCtrl'
			})

			.state('loginPage', {		//Navigate to login page
				url:'/login',
				templateUrl: 'loginPage.html',
				controller: 'loginCtrl'
			})
			
		});
