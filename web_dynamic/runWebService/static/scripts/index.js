$(document).ready(function(){
    let a = 0
    $('.account').hover(function(){
        $('.drop_down_acc').show()
        a = 1
    })
    $('.account').click(function(){
        $('.drop_down_acc').show()
        a = 1
    })
    $('.drop_down_acc').mouseleave(function(){
        $('.drop_down_acc').hide()
    })
    
    $('body').click(function(){
        if (a == 1){
            $('.drop_down_acc').hide()
        }
    })

    $('.category p').click(function(){
        let clas = $(this).attr('class')
        let catNam = $(this).attr('catName')
        $(".hidden input[name='cat_id']").val(clas)
        $(".hidden input[name='cat_name']").val(catNam)
        $(".hidden input[type='submit']").click()
    })

    $('.row').click(function(){
        let prodID = $(this).find('p#prodID').text()
        $(".hide input[name='prodID']").val(prodID)
        $('.hide input[type="submit"]').click() 
    })

})