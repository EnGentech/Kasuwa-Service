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

    let count = 0
    let totalAmount = 0
    
    function checkOut(){
        $('.summary_section span').text(count)
    }

    function same(){
        let cout = $('.summary_section span').text()
        let sCart = $('.gen_cart_items span').text()
        if (cout === sCart){
            $('#specialSelectAll input[type="checkbox"]').prop('checked', true)
        }
    }
    
    function display(){
        $('.payNow').show()
        $('.summary_section button').css('border-bottom', '3px solid black')
        $('.summary_section button').css('cursor', 'pointer')
    }
    function hideit(){
        $('.payNow').hide()
        $('.summary_section button').css('border-bottom', 'none')
        $('.summary_section button').css('cursor', 'not-allowed')
    }

    $('.cart_item_img input[type="checkbox"]').prop('disabled', true);
    function check_all(){
        $('.select_all input[type="checkbox"]').prop('checked', true)
        $('.cart_item_img input[type="checkbox"]').prop('checked', true);
        count = $('.select_all input[type="checkbox"]').prop('checked', true).length - 1
    }
    function uncheck_all(){
        $('.select_all input[type="checkbox"]').prop('checked', false)
        $('.cart_item_img input[type="checkbox"]').prop('checked', false);
    }

    $('.select_all input[type="checkbox"]').change(function () {
        var cartItemsDiv = $(this).closest('.cart_items');
        let price = $(this).closest('.description span').text()
        alert(price)
        
        if ($(this).is(':checked')) {
            cartItemsDiv.find('.cart_item_img input[type="checkbox"]').prop('checked', true);
            count += 1
            if (count > 0){
                display()
            }
            checkOut()
            same()
            
        } else {
            cartItemsDiv.find('.cart_item_img input[type="checkbox"]').prop('checked', false);
            $('#specialSelectAll input[type="checkbox"]').prop('checked', false)
            count -= 1
            if (count === 0){
                hideit()
            }
            checkOut()
        }
    });
    $('#specialSelectAll input[type="checkbox"]').change(function () {
        if ($(this).is(':checked')) {
            check_all()
            checkOut()
            if (count > 0){
                display()
            }
        } else {
            uncheck_all()
            count = 0
            checkOut() 
            hideit() 
        }
    });




    //This part integrates the computational analysis of amount to be paid//



});