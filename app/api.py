from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from app import models
from app.database import engine, get_db
from app.models import (Balloon, Bouquet, BouquetOfRoses, ByThePiece, Card, Celebrate, FlowersBasket, FlowersBox,
                        Present, ToWhom, Toy)
from sqlalchemy.sql.expression import func

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api/balloons/{min}/{max}/{id}")
def get_balloons(min, max, id, db: Session = Depends(get_db)):
    balloons = (db.query(Balloon).filter(Balloon.price.__ge__(min), Balloon.price.__le__(max)).limit(id).all())
    if balloons is None:
        return JSONResponse(status_code=404, content={"message": "Шары не найдены"})
    return balloons


@app.get("/api/balloons/{id}")
def get_balloon(id, db: Session = Depends(get_db)):
    balloon = (db.query(Balloon).filter(Balloon.id.__eq__(id)).all())
    if balloon is None:
        return JSONResponse(status_code=404, content={"message": "Шар не найден"})
    return balloon


@app.get("/api/bouquets/{min}/{max}/{id}")
def get_bouquets(min, max, id, db: Session = Depends(get_db)):
    bouquets = (db.query(Bouquet).filter(Bouquet.price.__ge__(min), Bouquet.price.__le__(max)).limit(id).all())
    if bouquets is None:
        return JSONResponse(status_code=404, content={"message": "Букеты не найдены"})
    return bouquets


@app.get("/api/bouquets/{id}")
def get_bouquet(id, db: Session = Depends(get_db)):
    bouquet = (db.query(Bouquet).filter(Bouquet.id.__eq__(id)).all())
    if bouquet is None:
        return JSONResponse(status_code=404, content={"message": "Букет не найден"})
    return bouquet


@app.get("/api/bouquets_of_roses/{min}/{max}/{id}")
def get_bouquets_of_roses(min, max, id, db: Session = Depends(get_db)):
    bouquetsOfRoses = (
        db.query(BouquetOfRoses).filter(BouquetOfRoses.price.__ge__(min), BouquetOfRoses.price.__le__(max)).limit(
            id).all())
    if bouquetsOfRoses is None:
        return JSONResponse(status_code=404, content={"message": "Букеты роз не найдены"})
    return bouquetsOfRoses


@app.get("/api/bouquets_of_roses/{id}")
def get_bouquet_of_roses(id, db: Session = Depends(get_db)):
    bouquetOfRoses = (db.query(BouquetOfRoses).filter(BouquetOfRoses.id.__eq__(id)).all())
    if bouquetOfRoses is None:
        return JSONResponse(status_code=404, content={"message": "Букет роз не найден"})
    return bouquetOfRoses


@app.get("/api/by_the_piece/{min}/{max}/{id}")
def get_by_the_pieces(min, max, id, db: Session = Depends(get_db)):
    byThePieces = (
        db.query(ByThePiece).filter(ByThePiece.price.__ge__(min), ByThePiece.price.__le__(max)).limit(id).all())
    if byThePieces is None:
        return JSONResponse(status_code=404, content={"message": "Цветы не найдены"})
    return byThePieces


@app.get("/api/by_the_piece/{id}")
def get_by_the_piece(id, db: Session = Depends(get_db)):
    byThePiece = (db.query(ByThePiece).filter(ByThePiece.id.__eq__(id)).all())
    if byThePiece is None:
        return JSONResponse(status_code=404, content={"message": "Цветок не найден"})
    return byThePiece


@app.get("/api/cards/{min}/{max}/{id}")
def get_cards(min, max, id, db: Session = Depends(get_db)):
    cards = (db.query(Card).filter(Card.price.__ge__(min), Card.price.__le__(max)).limit(id).all())
    if cards is None:
        return JSONResponse(status_code=404, content={"message": "Открытки не найдены"})
    return cards


@app.get("/api/cards/{id}")
def get_card(id, db: Session = Depends(get_db)):
    card = (db.query(Card).filter(Card.id.__eq__(id)).all())
    if card is None:
        return JSONResponse(status_code=404, content={"message": "Отарытка не найдена"})
    return card


@app.get("/api/celebrate/{min}/{max}/{id}")
def get_cards(min, max, id, db: Session = Depends(get_db)):
    celebrates = (db.query(Celebrate).filter(Celebrate.price.__ge__(min), Celebrate.price.__le__(max)).limit(id).all())
    if celebrates is None:
        return JSONResponse(status_code=404, content={"message": "Цветы не найдены"})
    return celebrates


@app.get("/api/celebrate/{id}")
def get_celebrate(id, db: Session = Depends(get_db)):
    celebrate = (db.query(Celebrate).filter(Celebrate.id.__eq__(id)).all())
    if celebrate is None:
        return JSONResponse(status_code=404, content={"message": "Цветок не найден"})
    return celebrate


@app.get("/api/flowers_baskets/{min}/{max}/{id}")
def get_flowers_baskets(min, max, id, db: Session = Depends(get_db)):
    flowersBaskets = (
        db.query(FlowersBasket).filter(FlowersBasket.price.__ge__(min), FlowersBasket.price.__le__(max)).limit(
            id).all())
    if flowersBaskets is None:
        return JSONResponse(status_code=404, content={"message": "Корзины не найдены"})
    return flowersBaskets


@app.get("/api/flowers_baskets/{id}")
def get_flowers_basket(id, db: Session = Depends(get_db)):
    flowersBasket = (db.query(FlowersBasket).filter(FlowersBasket.id.__eq__(id)).all())
    if flowersBasket is None:
        return JSONResponse(status_code=404, content={"message": "Корзина не найдена"})
    return flowersBasket


@app.get("/api/flowers_boxes/{min}/{max}/{id}")
def get_flowers_boxes(min, max, id, db: Session = Depends(get_db)):
    flowers_boxes = (
        db.query(FlowersBox).filter(FlowersBox.price.__ge__(min), FlowersBox.price.__le__(max)).limit(id).all())
    if flowers_boxes is None:
        return JSONResponse(status_code=404, content={"message": "Коробки не найдены"})
    return flowers_boxes


@app.get("/api/flowers_boxes/{id}")
def get_flowers_box(id, db: Session = Depends(get_db)):
    flowersBox = (db.query(FlowersBox).filter(FlowersBox.id.__eq__(id)).all())
    if flowersBox is None:
        return JSONResponse(status_code=404, content={"message": "Коробка не найдена"})
    return flowersBox


@app.get("/api/presents/{min}/{max}/{id}")
def get_presents(min, max, id, db: Session = Depends(get_db)):
    presents = (db.query(Present).filter(Present.price.__ge__(min), Present.price.__le__(max)).limit(id).all())
    if presents is None:
        return JSONResponse(status_code=404, content={"message": "Подарки не найдены"})
    return presents


@app.get("/api/presents/{id}")
def get_present(id, db: Session = Depends(get_db)):
    present = (db.query(Present).filter(Present.id.__eq__(id)).all())
    if present is None:
        return JSONResponse(status_code=404, content={"message": "Подарок не найден"})
    return present


@app.get("/api/to_whom/{min}/{max}/{id}")
def get_to_whom(min, max, id, db: Session = Depends(get_db)):
    toWhom = (db.query(ToWhom).filter(ToWhom.price.__ge__(min), ToWhom.price.__le__(max)).limit(id).all())
    if toWhom is None:
        return JSONResponse(status_code=404, content={"message": "Не найдено"})
    return toWhom


@app.get("/api/to_whom/{id}")
def get_whom(id, db: Session = Depends(get_db)):
    whom = (db.query(ToWhom).filter(ToWhom.id.__eq__(id)).all())
    if whom is None:
        return JSONResponse(status_code=404, content={"message": "Не найдено"})
    return whom


@app.get("/api/toys/{min}/{max}/{id}")
def get_toys(min, max, id, db: Session = Depends(get_db)):
    toys = (db.query(Toy).filter(Toy.price.__ge__(min), Toy.price.__le__(max)).limit(id).all())
    if toys is None:
        return JSONResponse(status_code=404, content={"message": "Игрушки не найдены"})
    return toys


@app.get("/api/toys/{id}")
def get_toy(id, db: Session = Depends(get_db)):
    toy = (db.query(Toy).filter(Toy.id.__eq__(id)).all())
    if toy is None:
        return JSONResponse(status_code=404, content={"message": "Игрушка не найдена"})
    return toy


@app.get("/api/toys/min_price")
def get_toys_min_price(db: Session = Depends(get_db)):
    minPrice = (db.query(func.min(Toy.price)).first()[0])
    if minPrice is None:
        return JSONResponse(status_code=404, content={"message": "Игрушка не найдена"})
    return minPrice
