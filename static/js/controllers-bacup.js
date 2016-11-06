
/* Controllers */


var LCtrl = myAppModule.controller("LeftCtrl", function($scope,$http){
    $scope.zarplata='50000';
    $scope.totalsumm=0;
    $scope.mdrange=0;
    $scope.mpmonth=["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"];
    $scope.LClick = function() {

            $http.post(djurl, {zarplata: $scope.zarplata,
                               startDate: $scope.mdStart,
                               endDate: $scope.mdEnd,
                               startYear:$scope.startYear,
                               endYear:$scope.endYear,
                               startmonthday: $scope.startmonthday,
                               endmonthday: $scope.endmonthday,

            }).success(function (response) {

                $scope.months = response.months;
                $scope.mdrange= response.mdrange;
                $scope.mdotpusk=response.mdotpusk;
                $scope.summotpusk=response.summotpusk;
                $scope.summotpusk1=response.summotpusk1;
                $scope.summotpusk2=response.summotpusk2;
                $scope.summmonth1=response.summmonth1;
                $scope.summmonth2=response.summmonth2;
                $scope.cenarabdnyainmonth1=response.cenarabdnyainmonth1;
                $scope.cenarabdnyainmonth2=response.cenarabdnyainmonth2;
                $scope.cenaotpusknogodnya=response.cenaotpusknogodnya;
                $scope.ostatokrabochihdneyinmonth1=response.ostatokrabochihdneyinmonth1;
                $scope.ostatokrabochihdneyinmonth2=response.ostatokrabochihdneyinmonth2;
                $scope.otpuskniedniinmonth1=response.otpuskniedniinmonth1;
                $scope.otpuskniedniinmonth2=response.otpuskniedniinmonth2;






            });



    };

    $scope.onlyNumbers = /^[0-9]+$/;

    $scope.changeDate=function(){
        $scope.mdStart=NumDay(
                    parseInt($scope.mDateRange.startDate.format('DD'),10),
                    parseInt($scope.mDateRange.startDate.format('MM'),10),
                    parseInt($scope.mDateRange.startDate.format('YYYY'),10)

                );
        $scope.startYear=parseInt($scope.mDateRange.startDate.format('YYYY'),10);
        $scope.mdEnd=NumDay(
                    parseInt($scope.mDateRange.endDate.format('DD'),10),
                    parseInt($scope.mDateRange.endDate.format('MM'),10),
                    parseInt($scope.mDateRange.endDate.format('YYYY'),10)

                )+1;
        $scope.endYear=parseInt($scope.mDateRange.endDate.format('YYYY'),10);
        $scope.mdrange = $scope.mdEnd - $scope.mdStart;
        $scope.startmonthday=NumDay(1,
                    parseInt($scope.mDateRange.startDate.format('MM'),10),
                    parseInt($scope.mDateRange.startDate.format('YYYY'),10)
                );
        $scope.endmonthday=NumDay(1,
                    parseInt($scope.mDateRange.endDate.format('MM'),10),
                    parseInt($scope.mDateRange.endDate.format('YYYY'),10)
                );
        $scope.month1=$scope.mpmonth[parseInt($scope.mDateRange.startDate.format('MM'),10)-1]
        $scope.month2=$scope.mpmonth[parseInt($scope.mDateRange.endDate.format('MM'),10)-1]
        $scope.viewmonths={};
        $scope.LClick();
    };



    $scope.validatenum = function(event){


    if ((event.keyCode < 17) || (event.keyCode > 57) || (event.shiftKey==true)||(event.keyCode==32)) {
        if((event.keyCode < 8)||(event.keyCode > 9)) {
            if ((event.keyCode < 96) || (event.keyCode > 105)){
            event.preventDefault();}}
    }
//    console.log(event);
    };


    $scope.summ = function(){
        var sum=0;
        for (var st in $scope.months){
            if ($scope.months[st].dox){
            sum += parseInt($scope.months[st].dox, 10);
            }
        }
        return sum;
    };
});

