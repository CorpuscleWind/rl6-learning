function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function serializeForm(form) {
    var data = $(form).serializeArray();
    var result = {};
    for (var i = 0; i < data.length; i++) {
        result[data[i].name] = data[i].value;
    }
    result['csrfmiddlewaretoken'] = getCookie('csrftoken');
    return result;
}

function processResponse(response, form) {
    if(response.status == "OK") {
        location.reload();
    } else {
        $('html, body').animate({ scrollTop: $(form).offset().top }, 'slow');
        var errors = response.message;
        for(var field in errors) {
            if (errors.hasOwnProperty(field)) {
                var errorDiv = '<div class="form-error">' + errors[field] + '</div>';
                if(field == '__all__') {
                    $(form).prepend(errorDiv);
                } else {
                    $('[name="' + field + '"]').after(errorDiv);
                }
            }
        }
    }
}

function clearErrors() {
    $('div.form-error').remove();
}

function ajaxOnFormSubmit(formSelector) {
    clearErrors();
    var url = $(formSelector).attr('action');

    $.post({
        url: url,
        data: serializeForm(formSelector),
        success: function (response) {
            processResponse(response, formSelector);
        }
    })
}

$('form#login-form').on('submit', function(event) {
    event.preventDefault();
    ajaxOnFormSubmit(this);
});

$('form#registration-form').on('submit', function(event) {
    event.preventDefault();
    ajaxOnFormSubmit(this);
});

$('form#test-form').on('submit', function(event) {
    event.preventDefault();
    ajaxOnFormSubmit(this);
});

$('form#feedback-form').on('submit', function(event) {
    event.preventDefault();
    ajaxOnFormSubmit(this);
});