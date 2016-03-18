from boto.exception import BotoServerError


class CfnSphereException(Exception):
    def __init__(self, message="", boto_exception=None):
        self.message = message
        self.str = self.message
        try:
            self.request_id = boto_exception.request_id
            self.str += " (Request ID: {0})".format(self.request_id)
            self.boto_exception = boto_exception
        except:
            pass

    def __str__(self):
        return self.str


class CfnStackActionFailedException(CfnSphereException):
    pass

class TemplateErrorException(CfnSphereException):
    pass


class NoConfigException(CfnSphereException):
    pass


class BadConfigException(CfnSphereException):
    pass


class CyclicDependencyException(CfnSphereException):
    pass


class InvalidDependencyGraphException(CfnSphereException):
    pass


class InvalidEncryptedValueException(CfnSphereException):
    pass


class CfnSphereBotoErrorException(CfnSphereException):
    def __init__(self, e):
        self.boto_exception = e

    def __str__(self):
        return "{0}: {1} (Request ID: {2})".format(self.boto_exception.error_code,
                                                 self.boto_exception.message,
                                                 self.boto_exception.request_id)
