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

    function amt() {
        totalAmount = 0;

        // Iterate through each checked cart item
        $('.cart_items .select_all input[type="checkbox"]:checked').each(function () {
            let a_mount = $(this).closest('.cart_items').find('.description span').text();
            let qty = $(this).closest('.cart_items').find('.plus #qty').text();
            let amount = parseInt(a_mount.replace(/,/g, ''), 10);
            amount = amount * qty
            totalAmount += amount;
        });

        // Display the total amount
        $('.summary_section #total').text('NGN ' + totalAmount.toLocaleString())
        $('.payNow #grandTotal').text('NGN ' + totalAmount.toLocaleString())
    }
    
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
        
        if ($(this).is(':checked')) {
            cartItemsDiv.find('.cart_item_img input[type="checkbox"]').prop('checked', true);
            count += 1
            if (count > 0){
                display()
            }
            checkOut()
            same()
            amt()
        } else {
            cartItemsDiv.find('.cart_item_img input[type="checkbox"]').prop('checked', false);
            $('#specialSelectAll input[type="checkbox"]').prop('checked', false)
            count -= 1
            if (count === 0){
                hideit()
            }
            checkOut()
            amt()
        }
    });
    $('#specialSelectAll input[type="checkbox"]').change(function () {
        if ($(this).is(':checked')) {
            check_all()
            checkOut()
            amt()
            if (count > 0){
                display()
            }
        } else {
            uncheck_all()
            count = 0
            checkOut() 
            hideit() 
            amt()
        }
    });




    //This part integrates the computational analysis of amount to be paid
    //store product id's of selected iteration into a list 
    let ids = []
    let qttys = []
    let getAmount = ''

    function ordered() {
        $('.cart_items_description').each(function() {
            const checkboxes = $(this).find('input[type="checkbox"]:checked');
            if (checkboxes.length > 0) {
                let id = ($(this).find('.delid').text());
                let qtty = ($(this).find('#qty').text());
                getAmount = $('#grandTotal').text()
                //alert(keypair)
                ids.push(id)
                qttys.push(qtty)
            }
        });
        let idString = ids.join(',')
        $('#order').val(idString)
        $('#payNow').val(getAmount)
        $('#quantity').val(qttys)
        $('#submitme').click()
        
        /*$.ajax({
            url: '/kasuwa/cart/order',
            method: 'POST',
            data: {orderedList: idString},
            success: function(response){
                console.log('Success')
            }
        })*/
        //I will take it from here
    }

    function check(){
        let orderedItems = $('#NO').text()
        if (orderedItems > 0){
            ordered()
        } else {
            alert("Select at least an item")
        }
    }

    $('#checkOut').click(function(){
        check()
        /*let numb = $('#NO').text()
        if (numb == 0){
            $('#NoItems').removeAttr('href')
        } else {
            let value = $('#NoItems').attr('href')
            value = value.replace('0', numb)
            $('#NoItems').attr('href', value)
            
        }*/
    })

    $('#change').click(function(){
        $('.addressList').show()
        $('.addressList').css('backdrop-filter', 'brightness(30%)')
        $('body').css('overflow', 'hidden')
    })

    $('.submitBut #btn1').click(function(){
        $('.billingAddress').show()
        $('.addressList').hide()
        $('.billingAddress').css('backdrop-filter', 'brightness(30%)')
        $('body').css('overflow', 'hidden')
    })

});