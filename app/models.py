from app.database import Base
from sqlalchemy import Column, Integer, String, Numeric


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
