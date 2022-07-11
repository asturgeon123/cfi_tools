




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

      console.log('Generating PDF')

      $.ajax({
          type: "POST",
          url: "/pdf_gen",
          data: JSON.stringify ({remos_block10_rate:"110",remos_block5_rate:"115",remos_hourly_rate:"120",cfi_name:"Alex Sturgeon","student_name":student_name,'destination':location,'payment_method':payment_type,'tailnumber':plane,'hobbs_in':hobbsin,'hobbs_out':hobbsout,'ground_start':ground_start,'ground_stop':ground_stop,'product_name':product_name,'productprice':productprice}),
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








