class CourierAPIException(Exception):
    response = None
    message = "An unknown error occurred"

    def __init__(self, response):
        self.response = response
        respJSON = response.json()
        msg = respJSON.get("Message") or respJSON.get("message")
        self.message = "Call to {uri} returned {status_code}\n{msg}".format(
            uri=response.url,
            status_code=response.status_code,
            msg=msg
        )
