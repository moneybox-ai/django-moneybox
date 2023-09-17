from drf_spectacular.extensions import OpenApiAuthenticationExtension


class AuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "api.authentication.APIAuthentication"
    name = "APIAuthentication"

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
