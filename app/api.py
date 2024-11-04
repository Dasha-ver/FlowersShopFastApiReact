from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from app import models
from app.database import engine, get_db
from app.models import (Balloon, Bouquet, BouquetOfRoses, ByThePiece, Card, Celebrate, FlowersBasket, FlowersBox,
                        Present, ToWhom, Toy, User, Role)
from sqlalchemy.sql.expression import func
from datetime import datetime, timedelta
from typing import Union, List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import schemas


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: models.User = Depends(get_current_active_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")


allow_admin = RoleChecker([models.Role.ADMIN.name])


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/register-admin", status_code=201, response_model=schemas.User)
def create_admin(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = db.query(models.User).filter(models.User.role == models.Role.ADMIN.name).first()
    if admin:
        raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="The administrator exists",
                )

    else:
        admin = models.User(
            username=form_data.username,
            hashed_password=models.User.get_password_hash(form_data.password),
            role=models.Role.ADMIN

        )
        db.add(admin)
        db.commit()
        return admin


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = models.User.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user


@app.get("/only-admin/", dependencies=[Depends(allow_admin)])
async def only_admin():
    return {"detail": "success"}

