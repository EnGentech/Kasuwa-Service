$(document).ready(function(){
   $('#close').click(function(){
    $('.addressList').hide()
    $('body').css('overflow', 'scroll')
   })

   $('#closeBillingAddress').click(function(){
    location.reload()
    
    setTimeout(function(){
        $('#change').click()
    }, 3000);
    
   })   


})