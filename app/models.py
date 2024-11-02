from app.database import Base
from sqlalchemy import Column, Integer, String, Numeric, Enum, Boolean
import enum
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Role(str, enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(Role))

    class Config:
        orm_mode = True

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def authenticate_user(cls, db, username: str, password: str):
        user = db.query(cls).filter(cls.username == username).first()
        if not user:
            return False
        if not cls.verify_password(password, user.hashed_password):
            return False
        return user

    @classmethod
    def create_user(cls, db, username, password, role):
        user = cls(
            username=username,
            hashed_password=cls.get_password_hash(password),
            role=role
        )
        db.add(user)
        db.commit()

        return user


class Balloon(Base):
    __tablename__ = "balloons"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class Bouquet(Base):
    __tablename__ = "bouquets"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class BouquetOfRoses(Base):
    __tablename__ = "bouquets_of_roses"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class ByThePiece(Base):
    __tablename__ = "by_the_piece"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class Celebrate(Base):
    __tablename__ = "celebrate"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class FlowersBasket(Base):
    __tablename__ = "flowers_baskets"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class FlowersBox(Base):
    __tablename__ = "flowers_boxes"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class Present(Base):
    __tablename__ = "presents"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class ToWhom(Base):
    __tablename__ = "to_whom"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)


class Toy(Base):
    __tablename__ = "toys"

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
