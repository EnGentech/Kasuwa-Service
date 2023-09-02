$(document).ready(function(){
  $('#addToCart').click(function(){
    let id = $('#productid').text()
    let qty = $('#qty').text()
    
    $.ajax({
        url: '/kasuwa/cart',
        method: 'POST',
        data: {productid: id, quantity: qty},
        success: function(response){
            alert("Successfully added to cart")
        }
    })
  })
})