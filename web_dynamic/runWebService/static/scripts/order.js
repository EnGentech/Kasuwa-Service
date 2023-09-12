$(document).ready(function(){
   $('#close').click(function(){
    $('.addressList').hide()
    $('body').css('overflow-y', 'scroll')
   })

   $('#closeBillingAddress').click(function(){
    location.reload()
    
    setTimeout(function(){
        $('#change').click()
    }, 3000);
    
   }) 
   
   let availAddress = $('#yes').text()
   if (availAddress > 0){
    $('#useClass').addClass('billingAddress')
   } else {
    $('#useClass').addClass('nobillingAddress')
    $('.addressList').hide()
    $('body').css('overflow', 'hidden')
    $('.nobillingAddress').css('backdrop-filter', 'brightness(30%)')
   }

   $('#placeOrder').click(function(){
    $('.placeOrders').show()
    $('.placeOrders').css('backdrop-filter', 'brightness(30%)')
    $('body').css('overflow', 'hidden')
   })

})