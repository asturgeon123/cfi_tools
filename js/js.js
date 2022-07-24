

function round(value, precision) {
    var multiplier = Math.pow(10, precision || 0);
    return Math.round(value * multiplier) / multiplier;
}


$("form").submit(function(event) {
      var student_name = $("#studentName").val();
      var location = $("#location").val();
      var payment_type = $("#paymentType").val();

      var plane = $("#plane").val();
      var hobbsin = $("#hobbsIn").val();
      var hobbsout = $("#hobbsOut").val();
      var ground_start = $("#groundStart").val();
      var ground_stop = $("#groundEnd").val();
      var product_name = $("#productName").val();
      var productprice = $("#productPrice").val();

      var takeoffs = $("#takeoffs").val();
      var landings = $("#landings").val();
      var Route = $("#Route").val();
      var TT = $("#TT").val();
      var PIC = $("#PICDUEL").val();
      var DUEL = $("#DUEL").val();
      var XC = $("#XC").val();
      var NIGHT = $("#NIGHT").val();




      console.log('Generating PDF')

      $.ajax({
          type: "POST",
          url: "/pdf_gen",
          data: JSON.stringify ({ground_instruction_rate:"50",flight_instruction_rate:"50",remos_block10_rate:"110",remos_block5_rate:"115",remos_hourly_rate:"120",cfi_name:"Alex Sturgeon","student_name":student_name,'destination':location,'payment_method':payment_type,'tailnumber':plane,'hobbs_in':hobbsin,'hobbs_out':hobbsout,'ground_start':ground_start,'ground_stop':ground_stop,'product_name':product_name,'productprice':productprice,'takeoffs':takeoffs,'landings':landings,'Route':Route,'TT':TT,'PIC':PIC,'DUEL':DUEL,'XC':XC,'NIGHT':NIGHT}),
          success: function(response){
            //alert(data)
            console.log(response)
            window.open('/pdf');
          },
          dataType: "json",
          contentType : "application/json"
        });
      event.preventDefault(); 
     });


var input_items = $( ".auto_move_cursor" ).map(function() {return this.id;})
console.log(input_items)
console.log(typeof(input_items))

//Automatically add decimal place
$(".auto_decimal").keyup(function () {
    if (this.value.length == this.maxLength-2) {
      console.log(this.value.length)

      $(this).val(function() {
        if (this.value.includes('.')) {
          console.log("")
        } else {
          return this.value + '.';
        }
        })

      //let index = input_items.indexOf(this.id);
      //$("#"+input_items[index]).focus();
    }
});

//Automatically Move Input
$('input').keyup(function(){
  if($(this).val().length==$(this).attr("maxlength")){
        var tabIndex = +$(this).attr('tabindex');
        $('[tabindex=' + (+tabIndex+1) + ']').focus();
  }
});


//setup before functions
var typingTimer;                //timer identifier
var doneTypingInterval = 4000;  //time in ms, 5 seconds for example
var $input = $('#hobbsOut');

//on keyup, start the countdown
$input.on('keyup', function () {
  clearTimeout(typingTimer);
  typingTimer = setTimeout(doneTyping, doneTypingInterval);
  //console.log("timer Started")
});

//on keydown, clear the countdown 
$input.on('keydown', function () {
  clearTimeout(typingTimer);
});

//user is "finished typing," do something
function doneTyping () {
  //console.log("Done Typing")

  var hob1 = parseFloat($('#hobbsOut').val())
  var hob2 = parseFloat($('#hobbsIn').val())
  console.log(hob1)
  var hobbs_total = round(hob2 - hob1,1)
  
  $('#TT').val(function() {
        return this.value + hobbs_total;})
    $('#PIC').val(function() {
        return this.value + hobbs_total;})
      $('#DUEL').val(function() {
        return this.value + hobbs_total;})
}





