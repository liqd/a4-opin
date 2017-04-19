/* eslint-disable */
/* global $ Highcharts */

$(function () {
        var e = $('#result').get(0)
        var poll = JSON.parse(e.getAttribute('data-poll'))
        var pollresult = JSON.parse(e.getAttribute('data-poll-result'))

        if(pollresult.noOfReceivedResults && pollresult.noOfReceivedResults != 0){
            for(ind=0;ind<poll.questions.length;ind++){
                question = poll.questions[ind];
                var answer_text_list = [];
                var answer_percent_list = [];

                for(indc=0;indc<question.answers.length;indc++){
                    answer = question.answers[indc];
                    answer_text_list.push(answer.answerText);
                    var score = pollresult.pollResQuestions[ind].pollResultAnswers[indc].answerScore;
                    var percent = (score/pollresult.noOfReceivedResults)*100;
                    answer_percent_list.push(percent);
                }

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
                        max: 100
                    },
                    series: [{
                        name: 'Total: '+pollresult.noOfReceivedResults,
                        data: answer_percent_list
                    }]
                });
        }
    }
});
