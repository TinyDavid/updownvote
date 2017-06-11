$(document).ready(function() {
    $('.votes .vote-up, .votes .vote-down').click(function() {
        
        var vote_element = $(this),
            div = vote_element.parent(),
            vote_type = vote_element.is(".vote-up") ? "positive" : "negative",
            id = div.attr("topic-id");

        $.ajax({
             type:"POST",
             url:"vote",
             data: {id:id, type:vote_type},
             success: function(response){
                 if (Number.isInteger(parseInt(response, 10))) {
                    var votes_number = div.find(".num");
                    votes_number.html(response);
                }
             }
        });
    });
});