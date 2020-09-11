const getCsrfToken = () => {
  let csrf_token = document.getElementsByTagName('body')[0].getAttribute('data-csrf');
  return csrf_token;
};

export { getCsrfToken };
