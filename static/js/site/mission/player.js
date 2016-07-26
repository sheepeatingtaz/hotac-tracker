$(document).ready(function () {
    // Update table id: monthly-absences
    var csrftoken = Cookies.get('csrftoken');
    $('#next-turn').click(function () {
        $.ajax({
            url: $(this).attr('data-url'),
            method: "PUT",
            data: {
                turn: parseInt($(this).attr('data-turn')) + 1
            },
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (data) {
                alert(data.turn)
            }
        })
    });
    
});