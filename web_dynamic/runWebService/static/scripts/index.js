$(document).ready(function(){
    $('.account').hover(function(){
        $('.drop_down_acc').show()
    })
    $('.drop_down_acc').mouseleave(function(){
        $('.drop_down_acc').hide()
    })

    $('.category p').click(function(){
        let clas = $(this).attr('class')
        let catNam = $(this).attr('catName')
        $(".category input[name='cat_id']").val(clas)
        $(".category input[name='cat_name']").val(catNam)
        $(".category input[type='submit']").click()
    })

})