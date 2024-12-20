import connexion
import six
from flask import request

from swagger_server.models.seller import Seller  # noqa: E501
from swagger_server.models.seller_request import SellerRequest  # noqa: E501
from swagger_server.models.seller_update import SellerUpdate  # noqa: E501
from swagger_server import util


def sellers_get():  # noqa: E501
    """Obtener todos los vendedores

     # noqa: E501


    :rtype: List[Seller]
    """
    return 'do some magic!'


def sellers_id_delete(id):  # noqa: E501
    """Eliminar un vendedor

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def sellers_id_get(id):  # noqa: E501
    """Obtener un vendedor por ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Seller
    """
    return 'do some magic!'


def sellers_id_patch(body, id):  # noqa: E501
    """Actualizar parcialmente un vendedor

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: Seller
    """
    if request.is_json:
        body = SellerUpdate.from_dict(request.get_json())  # noqa: E501
    return 'do some magic!'


def sellers_post(body):  # noqa: E501
    """Crear un nuevo vendedor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Seller
    """
    if request.is_json:
        body = SellerRequest.from_dict(request.get_json())  # noqa: E501
    return 'do some magic!'
