# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.seller import Seller  # noqa: E501
from swagger_server.models.seller_request import SellerRequest  # noqa: E501
from swagger_server.models.seller_update import SellerUpdate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_sellers_get(self):
        """Test case for sellers_get

        Obtener todos los vendedores
        """
        response = self.client.open(
            '/sellers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sellers_id_delete(self):
        """Test case for sellers_id_delete

        Eliminar un vendedor
        """
        response = self.client.open(
            '/sellers/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sellers_id_get(self):
        """Test case for sellers_id_get

        Obtener un vendedor por ID
        """
        response = self.client.open(
            '/sellers/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sellers_id_patch(self):
        """Test case for sellers_id_patch

        Actualizar parcialmente un vendedor
        """
        body = SellerUpdate()
        response = self.client.open(
            '/sellers/{id}'.format(id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sellers_post(self):
        """Test case for sellers_post

        Crear un nuevo vendedor
        """
        body = SellerRequest()
        response = self.client.open(
            '/sellers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
