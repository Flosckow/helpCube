# ---Django_social---

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',  # TODO добавить GitLab
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend',
)

# TODO  SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # TODO не очень надёжная штука судя по докам
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# Facebook settings
SOCIAL_FACEBOOK_ID = "328787081719892"
SOCIAL_FACEBOOK_TOKEN = "9f907bbab9aa1fd3e260cef41df00c68"
SOCIAL_FACEBOOK_API_URL = 'https://graph.facebook.com/me/?'
SOCIAL_FACEBOOK_AUTH_URL = 'https://www.facebook.com/v8.0/dialog/oauth?'
SOCIAL_FACEBOOK_TOKEN_URL = 'https://graph.facebook.com/v8.0/oauth/access_token?'
SOCIAL_FACEBOOK_REDIRECT_URL = "http://localhost:8000/social/fb"

SOCIAL_FACEBOOK_DEBUG_TOKEN_URL = 'https://graph.facebook.com/debug_token?'  # TODO пока не используется
SOCIAL_FACEBOOK_ACCESS_TOKEN = "328787081719892|JQlxsenjuByFjPLgS03ZDfwDaVI"  # TODO пока не используется
