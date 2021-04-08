function _selectDate(e) {

    console.log(e)
    // console.log('--------------------------------------')


    $.ajax({
        url: '/selectDate',
        data: $('form').serialize(),
        type: 'POST', 
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    });

  }