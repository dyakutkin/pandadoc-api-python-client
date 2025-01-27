"""
    PandaDoc Public API

    PandaDoc Public API documentation  # noqa: E501

    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pandadoc_client.api_client import ApiClient, Endpoint as _Endpoint
from pandadoc_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pandadoc_client.model.form_list_response import FormListResponse


class FormsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_form_endpoint = _Endpoint(
            settings={
                'response_type': (FormListResponse,),
                'auth': [
                    'apiKey',
                    'oauth2'
                ],
                'endpoint_path': '/public/v1/forms',
                'operation_id': 'list_form',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'count',
                    'page',
                    'status',
                    'order_by',
                    'asc',
                    'name',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'status',
                    'order_by',
                ],
                'validation': [
                    'count',
                    'page',
                ]
            },
            root_map={
                'validations': {
                    ('count',): {

                        'inclusive_minimum': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('status',): {

                        "DRAFT": "draft",
                        "ACTIVE": "active",
                        "DISABLED": "disabled"
                    },
                    ('order_by',): {

                        "NAME": "name",
                        "RESPONSES": "responses",
                        "STATUS": "status",
                        "CREATED_DATE": "created_date",
                        "MODIFIED_DATE": "modified_date"
                    },
                },
                'openapi_types': {
                    'count':
                        (int,),
                    'page':
                        (int,),
                    'status':
                        ([str],),
                    'order_by':
                        (str,),
                    'asc':
                        (bool,),
                    'name':
                        (str,),
                },
                'attribute_map': {
                    'count': 'count',
                    'page': 'page',
                    'status': 'status',
                    'order_by': 'order_by',
                    'asc': 'asc',
                    'name': 'name',
                },
                'location_map': {
                    'count': 'query',
                    'page': 'query',
                    'status': 'query',
                    'order_by': 'query',
                    'asc': 'query',
                    'name': 'query',
                },
                'collection_format_map': {
                    'status': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def list_form(
        self,
        **kwargs
    ):
        """Forms  # noqa: E501

        List forms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_form(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            count (int): Optionally, specify how many forms to return. Default is 50 forms, maximum is 100 forms.. [optional]
            page (int): Optionally, specify which page of the dataset to return.. [optional]
            status ([str]): Optionally, specify which status of the forms dataset to return.. [optional]
            order_by (str): Optionally, specify the form dataset order to return.. [optional]
            asc (bool): Optionally, specify sorting the result-set in ascending or descending order.. [optional]
            name (str): Specify the form name.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            FormListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_form_endpoint.call_with_http_info(**kwargs)

