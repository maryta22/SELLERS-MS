from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(10), nullable=False)
    
    sellers = relationship("Seller", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone
        }

class Seller(Base):
    __tablename__ = 'sales_advisor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    state = Column(Integer, nullable=False)

    user = relationship("User", back_populates="sellers")

    def to_dict(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "state": self.state,
            "user": self.user.to_dict() if self.user else None
        }