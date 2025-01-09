import logging
from flask import request, jsonify
from flask_cors import cross_origin

from swagger_server.models.seller import Seller  # noqa: E501
from swagger_server.models.seller_request import SellerRequest  # noqa: E501
from swagger_server.models.seller_update import SellerUpdate  # noqa: E501
from swagger_server import util

from swagger_server.repositories.seller_repository import SellerRepository

seller_repository = SellerRepository()

def sellers_get():  # noqa: E501
    """Obtener todos los vendedores o filtrar por programa

     # noqa: E501


    :rtype: List[Seller]
    """
    program_id = request.args.get('program_id', type=int)
    if  program_id:
        sellers = seller_repository.get_sellers(program_id)
    else:
        sellers = seller_repository.get_all_sellers()
    return jsonify(sellers)


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


def sellers_id_patch(body, id_):  # noqa: E501
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
        return seller_repository.update_seller(id_, body)


def sellers_post(body):  # noqa: E501
    """Crear un nuevo vendedor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Seller
    """
    if request.is_json:
        body = SellerRequest.from_dict(request.get_json())  # noqa: E501
        
        # Validaciones
        if not body.correo or not body.nombres or not body.apellidos:
            return jsonify({"message": "Email, first name, and last name are required."}), 400
        
        # Asegurar que el estado siempre sea 1
        body.estado = 1
        
        return seller_repository.create_seller(body)
