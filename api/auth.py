# Authentication boundary. Production deployments should configure secure session handling,
# Google OAuth credentials, HTTPS, and ownership checks before enabling external login.
def authentication_configuration():
    return {"google_oauth_supported": True, "configured": False}
