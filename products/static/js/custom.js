$(document).ready(function () {
    $('#increment-btn').click(function (e) {
        e.preventDefault();
        var inc_value = $(this).closest('#product_data').find('#qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value)  ? 0: value;
        if(value < 10 ){
            value++;
            $(this).closest('#product_data').find('#qty-input').val(value);
        }
    });
    $('#decrement-btn').click(function (e) {
        e.preventDefault();
        var dec_value = $(this).closest('#product_data').find('#qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value)  ? 0: value;
        if(value > 1 ){
            value--;
            $(this).closest('#product_data').find('#qty-input').val(value);
        }
    });

   
});
$(document).ready(function () {
    $("#addtocartbtn").click(function (event){
        event.preventDefault();

        var product_id = $("#prod_id").val()
        var product_qty = $("#qty-input").val()
        

        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
          
            success: function (response){
                 console.log(response)
                 console.log(product_id)
                 console.log(product_qty)
                 alertify.success(response.status)
            }


        });
    });
   
});
// update cart
$(document).ready(function () {
    $('.changequantity').click(function (e){
        e.preventDefault();

        var product_id =$('#prod_id').val();
        var product_qty = $('#qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
          
            success: function (response){
                 console.log(response)
                 alertify.success(response.status)
            }


        });
    });
});
// delete cart item
$(document).ready(function () {
    $(document).on('click','#delete-cart-item', function (e){
        e.preventDefault();
        var product_id = $('#prod_id').val();
        

        $.ajax({
            method: "POST",
            url: "/deletecartitem",
            data: {
                'product_ids': product_id,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
          
            success: function (response){
                 console.log(response)
                 alertify.success(response.status)
                 $('#cartdata').load(location.href + " #cartdata");
            }


        });
    });
    
});
$(document).ready(function () {
    $('#addtowishlist').click(function (e){
        e.preventDefault();

        var product_id = $('#prod_id').val();
       
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
          
            success: function (response){
                 console.log(response)
                 alertify.success(response.status)
            }


        });
    });
});
// delte wishlist item
$(document).ready(function () {
    $(document).on('click','#deletewishlistitem', function (e){
        e.preventDefault();
        var product_ids = $(this).closest('#wishitem').find('#prods_id').val();
       

        $.ajax({
            method: "POST",
            url: "/deletewishlistitem",
            data: {
                'products_ids': product_ids,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()

            },
          
            success: function (response){
                 console.log(response)
                 console.log(product_id)
                 alertify.success(response.status)
                 $('#wishdata').load(location.href + " #wishdata");
            }
           

        });
    });
});