from xai_components.base import InArg, OutArg, Component, xai_component
import requests

@xai_component
class GetRequestComponent(Component):
    """A component that performs a GET request and returns the response as a string.

    ##### inPorts:
    - url (str): The URL to send the GET request to.

    ##### outPorts:
    - response (str): The response from the GET request.
    """
    url: InArg[str]
    response: OutArg[str]

    def execute(self, ctx) -> None:
        try:
            # Perform the GET request
            resp = requests.get(self.url.value)
            # Set the response output
            self.response.value = resp.text
        except Exception as e:
            self.response.value = f"Error: {str(e)}"
