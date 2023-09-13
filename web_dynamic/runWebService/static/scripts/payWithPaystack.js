$(document).ready(function(){

    function genran() {
        const min = 100000000000; // Smallest 12-digit number
        const max = 999999999999; // Largest 12-digit number
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    $('#placeOrder').click(function(){
        let amount = $('#total').text()
        let amt = parseFloat(amount.replace(/[^0-9]/g, ''));
        amt = Math.round(amt * 100)
        let email = $('#mail').text()

        let refree = genran()
        
        let handler = PaystackPop.setup({
            key: 'pk_test_18ed358a84c305a3340530bf43a9832fdef246f5',
            email: email,
            amount: amt,
            currency: 'NGN',
            ref: refree,
            callback: function (response) {
                var reference = response.reference;
                alert('Payment complete! Reference: ' + reference);
                // Make an AJAX call to your server with the reference to verify the transaction
            },
            onClose: function () {
                alert('Transaction was not completed, window closed.');
            },
        });
        handler.openIframe();

        
    })
})