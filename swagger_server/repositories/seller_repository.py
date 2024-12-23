from swagger_server.database_models.models import Seller, User

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