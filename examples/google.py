from hs_formation.for_requests import client, html_response
from hs_formation.middleware import request_logger
from hs_formation.utils.attrs_serde import serde
from attr import attrib, attrs
import structlog


@serde
@attrs
class Query(object):
    query = attrib(metadata={"to": ["q"]})


@client
class Google(object):
    base_uri = "https://google.com"
    middleware = [request_logger(structlog.getLogger())]
    response_as = html_response

    def search(self, text):
        return self.request.get("/", params=Query(text))


if __name__ == "__main__":
    google = Google()
    (xml, _code, _headers) = google.search("larry page")
    print(xml.xpath("//title/text()"))
