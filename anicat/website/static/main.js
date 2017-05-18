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

$('#post-form').submit(function(event){
    var form = $('#post-form').serialize()
    event.preventDefault();
    $.ajaxSetup({
        type : 'POST',
        url  : "login/",
        data : form,
        success : function(data){
            if(data.success){
              $('#largeShoes').modal('hide');
              $('#new_user_form').trigger('reset');
              alert("logged in");
              location.reload();
            }
            else{
                alert("error");
            }
        }
      });
      $.ajax({});
});

$("#reg_id").change(function () {
    var form = {
        'username' : $('#reg_id').val(),
    };

      $.ajax({
        type : 'GET',
        url  : 'ajax/validate_username/',
        data : form,
        dataType : 'json',
        success : function(data){
            if(data.is_taken){
                alert("username is taken");
            }
        }
    });
});

$("#mail_id").change(function () {
    var form = {
        'email'    : $('#mail_id').val(),
    };

      $.ajax({
        type : 'GET',
        url  : 'ajax/validate_email/',
        data : form,
        dataType : 'json',
        success : function(data){
            if(data.is_taken){
                alert("email is taken");
            }
        }
    });
});

$('#new-user-form').submit(function(event){
    var form = $('#new-user-form').serialize()
    event.preventDefault();
    $.ajaxSetup({
        type : 'POST',
        url  : "user/create/",
        data : form,
        success : function(){
              $('#largeShoes').modal('hide');
              $('#new_user_form').trigger('reset');
              alert("Created New User");
        },
        error : function(){
            alert("error");
            $('#new_user_form').trigger('reset');
        }
      });
      $.ajax({});
});
