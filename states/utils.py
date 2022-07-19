from aiogram.dispatcher.filters.state import StatesGroup, State


class Mailing(StatesGroup):
    Text = State()


class Calculator(StatesGroup):
    SendWeight = State()
    SendHeight = State()
    SendAge = State()
    SendBoo = State()
    SendChoice = State()


class Back(StatesGroup):
    Q0 = State()
    Q1 = State()
    Q2 = State()
    P1 = State()
    P2 = State()


class Hard(StatesGroup):
    P1_W1 = State()
    P1_W2 = State()
    P1_W3 = State()
    P1_W4 = State()
    P2_W1 = State()
    P2_W2 = State()
    P2_W3 = State()
    P2_W4 = State()


