
from hashlib import md5
from django.utils.deprecation import MiddlewareMixin


class SecretBallotMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.secretballot_token = self.generate_token(request)

    def generate_token(self, request):
        raise NotImplementedError


class SecretBallotIpMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        return request.META['REMOTE_ADDR']


class SecretBallotIpUseragentMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        s = u"".join((request.META['REMOTE_ADDR'], request.META.get('HTTP_USER_AGENT', '')))
        return md5(s.encode('utf-8')).hexdigest()


# from django.utils.deprecation import MiddlewareMixin
#
#
# class SecretBallotIpUseragentMiddleware(MiddlewareMixin):
