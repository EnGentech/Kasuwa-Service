$(document).ready(function(){

  let amountText = $('.integer').text()
  let a_mount = amountText.replace(/,/g, '');
  let amount = parseInt(a_mount, 10);
  new_amount = amount
  
  $('span#ammount').text(amount.toLocaleString())


  let koboText = $('.kobo').text()
  let kobo = parseInt(koboText, 10);
  new_kobo = kobo
 
  if (kobo < 9){
  $('span#kobo').text('0' + kobo.toLocaleString())
  } else {
    $('span#kobo').text(kobo.toLocaleString())
  }


  $('i#plus').click(function(){
    $('#minus').css('cursor', 'pointer')
    let qtity = parseInt($('p#qty').text(), 10)
    qtity += 1
    $('p#qty').text(qtity)
    new_amount += amount
    new_kobo += kobo
    if (new_kobo < 10){
      $('span#kobo').text("0" + new_kobo.toLocaleString())
    } else {
      $('span#kobo').text(new_kobo.toLocaleString())
    }
    $('span#ammount').text(new_amount.toLocaleString()) 
    
  })




  $('#minus').click(function(){
    let qtity = parseInt($('p#qty').text(), 10)
    if (qtity > 1){
      $('#minus').css('cursor', 'pointer')
      qtity -= 1
      $('p#qty').text(qtity)

      new_amount -= amount
      new_kobo -= kobo
      if (new_kobo < 10){
        $('span#kobo').text("0" + new_kobo.toLocaleString())
      } else {
        $('span#kobo').text(new_kobo.toLocaleString())
      }
      $('span#ammount').text(new_amount.toLocaleString())   
    
    } else {
      $('#minus').css('cursor', 'not-allowed')
    }
  })
 
 
  $('#addToCart').click(function(){
    let id = $('#productid').text()
    let qty = $('#qty').text()
    let counter = parseInt(sessionStorage.getItem('count')) || 0
    counter += 1
    sessionStorage.setItem('count', counter)
    $('#cartCount').show()
    $('#cartCount').text(counter)
    
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