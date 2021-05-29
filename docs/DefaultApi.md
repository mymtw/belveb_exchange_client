# belveb_exchange_client.DefaultApi

All URIs are relative to *https://dbo.bveb.by/public/exchange/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rates_get**](DefaultApi.md#get_rates_get) | **GET** /getRates | Bel VEB exchange rates client


# **get_rates_get**
> Rates get_rates_get(exchange_type)

Bel VEB exchange rates client

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import belveb_exchange_client
from belveb_exchange_client.api import default_api
from belveb_exchange_client.model.rates import Rates
from pprint import pprint
# Defining the host is optional and defaults to https://dbo.bveb.by/public/exchange/1
# See configuration.py for a list of all supported configuration parameters.
configuration = belveb_exchange_client.Configuration(
    host = "https://dbo.bveb.by/public/exchange/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = belveb_exchange_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with belveb_exchange_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    exchange_type = "beznal" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Bel VEB exchange rates client
        api_response = api_instance.get_rates_get(exchange_type)
        pprint(api_response)
    except belveb_exchange_client.ApiException as e:
        print("Exception when calling DefaultApi->get_rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_type** | **str**|  |

### Return type

[**Rates**](Rates.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

