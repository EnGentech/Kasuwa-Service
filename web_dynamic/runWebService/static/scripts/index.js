$(document).ready(function(){
    $('.account').hover(function(){
        $('.drop_down_acc').show()
    })
    $('.drop_down_acc').mouseleave(function(){
        $('.drop_down_acc').hide()
    })

    $('.cat_prod2').click(function(){
       execute()
    })

    function execute(){
        fetch('/kasuwa/category/products', {
            method: 'POST'
        }).then(function(response) {
            if (response.ok){
                console.log('success')
            } else {
                alert('failure')
            }
        })
    }

})