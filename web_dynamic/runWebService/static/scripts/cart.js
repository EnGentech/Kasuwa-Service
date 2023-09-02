$(document).ready(function() {
    $('[del]').click(function() {
        let del = $(this).text().trim()
        
        $.ajax({
            url: '/kasuwa/cart/delete',
            method: 'POST',
            data: {delid: del},
            success: function(response){
                alert("Successfully deleted from cart")
                location.reload()
            }
        })

    });
});