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


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/api/balloons")
def get_all_balloons(db: Session = Depends(get_db)):
    return db.query(Balloon).all()


@app.get("/api/balloon/{id}")
def get_balloon(id, db: Session = Depends(get_db)):
    balloon = (db.query(Balloon).filter(Balloon.id.__eq__(id)).all())
    if balloon is None:
        return JSONResponse(status_code=404, content={"message": "Шар не найден"})
    return balloon


@app.get("/api/bouquet/{id}")
def get_balloon(id, db: Session = Depends(get_db)):
    bouquet = (db.query(Bouquet).filter_by(id=id))
    if bouquet is None:
        return JSONResponse(status_code=404, content={"message": "Шар не найден"})
    return bouquet


@app.get("/api/balloons/{min}/{max}/{id}")
def get_balloons(min, max, id, db: Session = Depends(get_db)):
    balloons = (db.query(Balloon).filter(Balloon.price.__ge__(min), Balloon.price.__le__(max)).limit(id).all())
    if balloons is None:
        return JSONResponse(status_code=404, content={"message": "Шар не найден"})
    return balloons


@app.get("/api/bouquets/{min}/{max}/{id}")
def get_bouquets(min, max, id, db: Session = Depends(get_db)):
    bouquets = (db.query(Bouquet).filter(Bouquet.price.__ge__(min), Bouquet.price.__le__(max)).limit(id).all())
    if bouquets is None:
        return JSONResponse(status_code=404, content={"message": "Букет не найден"})
    return bouquets


@app.get("/api/bouquets_of_roses/{min}/{max}/{id}")
def get_bouquets_of_roses(min, max, id, db: Session = Depends(get_db)):
    bouquetsOfRoses = (
        db.query(BouquetOfRoses).filter(BouquetOfRoses.price.__ge__(min), BouquetOfRoses.price.__le__(max)).limit(
            id).all())
    if bouquetsOfRoses is None:
        return JSONResponse(status_code=404, content={"message": "Букет не найден"})
    return bouquetsOfRoses


@app.get("/api/by_the_piece/{min}/{max}/{id}")
def get_by_the_piece(min, max, id, db: Session = Depends(get_db)):
    byThePiece = (
        db.query(ByThePiece).filter(ByThePiece.price.__ge__(min), ByThePiece.price.__le__(max)).limit(id).all())
    if byThePiece is None:
        return JSONResponse(status_code=404, content={"message": "Цветок не найден"})
    return byThePiece


@app.get("/api/cards/{min}/{max}/{id}")
def get_cards(min, max, id, db: Session = Depends(get_db)):
    cards = (db.query(Card).filter(Card.price.__ge__(min), Card.price.__le__(max)).limit(id).all())
    if cards is None:
        return JSONResponse(status_code=404, content={"message": "Открытка не найдена"})
    return cards


@app.get("/api/celebrate/{min}/{max}/{id}")
def get_cards(min, max, id, db: Session = Depends(get_db)):
    celebrate = (db.query(Celebrate).filter(Celebrate.price.__ge__(min), Celebrate.price.__le__(max)).limit(id).all())
    if celebrate is None:
        return JSONResponse(status_code=404, content={"message": "Цветок не найден"})
    return celebrate


@app.get("/api/flowers_baskets/{min}/{max}/{id}")
def get_flowers_baskets(min, max, id, db: Session = Depends(get_db)):
    flowers_baskets = (
        db.query(FlowersBasket).filter(FlowersBasket.price.__ge__(min), FlowersBasket.price.__le__(max)).limit(
            id).all())
    if flowers_baskets is None:
        return JSONResponse(status_code=404, content={"message": "Корзина не найдена"})
    return flowers_baskets


@app.get("/api/flowers_boxes/{min}/{max}/{id}")
def get_flowers_boxes(min, max, id, db: Session = Depends(get_db)):
    flowers_boxes = (
        db.query(FlowersBox).filter(FlowersBox.price.__ge__(min), FlowersBox.price.__le__(max)).limit(id).all())
    if flowers_boxes is None:
        return JSONResponse(status_code=404, content={"message": "Коробка не найдена"})
    return flowers_boxes


@app.get("/api/presents/{min}/{max}/{id}")
def get_presents(min, max, id, db: Session = Depends(get_db)):
    presents = (db.query(Present).filter(Present.price.__ge__(min), Present.price.__le__(max)).limit(id).all())
    if presents is None:
        return JSONResponse(status_code=404, content={"message": "Подарок не найден"})
    return presents


@app.get("/api/to_whom/{min}/{max}/{id}")
def get_to_whom(min, max, id, db: Session = Depends(get_db)):
    to_whom = (db.query(ToWhom).filter(ToWhom.price.__ge__(min), ToWhom.price.__le__(max)).limit(id).all())
    if to_whom is None:
        return JSONResponse(status_code=404, content={"message": "Не найдено"})
    return to_whom


@app.get("/api/toys/{min}/{max}/{id}")
def get_toys(min, max, id, db: Session = Depends(get_db)):
    toys = (db.query(Toy).filter(Toy.price.__ge__(min), Toy.price.__le__(max)).limit(id).all())
    if toys is None:
        return JSONResponse(status_code=404, content={"message": "Игрушка не найдена"})
    return toys


@app.get("/api/toys/min_price")
def get_toys_min_price(db: Session = Depends(get_db)):
    minPrice = (db.query(func.min(Toy.price)).first()[0])
    if minPrice is None:
        return JSONResponse(status_code=404, content={"message": "Игрушка не найдена"})
    return minPrice
