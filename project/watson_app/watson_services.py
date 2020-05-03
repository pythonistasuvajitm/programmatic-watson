from django.conf import settings
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import DiscoveryV1


class WatsonService(object):

    def __init__(self):
        self.apikey = settings.WATSON_API_KEY
        authenticator = IAMAuthenticator(settings.WATSON_API_KEY)
        self.discovery = DiscoveryV1(
            version='2019-04-30',
            authenticator=authenticator
        )
        self.discovery.set_service_url(settings.WATSON_SERVICE_BASE_URL)

    def add_document(self, file=None):
        add_doc = self.discovery.add_document(
            settings.WATSON_ENVIRONMENT_ID,
            settings.WATSON_COLLECTION_ID,
            file=file).get_result()
        return add_doc
