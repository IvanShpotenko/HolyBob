var searchApp = angular.module('searchApp',[]);

searchApp.controller('MainCtrl',
    function($scope, $http) {

        $scope.chatMessages = [
            {user: 'Chatbot', text: 'Hi! Enter your name, your holiness!'}
        ];

        $scope.sendMessage = function(text) {
            if (!text) return;
            $scope.chatMessages.push({user: 'You', text: text});
            $http.post('/response', {text: text}).then(function(res) {
                console.log(res.data.response);
                $scope.chatMessages.push({user: 'Chatbot', text: res.data.response});

        });};

});