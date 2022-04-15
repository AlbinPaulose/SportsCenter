$('.addtocart').click(function (e){
    const url = $("#details").attr("data-cart-url");
    e.preventDefault();

    //var productid = $(this).closest('.product_box').find('.productId').val();
    var productid = $('.productId').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    console.log('older');
    console.log(productid);
    $.ajax({
        method: "POST",
        url: url,
        data: {
            'product_id':productid,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            let addToCartResult= response
            if(typeof(response)=='string')
            {
                addToCartResult= JSON.parse(response)
            }
            console.log(typeof(addToCartResult))
            alertify.success(addToCartResult.status)

        }

    });
});



$('.cartbtn').click(function (e){
    const url = $("#cartDetails").attr("data-cart-url");
    e.preventDefault();

    //var productid = $(this).closest('.product_box').find('.productId').val();
    var productid = $('.newProductId').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    console.log('newer');
    console.log(productid);
    $.ajax({
        method: "POST",
        url: url,
        data: {
            'product_id':productid,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            let addToCartResult= response
            if(typeof(response)=='string')
            {
                addToCartResult= JSON.parse(response)
            }
            alertify.success(addToCartResult.status)

        }

    });
});

/* TO UPDATE QUANTITY IN CART PAGE */

$(".cartTable .cartRow .qty").change(function (){
    var pid = $(this).closest('tr').find('input[name=productId]').val();
    var qty = $(this).closest('tr').find('input[name=quantity]').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    console.log(pid);
    console.log(qty);
    $.ajax({
        method: "POST",
        url: "update_quantity",
        data: {
            'product_id':pid,
            'quantity':qty,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            var cartUpadte = response;
            if(typeof(cartUpadte)=='string')
            {
                cartUpadte = JSON.parse(response)
            }
            console.log(cartUpadte);
            if(cartUpadte.status == "success")
            {
                location.reload();
            }
            else if(cartUpadte.status == "unsuccessful")
            {
                alert(cartUpadte.message);
                location.reload();
            }
            else if(cartUpadte.status == "nostock")
            {
                alert(cartUpadte.message);
                location.reload();
                alertify.success(cartUpadte.message);
            }
            // let cartUpdate= response
            // if(cartUpdate=='string')
            // {
            //     cartUpdate= JSON.parse(response)
            // }
            // alertify.success(cartUpdate.status)
            // location.reload();
        }

    });
});


/* FOOTBALL BOOKING PAGE, LOAD AVAILABLE TIME SLOT */
function footballDateFunction(){
    const url = $("#book").attr("data-date-url");
    const dateValue = $("#book").find('input[name=book_date]').val();
    $.ajax({                       
    url: url,                    
    data: {
        'date_value': dateValue       
    },
    success: function (data) {   
        let html_data = '<option value="">Available Time Slots</option>';
        data.forEach(function (times) {
            html_data += `<option value="${times.time_slot}">${times.time_slot}</option>`
        });
        $("#timeslot").html(html_data);
        }
    });
}

/*TO GET CORRESPONDING PRICE OF TIME SLOTS IN FOOTBALL TURF */
function footballTimeFunction(){
    const url = $("#book").attr("data-price-url");
    const timeId = $("#book").find('select[name=hour_preference]').val();
    $.ajax({                       
    url: url,                    
    data: {
        'time_id': timeId       
    },
        success: function (price) {   
            $('#price').val(price);
        }
    });
}

/* SHUTTLE BOOKING PAGE, LOAD AVAILABLE TIME SLOT */
function shuttleDateFunction(){
    const url = $("#book_shuttle").attr("data-date-url");
    const dateValue = $("#book_shuttle").find('input[name=book_date]').val();
    $.ajax({                       
    url: url,                    
    data: {
        'date_value': dateValue       
    },
    success: function (data) {   
        let html_data = '<option value="">Available Time Slots</option>';
        data.forEach(function (times) {
            html_data += `<option value="${times.time_slot}">${times.time_slot}</option>`
        });
        $("#timeslot").html(html_data);
        }
    });
}

/*TO GET CORRESPONDING PRICE OF TIME SLOTS IN FOOTBALL TURF */
function shuttleTimeFunction(){
    const url = $("#book_shuttle").attr("data-price-url");
    const timeId = $("#book_shuttle").find('select[name=hour_preference]').val();
    $.ajax({                       
    url: url,                    
    data: {
        'time_id': timeId       
    },
        success: function (price) {   
            $('#price').val(price);
        }
    });
}


/* CRICKET BOOKING PAGE, LOAD AVAILABLE TIME SLOT */

function cricketDateFunction(){
    console.log('cricket');
    const url = $("#book_cricket").attr("data-date-url");
    const dateValue = $("#book_cricket").find('input[name=book_date]').val();
    $.ajax({                       
    url: url,                    
    data: {
        'date_value': dateValue       
    },
    success: function (data) {   
        let html_data = '<option value="">Available Time Slots</option>';
        data.forEach(function (times) {
            html_data += `<option value="${times.time_slot}">${times.time_slot}</option>`
        });
        $("#timeslot").html(html_data);
        }
    });
}


/*TO GET CORRESPONDING PRICE OF TIME SLOTS IN CRICKET TURF */
function cricketTimeFunction(){
    const url = $("#book_cricket").attr("data-price-url");
    const timeId = $("#book_cricket").find('select[name=hour_preference]').val();
    $.ajax({                       
    url: url,                    
    data: {
        'time_id': timeId       
    },
        success: function (price) {   
            $('#price').val(price);
        }
    });
}






        