$(document).ready(function(){
    $('.billingAddress #btn2').click(function(){
        $('.billingAddress').hide()
        $('.addressList').show()
    })


    $('#useClass #btn1').click(function (event) {
      event.preventDefault();
     
      const formData = $('#myform').serialize();
      
      $.ajax({
        type: 'POST',
        url: '/kasuwa/cart/order/billingAddress',
        data: formData,
        success: function (response) {
          console.log(response);
          } 
            
        });

      $('#load').show()
      //$('.addressList').hide()
      $('.billingAddress').css('pointer-events', 'none')

      setTimeout(function(){
        location.reload()
      }, 3000);

      setTimeout(function(){
        $('.addressList').show()
        $('.addressList').css('backdrop-filter', 'brightness(30%)')
        $('body').css('overflow', 'hidden')
      }, 4000)
        
      });
      

      
})