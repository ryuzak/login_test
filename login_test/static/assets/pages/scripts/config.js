
var handleInputMasks = function () {
    $.extend($().inputmask.defaults, {
        'autounmask': true
    });

    $(".mask_phone").inputmask("mask", {"mask": "(999) 999-9999"}); //specifying fn & options
    $(".mask_number").inputmask({ "mask": "9", "repeat": 10, "greedy": false });  // ~ mask "9" or mask "99" or ... mask "9999999999"
    // $(".mask_decimal").inputmask('decimal', { rightAlignNumerics: false }); //disables the right alignment of the decimal input
    $(".mask_decimal").inputmask({'mask':"9{0,5}.9{0,2}", greedy: false}); 
    // $(".mask_currency").inputmask('999,999,999.99', { numericInput: true });
    $(".mask_currency").inputmask('decimal',
      { 'alias': 'currency',
        'groupSeparator': ',',
        'autoGroup': true,
        'digits': 2,
        'radixPoint': ".",
        'digitsOptional': false,
        'allowMinus': false,
        'placeholder': '0.00'
      }
    );
    // $(".mask_rfc").inputmask("mask", {"mask":"9-a{1,3}9{1,3}" });
}

 
 
$(document).ready(function() {

    
    if ($('.mask_phone').get(0) || $('.mask_number').get(0) || $('.mask_decimal').get(0) || $('.mask_currency').get(0)){
         handleInputMasks();
    }

     $('.mask_decimal').on('keyup', function(e) {
        if (!this.value.match(/^\d{0,5}(\.[0-9]{1,2})?$/)) {
            $(this).addClass('error');// adding error class
        } else {
            $(this).removeClass('error');// remove error class
        }
    });
    
});
