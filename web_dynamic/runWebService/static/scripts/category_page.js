$(document).ready(function(){
$('.manhattan--container').click(function(){
    let prodID = $(this).find('p#prodID').text()
    $(".hide input[name='prodID']").val(prodID)
    $('.hide input[type="submit"]').click() 
})

})