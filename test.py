import unittest
from unittest.mock import patch, MagicMock
from kaleidoscope_sdk import KaleidoscopeAPI

class TestKaleidoscopeAPI(unittest.TestCase):
    """Unit tests for the KaleidoscopeAPI SDK."""

    def setUp(self):
        """Set up a test instance of the API client."""
        self.api = KaleidoscopeAPI(api_key="test_api_key")
    
    @patch("requests.get")
    def test_search_sec_filings_success(self, mock_get):
        """Test successful SEC filings search."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "mock_sec_filings_data"}
        mock_get.return_value = mock_response
        
        response = self.api.search_sec_filings("AAPL", "sec")
        self.assertEqual(response, {"data": "mock_sec_filings_data"})
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_get_stock_real_time_success(self, mock_get):
        """Test successful retrieval of real-time stock data."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ticker": "TSLA", "last_price": 236.86}
        mock_get.return_value = mock_response
        
        response = self.api.get_stock_real_time()
        self.assertEqual(response["ticker"], "TSLA")
        self.assertEqual(response["last_price"], 236.86)
        mock_get.assert_called_once()
    
    @patch("requests.get")
    def test_handle_unauthorized_error(self, mock_get):
        """Test handling of unauthorized API key error."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        with self.assertRaises(Exception) as context:
            self.api.get_stock_real_time()
        self.assertIn("Kaleidoscope API Error 401", str(context.exception))
    
    @patch("requests.get")
    def test_handle_not_found_error(self, mock_get):
        """Test handling of 404 Not Found error."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with self.assertRaises(Exception) as context:
            self.api.get_stock_real_time()
        self.assertIn("Kaleidoscope API Error 404", str(context.exception))
    
    @patch("requests.get")
    def test_handle_rate_limit_error(self, mock_get):
        """Test handling of 429 Too Many Requests error."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_get.return_value = mock_response
        
        with self.assertRaises(Exception) as context:
            self.api.get_stock_real_time()
        self.assertIn("Kaleidoscope API Error 429", str(context.exception))
    
    @patch("requests.get")
    def test_handle_server_error(self, mock_get):
        """Test handling of server error responses."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        with self.assertRaises(Exception) as context:
            self.api.get_stock_real_time()
        self.assertIn("Kaleidoscope API Error 500", str(context.exception))

if __name__ == "__main__":
    unittest.main()
