from swagger_server.database_models.models import Seller, User, ProgramSellers, AcademicProgram

import logging
from datetime import datetime

from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

class SellerRepository:
    def __init__(self):
        pass_sam = os.getenv('DB_PASSWORD')
        self.engine = create_engine(f'mysql+pymysql://root:{pass_sam}@localhost:3306/espae_prospections')
        self.Session = sessionmaker(bind=self.engine)

    def get_all_sellers(self):
        session = self.Session()
        try:
            sellers = session.query(Seller).join(User).all()
            return [seller.to_dict() for seller in sellers], 200
        except Exception as e:
            logging.error(f"Error retrieving sellers: {e}")
            return {"message": f"Error retrieving sellers: {str(e)}"}, 500
        finally:
            session.close()

    def get_sellers(self, program_id):
        session = self.Session()
        try:
            sellers = session.query(Seller).join(ProgramSellers).filter(ProgramSellers.id_academic_program == program_id).all()
            return [seller.to_dict() for seller in sellers], 200
        except Exception as e:
            logging.error(f"Error retrieving sellers: {e}")
            return {"message": f"Error retrieving sellers: {str(e)}"}, 500
        finally:
            session.close()

    def create_seller(self, seller_request):
        session = self.Session()
        try:
            # Crear el usuario asociado
            new_user = User(
                first_name=seller_request.nombres,
                last_name=seller_request.apellidos,
                email=seller_request.correo,
                phone=seller_request.celular
            )
            session.add(new_user)
            session.flush()  # Para obtener el ID del usuario

            # Crear el vendedor asociado al usuario
            new_seller = Seller(
                id_user=new_user.id,
                state=seller_request.estado
            )
            session.add(new_seller)
            session.commit()

            return new_seller.to_dict(), 201
        except Exception as e:
            session.rollback()
            logging.error(f"Error creating seller: {e}")
            return {"message": f"Error creating seller: {str(e)}"}, 500
        finally:
            session.close()
    
    def update_seller(self, seller_id, seller_update):
        session = self.Session()
        try:
            seller = session.query(Seller).filter(Seller.id == seller_id).one_or_none()
            if not seller:
                return {"message": "Seller not found."}, 404

            user = seller.user
            if seller_update.nombres:
                user.first_name = seller_update.nombres
            if seller_update.apellidos:
                user.last_name = seller_update.apellidos
            if seller_update.correo:
                user.email = seller_update.correo
            if seller_update.celular:
                user.phone = seller_update.celular
            if seller_update.estado is not None:
                seller.state = seller_update.estado

            session.commit()
            return seller.to_dict(), 200
        except Exception as e:
            session.rollback()
            logging.error(f"Error updating seller: {e}")
            return {"message": f"Error updating seller: {str(e)}"}, 500
        finally:
            session.close()

    def get_seller_by_id(self, seller_id):
        session = self.Session()
        try:
            seller = session.query(Seller).options(joinedload(Seller.user)).filter(Seller.id == seller_id).one_or_none()
            if not seller:
                return None
            return seller
        except Exception as e:
            logging.error(f"Error retrieving seller by ID {seller_id}: {e}")
            return None
        finally:
            session.close()