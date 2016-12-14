var app = angular.module('myApp', []);
app.controller('loginCtrl', function($scope){
$scope.registerDiv = false;
    $scope.register = function(){
    	$scope.registerDiv = true;
    }

 });