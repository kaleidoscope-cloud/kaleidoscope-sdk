import requests

class KaleidoscopeAPI:
    """
    Kaleidoscope API SDK
    This SDK allows developers to interact with the Kaleidoscope API to retrieve SEC filings,
    holdings data, insider transactions, stock information, compensation details, and more.
    """
    BASE_URL = "https://api.kscope.io/v2"

    def __init__(self, api_key: str):
        """
        Initialize the SDK with an API key.
        :param api_key: API key required for authentication.
        """
        self.api_key = api_key
        self.headers = {"Content-Type": "application/json"}
    
    def _get(self, endpoint: str, params: dict):
        """
        Internal method to handle GET requests.
        :param endpoint: API endpoint to access.
        :param params: Dictionary of query parameters.
        :return: Parsed JSON response from the API.
        """
        params["key"] = self.api_key
        try:
            response = requests.get(f"{self.BASE_URL}{endpoint}", headers=self.headers, params=params)
            return self._handle_response(response)
        except requests.exceptions.Timeout:
            raise Exception("Kaleidoscope API request timed out. Please try again later.")
        except requests.exceptions.ConnectionError:
            raise Exception("Kaleidoscope API connection error. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An unexpected error occurred while communicating with Kaleidoscope API: {str(e)}")
    
    def _handle_response(self, response):
        """
        Handle API responses and errors specific to the Kaleidoscope API.
        :param response: Response object from the API call.
        :return: JSON data if the response is successful.
        """
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            raise Exception("Kaleidoscope API Error 400: Bad Request - The request was invalid or malformed.")
        elif response.status_code == 401:
            raise Exception("Kaleidoscope API Error 401: Unauthorized - API key is invalid or missing.")
        elif response.status_code == 403:
            raise Exception("Kaleidoscope API Error 403: Forbidden - Access to this resource is denied.")
        elif response.status_code == 404:
            raise Exception("Kaleidoscope API Error 404: Not Found - The requested resource was not found.")
        elif response.status_code == 429:
            raise Exception("Kaleidoscope API Error 429: Too Many Requests - Rate limit exceeded. Slow down requests.")
        elif response.status_code >= 500:
            raise Exception("Kaleidoscope API Error 500: Server Error - The Kaleidoscope API encountered an issue.")
        else:
            response.raise_for_status()

    # SEC Filings Search
    def search_sec_filings(self, identifier: str, content: str, **kwargs):
        """Search SEC filings by ticker or CIK."""
        return self._get(f"/sec/search/{identifier}", {"content": content, **kwargs})

    # Holdings Data
    def get_holdings(self, identifier: str, data_type: str, **kwargs):
        """Retrieve holdings data."""
        return self._get(f"/sec/holdings/{identifier}", {"type": data_type, **kwargs})

    # Form-D Filings
    def get_form_d(self, identifier: str, **kwargs):
        """Retrieve Form-D filings."""
        return self._get(f"/sec/form-d/{identifier}", kwargs)

    # Form-C Filings
    def get_form_c(self, identifier: str, **kwargs):
        """Retrieve Form-C filings."""
        return self._get(f"/sec/form-c/{identifier}", kwargs)

    # Insider Transactions
    def get_insider_transactions(self, identifier: str, **kwargs):
        """Retrieve insider transactions."""
        return self._get(f"/insider/{identifier}", kwargs)

    # Stock Real-Time Data
    def get_stock_real_time(self):
        """Retrieve real-time stock data."""
        return self._get("/stock/real-time", {})

    # Stock Historical Data
    def get_stock_historical(self, **kwargs):
        """Retrieve historical stock data."""
        return self._get("/stock/stock-historical", kwargs)

    # Compensation Data
    def get_compensation_summary(self, identifier: str, **kwargs):
        """Retrieve executive compensation summary."""
        return self._get(f"/compensation/summary/{identifier}", kwargs)

    def get_compensation_director(self, identifier: str, **kwargs):
        """Retrieve director compensation details."""
        return self._get(f"/compensation/director/{identifier}", kwargs)

    # Corporate Actions
    def get_corporate_actions(self, identifier: str, **kwargs):
        """Retrieve corporate actions from Form 8-K filings."""
        return self._get(f"/corporate-actions/{identifier}", kwargs)

    # SEDAR Filings
    def get_sedar_filings(self, identifier: str, **kwargs):
        """Retrieve SEDAR filings."""
        return self._get(f"/sedar/{identifier}", kwargs)

    # Press Releases
    def get_press_releases(self, identifier: str, **kwargs):
        """Retrieve press releases for a given ticker."""
        return self._get(f"/news/press-releases/{identifier}", kwargs)
