class CourierAPIException(Exception):
    response = None
    message = "An unknown error occurred"

    def __init__(self, response):
        self.response = response
        self.message = """Call to {uri} returned {status_code}
        {msg}""".format(
            uri=response.url,
            status_code=response.status_code,
            msg=response.json()
        )
