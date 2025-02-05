import unittest
from unittest.mock import patch, MagicMock
from kaleidoscope_sdk import KaleidoscopeAPI

class TestKaleidoscopeAPI(unittest.TestCase):
    """Unit tests for the KaleidoscopeAPI SDK."""

    def setUp(self):
        """Set up a test instance of the API client."""
        self.api = KaleidoscopeAPI(api_key="test_api_key")

    @patch("requests.get")
    def test_search_sec_filings(self, mock_get):
        """Test SEC filings search endpoint."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"data": "mock_sec_filings_data"})
        response = self.api.search_sec_filings("AAPL", "sec")
        self.assertEqual(response, {"data": "mock_sec_filings_data"})

    @patch("requests.get")
    def test_get_holdings(self, mock_get):
        """Test holdings data retrieval."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"data": "mock_holdings_data"})
        response = self.api.get_holdings("AAPL", "PDF")
        self.assertEqual(response, {"data": "mock_holdings_data"})

    @patch("requests.get")
    def test_get_form_d(self, mock_get):
        """Test Form-D filings retrieval."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"data": "mock_form_d_data"})
        response = self.api.get_form_d("123456")
        self.assertEqual(response, {"data": "mock_form_d_data"})

    @patch("requests.get")
    def test_get_form_c(self, mock_get):
        """Test Form-C filings retrieval."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"data": "mock_form_c_data"})
        response = self.api.get_form_c("123456")
        self.assertEqual(response, {"data": "mock_form_c_data"})

    @patch("requests.get")
    def test_get_insider_transactions(self, mock_get):
        """Test insider transactions retrieval."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"data": "mock_insider_data"})
        response = self.api.get_insider_transactions("AAPL")
        self.assertEqual(response, {"data": "mock_insider_data"})

    @patch("requests.get")
    def test_get_stock_real_time(self, mock_get):
        """Test real-time stock data retrieval."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"ticker": "TSLA", "last_price": 236.86})
        response = self.api.get_stock_real_time()
        self.assertEqual(response["ticker"], "TSLA")

    @patch("requests.get")
    def test_get_stock_historical(self, mock_get):
        """Test historical stock data retrieval."""
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"data": "mock_stock_historical_data"})
        response = self.api.get_stock_historical(sd="2023-01-01", ed="2023-12-31")
        self.assertEqual(response, {"data": "mock_stock_historical_data"})

    @patch("requests.get")
    def test_handle_error_responses(self, mock_get):
        """Test API error handling."""
        for error_code, error_message in [(401, "Kaleidoscope API Error 401"), (404, "Kaleidoscope API Error 404"), (429, "Kaleidoscope API Error 429"), (500, "Kaleidoscope API Error 500")]:
            mock_get.return_value = MagicMock(status_code=error_code)
            with self.assertRaises(Exception) as context:
                self.api.get_stock_real_time()
            self.assertIn(error_message, str(context.exception))

if __name__ == "__main__":
    unittest.main()
