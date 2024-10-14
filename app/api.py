from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from app import models
from app.database import engine, get_db
from app.models import (Balloon, Bouquet, BouquetOfRoses, ByThePiece, Card, Celebrate, FlowersBasket, FlowersBox,
                        Present, ToWhom, Toy)

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3001",
    "localhost:3001"
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
def get_balloons(db: Session = Depends(get_db)):
    return db.query(Balloon).all()


@app.get("/api/balloon/{id}")
def get_balloons(id, db: Session = Depends(get_db)):
    balloon = (db.query(Balloon).filter_by(id=id).first())
    if balloon is None:
        return JSONResponse(status_code=404, content={"message": "Шар не найден"})
    return balloon


@app.get("/api/balloons/{id}")
def get_balloons(id, db: Session = Depends(get_db)):
    balloons = (db.query(Balloon).order_by(Balloon.id.asc()).limit(id).all())
    if balloons is None:
        return JSONResponse(status_code=404, content={"message": "Шар не найден"})
    return balloons


@app.get("/api/bouquets/{id}")
def get_bouquets(id, db: Session = Depends(get_db)):
    bouquets = (db.query(Bouquet).order_by(Bouquet.id.asc()).limit(id).all())
    if bouquets is None:
        return JSONResponse(status_code=404, content={"message": "Букет не найден"})
    return bouquets


@app.get("/api/bouquets_of_roses/{id}")
def get_bouquets_of_roses(id, db: Session = Depends(get_db)):
    bouquetsOfRoses = (db.query(BouquetOfRoses).order_by(BouquetOfRoses.id.asc()).limit(id).all())
    if bouquetsOfRoses is None:
        return JSONResponse(status_code=404, content={"message": "Букет не найден"})
    return bouquetsOfRoses


@app.get("/api/by_the_piece/{id}")
def get_by_the_piece(id, db: Session = Depends(get_db)):
    byThePiece = (db.query(ByThePiece).order_by(ByThePiece.id.asc()).limit(id).all())
    if byThePiece is None:
        return JSONResponse(status_code=404, content={"message": "Цветок не найден"})
    return byThePiece


@app.get("/api/cards/{id}")
def get_cards(id, db: Session = Depends(get_db)):
    cards = (db.query(Card).order_by(Card.id.asc()).limit(id).all())
    if cards is None:
        return JSONResponse(status_code=404, content={"message": "Открытка не найдена"})
    return cards


@app.get("/api/celebrate/{id}")
def get_cards(id, db: Session = Depends(get_db)):
    celebrate = (db.query(Celebrate).order_by(Celebrate.id.asc()).limit(id).all())
    if celebrate is None:
        return JSONResponse(status_code=404, content={"message": "Цветок не найден"})
    return celebrate


@app.get("/api/flowers_baskets/{id}")
def get_flowers_baskets(id, db: Session = Depends(get_db)):
    flowers_baskets = (db.query(FlowersBasket).order_by(FlowersBasket.id.asc()).limit(id).all())
    if flowers_baskets is None:
        return JSONResponse(status_code=404, content={"message": "Корзина не найдена"})
    return flowers_baskets


@app.get("/api/flowers_boxes/{id}")
def get_flowers_boxes(id, db: Session = Depends(get_db)):
    flowers_boxes = (db.query(FlowersBox).order_by(FlowersBox.id.asc()).limit(id).all())
    if flowers_boxes is None:
        return JSONResponse(status_code=404, content={"message": "Коробка не найдена"})
    return flowers_boxes


@app.get("/api/presents/{id}")
def get_presents(id, db: Session = Depends(get_db)):
    presents = (db.query(Present).order_by(Present.id.asc()).limit(id).all())
    if presents is None:
        return JSONResponse(status_code=404, content={"message": "Подарок не найден"})
    return presents


@app.get("/api/to_whom/{id}")
def get_to_whom(id, db: Session = Depends(get_db)):
    to_whom = (db.query(ToWhom).order_by(ToWhom.id.asc()).limit(id).all())
    if to_whom is None:
        return JSONResponse(status_code=404, content={"message": "Не найдено"})
    return to_whom


@app.get("/api/toys/{id}")
def get_toys(id, db: Session = Depends(get_db)):
    toys = (db.query(Toy).order_by(Toy.id.asc()).limit(id).all())
    if toys is None:
        return JSONResponse(status_code=404, content={"message": "Игрушка не найдена"})
    return toys


