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

$('#new_user_form').submit(function(event){
    var form = {
        'username' : $('#reg_id').val(),
        'email'    : $('#mail_id').val(),
        'password' : $('#id_password').val(),
    };
    var csrftoken = getCookie('csrftoken')
    event.preventDefault();
    $.ajaxSetup({
        type : 'POST',
        url  : "user/create/",
        data : form,
        dataType : 'json',
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
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
function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
    return cookieValue;
}
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
