class InvalidRefreshTokenException(Exception):
    pass


class RefreshTokenExpiredException(Exception):
    pass


class InvalidAccessTokenException(Exception):
    pass


class UserAlreadyExistsException(Exception):
    pass


class PasswordDoesnotMatch(Exception):
    pass


class PasswordDoesNotMatchException(Exception):
    pass


class UserNotFoundException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass
