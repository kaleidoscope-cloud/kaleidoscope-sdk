from kaleidoscope_sdk import KaleidoscopeAPI

# Initialize the SDK with your API key
api = KaleidoscopeAPI(api_key="12539378-38b3-4b12-917f-b44185406b6a")

# Search SEC filings for Apple Inc. (AAPL) with content type 'sec'
try:
    sec_filings = api.search_sec_filings(identifier="AAPL", content="sec", limit=5)
    print(sec_filings)  # Print the retrieved filings
except Exception as e:
    print(f"Error fetching SEC filings: {e}")
