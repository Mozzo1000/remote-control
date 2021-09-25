import requests

class Connection:
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        }
        self._config = None

    def api_status(self):
        url = self.host + "api/"
        return requests.get(url, headers=self.headers).status_code

    def error_log(self):
        url = self.host + "api/error_log"
        return requests.get(url, headers=self.headers).text

    def get_config(self):
        url = self.host + "api/config"
        self._config = requests.get(url, headers=self.headers).json()
        return self._config

    def version(self):
        """Get version of Home Assistant

        Returns:
            str: Version of Home Assistant
        """
        if not self._config:
            self.get_config()
        return self._config["version"]

    def name(self):
        """Get location name of Home Assistant

        Returns:
            str: Name of Home Assistant
        """
        if not self._config:
            self.get_config()
        return self._config["location_name"]

    def components(self):
        """Get list of installed components in Home Assistant

        Returns:
            list: List of installed components in Home Assistant
        """
        if not self._config:
            self.get_config()
        return self._config["components"]
        
