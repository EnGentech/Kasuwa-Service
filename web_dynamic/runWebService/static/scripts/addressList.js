$(document).ready(function() {
    $('.selectedAddress').click(function() {
        if ($(this).is(':checked')) {
            let userChoice = $(this).closest('.address').find('.contact')
            let clonedAddress = userChoice.clone()
            $('#usedAddress').replaceWith(clonedAddress)

            localStorage.setItem('clonedAddress', clonedAddress.html());

            $('#lod').show()
            //$('.addressList').hide()
            $('.addressList').css('pointer-events', 'none')

            setTimeout(function(){
                location.reload()
            }, 500);
        }
    });
});

$(document).ready(function() {
    let storedAddress = localStorage.getItem('clonedAddress');
    if (storedAddress) {
        $('#usedAddress').html(storedAddress);
    }
});
