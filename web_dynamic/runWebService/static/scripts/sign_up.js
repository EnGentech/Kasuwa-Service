$(document).ready(function () {
    $('#con_pass').on({
      input: function () {
        comparePasswords();
      },
      mouseleave: function () {
        comparePasswords();
      }
    });
  
    function comparePasswords () {
      const pass_val = $('#pass').val();
      const compare_pass = $('#con_pass').val();
  
      if (pass_val !== compare_pass) {
        $('#con_pass').css('border-color', 'red');
        $('#registerBtn').prop('disabled', true);
        $('#registerBtn').css('background-color', 'red').css('color', 'white');
        $('#registerBtn').val('Check password');
        $("#registerBtn").css('cursor', 'not-allowed')
      } else {
        $('#con_pass').css('border-color', '');
        $('#registerBtn').prop('disabled', false);
        $('#registerBtn').css('background-color', '').css('color', '');
        $('#registerBtn').css('background-color', '');
        $('#registerBtn').val('Submit');
        $("#registerBtn").css('cursor', 'pointer')
      }
    }
  });