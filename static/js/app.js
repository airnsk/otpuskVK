var myAppModule = angular.module('myAppModule', ['ngBootstrap']);

myAppModule.config(['$httpProvider', function($httpProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
]);