function user_login() {
  $(document).on('click', '#navbar button', (e) => {
    e.preventDefault();
    let action = $(e.target).attr('id');
    let form = $(document).find(`form[name=${action}-form]`);
    if ($(form).hasClass('d-none')) {
      $(form).removeClass('d-none');
    } else {
      $(form).addClass('d-none');
    }
  });

  $(document).on('click', '#send-form', (e) => {
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
          console.log(errors);
        } else {
          $(form).find('.auth-error').find('span').html(`<span>${errors.auth_error}<span>`);
        }
      },
    });
  });
}

export default user_login;
