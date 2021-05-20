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

//   const progressBar = document.getElementsByClassName('progress-bar')[0]
//     setInterval(() => {
//         const computedStyle = getComputedStyle(progressBar)
//         const width = parseFloat(computedStyle.getPropertyValue('width')) || 0
//         progressBar.style.setProperty('width', width + 0.1)
//     }, 3)


    