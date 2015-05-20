"""Base request engine."""

__author__ = 'vovanec@gmail.com'

import logging


class BaseRequestEngine(object):

    """Base class for HTTP request engine."""

    def __init__(self, api_base_url, connect_timeout, request_timeout,
                 conn_retries, username=None, password=None,
                 client_cert=None, client_key=None, verify_cert=True,
                 ca_certs=None):
        """Constructor.

        :param str api_base_url: API base URL.
        :param int connect_timeout: connection timeout.
        :param int request_timeout: request timeout.
        :param int|None conn_retries: The number of retries on connection
               error. If None - no retries.
        :param str|None username: auth username.
        :param str|None password: auth password.
        :param str|None client_cert: client certificate.
        :param str|None client_key: client key.
        :param bool verify_cert: whether to verify server cert.
        :param str|None ca_certs: path to CA certificate chain.
        """

        self._connect_timeout = connect_timeout
        self._request_timeout = request_timeout
        self._api_base_url = api_base_url.rstrip('/')
        self._username = username
        self._password = password
        self._conn_retries = conn_retries
        self._client_cert = client_cert
        self._client_key = client_key
        self._ca_certs = ca_certs
        self._verify_cert = verify_cert

        self._log = logging.getLogger(self.__class__.__name__)

    def request(self, url, *, method='GET', data=None, **kwargs):
        """Perform request.

        :param str url: request URL.
        :param str method: request method.
        :param object data: JSON-encodable object.

        :rtype: dict
        :raise: APIError

        """

        url = self._api_base_url + url
        self._log.debug('Performing %s request to URL %s', method, url)
        return self._request(url, method=method, data=data, **kwargs)

    def _request(self, url, *, method='GET', data=None, **kwargs):
        """Perform request. Subclasses must implement this.

        :param str url: request URL.
        :param str method: request method.
        :param object data: JSON-encodable object.

        :rtype: dict
        :raise: APIError

        """

        raise NotImplementedError