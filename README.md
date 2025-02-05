# Kaleidoscope SDK

![Kaleidoscope SDK](https://your-image-url.com/logo.png)

Welcome to the **Kaleidoscope SDK**! This Python package provides a simple and intuitive way to interact with the **Kaleidoscope API**, allowing you to access SEC filings, insider transactions, stock data, corporate actions, and more.

## Features
- 📄 Retrieve **SEC filings** (10-K, 8-K, Form-D, Form-C, etc.)
- 📊 Get **real-time and historical stock data**
- 💼 Access **executive and director compensation data**
- 🔎 Fetch **insider transactions**
- 🏢 Retrieve **corporate actions** (mergers, acquisitions, IPOs, etc.)
- 🇨🇦 Query **SEDAR filings** for Canadian companies
- 📰 Access **press releases** by ticker symbol

## Installation

Install the SDK via pip:

```sh
pip install kaleidoscope-sdk
```

Or install from source:

```sh
git clone https://github.com/kaleidoscope-cloud/kaleidoscope-sdk.git
cd kaleidoscope-sdk
pip install .
```

## Getting Started

To start using the Kaleidoscope API, sign up for an API key at Kaleidoscope API Landing Page.

### Import and Initialize the SDK

```python
from kaleidoscope_sdk import KaleidoscopeAPI

# Initialize with your API key
api = KaleidoscopeAPI(api_key="your_api_key_here")
```

### Retrieve SEC Filings

```python
# Get SEC filings for Apple Inc. (AAPL)
sec_filings = api.search_sec_filings(identifier="AAPL", content="sec", limit=5)
print(sec_filings)
```

### Fetch Real-Time Stock Data

```python
# Get real-time stock data
real_time_stock = api.get_stock_real_time()
print(real_time_stock)
```

### Retrieve Insider Transactions

```python
# Get insider transactions for Apple Inc.
insider_trades = api.get_insider_transactions(identifier="AAPL", limit=3)
print(insider_trades)
```

### Retrieve Corporate Actions

```python
# Get corporate actions for Tesla (TSLA)
corporate_actions = api.get_corporate_actions(identifier="TSLA", limit=2)
print(corporate_actions)
```

## Error Handling
The SDK handles common API errors and provides informative error messages:

```python
try:
    data = api.get_stock_real_time()
    print(data)
except Exception as e:
    print(f"Error: {e}")
```

## API Reference
### **SEC Filings**
```python
api.search_sec_filings(identifier="AAPL", content="sec", limit=5)
```
- **identifier**: Ticker (e.g., `AAPL`) or CIK.
- **content**: Filter filings (`sec`, `exhibits`, `agreements`).
- **limit**: Number of results to return.

### **Stock Data**
```python
api.get_stock_real_time()
api.get_stock_historical(sd="2023-01-01", ed="2023-12-31", limit=10)
```

### **Insider Transactions**
```python
api.get_insider_transactions(identifier="AAPL", limit=3)
```

### **Compensation Data**
```python
api.get_compensation_summary(identifier="1214156", year=2022)
api.get_compensation_director(identifier="1214156", year=2022)
```

### **Corporate Actions**
```python
api.get_corporate_actions(identifier="TSLA", limit=2)
```

### **SEDAR Filings (Canada)**
```python
api.get_sedar_filings(identifier="00029882", limit=1)
```

## Running Tests
Run unit tests to verify functionality:
```sh
python -m unittest discover tests
```

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit your changes.
4. Push to your branch and create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For support or questions, open an issue or contact us at [support@kscope.io](mailto:support@kscope.io).

## 🌟 Star This Repo!
If you find this SDK useful, consider starring ⭐ the repository to help others find it!
Disclaimer

## Disclaimer
The data provided by this API is strictly for internal use only and is not intended for external distribution, publication, or unauthorized use. It also cannot be used for AI training, machine learning models, or any related purposes. However, this restriction does not apply to the Enterprise Package, which may be used externally as permitted by its terms. Unauthorized access, sharing, or disclosure of restricted data is strictly prohibited.

