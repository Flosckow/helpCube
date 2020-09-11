import { getCsrfToken } from './common';
import user_login from './user_login';

const csrf_token = getCsrfToken();

window.$ = window.jQuery = require('jquery');

(($) => {
  $(() => {
    // CSRF protection

    function csrfSaveMethod(method) {
      return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
    }

    $.ajaxSetup({
      beforeSend: (xhr, settings) => {
        if (!csrfSaveMethod(settings.type) && !$(this).crossDomain) {
          xhr.setRequestHeader('X-CSRFToken', csrf_token);
        }
      },
    });
    // end CSRF protection

    user_login();
  });
})($);
