# ---Django_social---

# Facebook settings
SOCIAL_FACEBOOK_ID = "328787081719892"
SOCIAL_FACEBOOK_TOKEN = "9f907bbab9aa1fd3e260cef41df00c68"
SOCIAL_FACEBOOK_API_URL = 'https://graph.facebook.com/me/?'
SOCIAL_FACEBOOK_AUTH_URL = 'https://www.facebook.com/v8.0/dialog/oauth?'
SOCIAL_FACEBOOK_TOKEN_URL = 'https://graph.facebook.com/v8.0/oauth/access_token?'
SOCIAL_FACEBOOK_REDIRECT_URL = "http://localhost:8000/social/fb"

SOCIAL_FACEBOOK_DEBUG_TOKEN_URL = 'https://graph.facebook.com/debug_token?'  # TODO пока не используется
SOCIAL_FACEBOOK_ACCESS_TOKEN = "328787081719892|JQlxsenjuByFjPLgS03ZDfwDaVI"  # TODO пока не используется

# Github settings
SOCIAL_GITHUB_ID = '7642118bb47047141802'
SOCIAL_GITHUB_SECRET = 'd96fffe82d8f2fcb006409c73d2ea8a086092674'
SOCIAL_GITHUB_REDIRECT_URL = 'http://localhost:8000/social/github'
SOCIAL_GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize?'
SOCIAL_GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token?"
SOCIAL_GITHUB_GET_USER_DATA = "https://api.github.com/user?"
SOCIAL_GITHUB_GET_USER_EMAIL = "https://api.github.com/user/emails?"

