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
    program_sellers = relationship("ProgramSellers", back_populates="sellers")

    def to_dict(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "state": self.state,
            "user": self.user.to_dict() if self.user else None
        }

# Table: AcademicProgram
class AcademicProgram(Base):
    __tablename__ = 'academic_program'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    state = Column(Integer, nullable=False)

    program_sellers = relationship("ProgramSellers", back_populates="academic_program")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "state": self.state,
            "sellers": [ps.sales_advisor.to_dict() for ps in self.program_sellers]
        }
    
# Table: ProgramSellers
class ProgramSellers(Base):
    __tablename__ = 'academic_program_sales_advisor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_academic_program = Column(Integer, ForeignKey('academic_program.id'), nullable=False)
    id_sales_advisor = Column(Integer, ForeignKey('sales_advisor.id'), nullable=False)
    state = Column(Integer, nullable=False)

    academic_program = relationship("AcademicProgram", back_populates="program_sellers")
    sellers = relationship("Seller", back_populates="program_sellers")

    def to_dict(self):
        return {
            "id": self.id,
            "id_academic_program": self.id_academic_program,
            "id_sales_advisor": self.id_sales_advisor,
            "state": self.state
        }
