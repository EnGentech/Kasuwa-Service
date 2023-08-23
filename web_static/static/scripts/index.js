$(document).ready(function(){
    $('.account').hover(function(){
        $('.drop_down_acc').show()
    })
    $('.drop_down_acc').mouseleave(function(){
        $('.drop_down_acc').hide()
    })
})