function user_login() {

  $(document).on('click', '#sent-form', (e) => {
    e.preventDefault();
    let form = $(e.target).closest('form');
    let formData = new FormData(form[0]);
    let action = $(form).data('action');
    formData.set('action', action);

    $.ajax({
      url: '/login/',
      type: 'POST',
      data: formData,
      processData: false,
      contentType: false,
      mimeType: 'multipart/form-data',
      success: (resp) => {
        let response = $.parseJSON(resp).payload;
        window.location.href = response['target'];
      },
      error: (err) => {
        let errors = $.parseJSON(err.responseText).errors;
        if (!errors.auth_error) {
          for (let k in errors) {
            $(document).find(`[name=${k}]`).addClass('invalid');
            $(document).find(`[name=${k}]`).closest('.input-field').find('.helper-text').attr('data-error', errors[k]);
          }
        } else {
          $(form).find('.auth-error').find('span').html(`<span>${errors.auth_error}<span>`);
        }
      },
    });
  });

  $(document).on('click', '.social', (e) => {
    e.preventDefault();
    let target = $(e.target).data('target');
    $.get(`/social/${target}/`, {}, (resp) => {
      window.location.href = resp;
    }).fail((error) => {
      console.log(error);
    });
  });
}

export default user_login;
