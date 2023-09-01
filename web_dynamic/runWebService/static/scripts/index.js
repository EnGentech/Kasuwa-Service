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

    $('.row').click(function(){
        let name = $(this).find('p#name').text()
        let description = $(this).find('p#flow').text()
        let naira = $(this).find('h4#naira').attr('naira')
        let kobo = $(this).find('span#kobo').attr('kobo')
        let stock = $(this).find('p#stock').attr('stock')
        $(".hide input[name='name']").val(name)
        $(".hide input[name='description']").val(description)
        $(".hide input[name='naira']").val(naira)
        $(".hide input[name='kobo']").val(kobo)
        $(".hide input[name='stock']").val(stock)
        $('.hide input[type="submit"]').click() 
    })

})