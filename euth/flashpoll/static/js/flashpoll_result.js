/* eslint-disable */
/* global $ Highcharts */

$(function () {
        var e = $('#result').get(0)
        var poll = JSON.parse(e.getAttribute('data-poll'))
        var pollresult = JSON.parse(e.getAttribute('data-poll-result'))

        if(pollresult.noOfReceivedResults && pollresult.noOfReceivedResults != 0){            
            for(ind=0;ind<poll.questions.length;ind++){
                var question = questionAtIndex(poll, ind);      
                var questionResult = questionResultAtIndex(pollresult, ind);      
                
                if(question.questionType != 'FREETEXT'){
                var answer_text_list = [];
                var answer_percent_list = [];
                              
                for(indc=0;indc<question.answers.length;indc++){                    
                    answer = answerAtIndex(question, indc);
                    answerResult = answerResultAtIndex(questionResult, indc);                                    
                    answer_text_list.push(answer.answerText);

                    var score = pollresult.pollResQuestions[ind].pollResultAnswers[indc].answerScore;
                    var score = answerResult.answerScore;
                    
                    var percent;
                    var maxValue;
                        
                    if(question.questionType != 'ORDER'){
                        percent = (score/pollresult.noOfReceivedResults)*100;
                        maxValue = 100;
                    }else{                        
                        percent = (score/pollresult.noOfReceivedResults);
                        maxValue = question.answers.length + 1;
                    }
                    answer_percent_list.push(percent);
                }

                if(question.questionType != 'ORDER'){
                    var myChart = Highcharts.chart('container-'+question.orderId, {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: question.questionText
                        },
                        xAxis: {
                            categories: answer_text_list
                        },
                        yAxis: {
                            title: {
                                text: 'Percent'
                            },
                            max: maxValue
                        },
                        series: [{
                            name: 'Total: '+pollresult.noOfReceivedResults,
                            data: answer_percent_list
                        }]
                    });
                }else{
                    var myChart = Highcharts.chart('container-'+question.orderId, {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: question.questionText
                        },
                        xAxis: {
                            categories: answer_text_list
                        },
                        yAxis: {
                            title: {
                                text: 'Average score'
                            },
                            max: maxValue
                        },
                        series: [{
                            name: 'Total: '+pollresult.noOfReceivedResults,
                            data: answer_percent_list
                        }]
                    });                    
                }
            }
        }
    }
});


function questionAtIndex(poll, index) {    
    for(var ind=0;ind<poll.questions.length;ind++){        
        if(poll.questions[ind].orderId == index + 1){
            return poll.questions[ind];
        }
    }                
    return {};
}

function answerAtIndex(question, index) {
    for(var ind=0;ind<question.answers.length;ind++){        
        if(question.answers[ind].orderId == index + 1){
            return question.answers[ind];
        }
    }                
    return {};
}

function questionResultAtIndex(pollresult, index) {    
    for(var ind=0;ind<pollresult.pollResQuestions.length;ind++){        
        if(pollresult.pollResQuestions[ind].questionOrderId == index + 1){
            return pollresult.pollResQuestions[ind];
        }
    }                
    return {};
}

function answerResultAtIndex(pollResQuestion, index) {
    for(var ind=0;ind<pollResQuestion.pollResultAnswers.length;ind++){        
        if(pollResQuestion.pollResultAnswers[ind].answerOrderId == index + 1){
            return pollResQuestion.pollResultAnswers[ind];
        }
    }                
    return {};
}