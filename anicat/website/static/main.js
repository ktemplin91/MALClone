// Submit post on submit
//$('#post-form').on('submit', function(event){
//    event.preventDefault();
//    console.log("form submitted!")  // sanity check
//    create_post();
//});


// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    console.log($('#post-text').val())
};


$("#post-form").change(function () {
      var username = $(this).val();

      $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists.");
          }
        }
      });

    });