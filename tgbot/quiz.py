import asyncio
import logging
import sys
from os import getenv
from dataclasses import dataclass, field

from aiogram import Bot, Dispatcher, Router, F, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.fsm.scene import Scene, SceneRegistry, ScenesManager, on
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import KeyboardBuilder

TOKEN=""
print(TOKEN)

@dataclass
class Answer: 
    text: str
    is_correct: bool = False

@dataclass
class Question: 
    text: str
    answers: list[Answer]

    correct_answer: str = field(init=False)
    
    def __post_init__(self):
        self.correct_answer = next(answer.text for answer in self.answers if answer.is_correct)

QUESTIONS = [
    Question(
        text="What is the largest planet in our solar system?",
        answers=[
            Answer("Mars"),
            Answer("Venus"),
            Answer("Jupiter", is_correct=True),
            Answer("Saturn"),
        ]
    ),
    Question(
        text="Who is the author of 'Romeo and Juliet'?",
        answers=[
            Answer("Charles Dickens"),
            Answer("William Shakespeare", is_correct=True),
            Answer("Jane Austen"),
            Answer("Mark Twain"),
        ]
    ),
    Question(
        text="In which year did World War II end?",
        answers=[
            Answer("1943"),
            Answer("1945", is_correct=True),
            Answer("1947"),
            Answer("1950"),
        ]
    ),
    Question(
        text="What is the capital of Australia?",
        answers=[
            Answer("Sydney"),
            Answer("Melbourne"),
            Answer("Canberra", is_correct=True),
            Answer("Perth"),
        ]
    ),
    Question(
        text="Which element has the chemical symbol 'H'?",
        answers=[
            Answer("Helium"),
            Answer("Hydrogen", is_correct=True),
            Answer("Hassium"),
            Answer("Hafnium"),
        ]
    ),
    Question(
        text="Who painted the Mona Lisa?",
        answers=[
            Answer("Vincent van Gogh"),
            Answer("Pablo Picasso"),
            Answer("Leonardo da Vinci", is_correct=True),
            Answer("Claude Monet"),
        ]
    ),
    Question(
        text="What is the capital of Brazil?",
        answers=[
            Answer("Sao Paulo"),
            Answer("Rio de Janeiro"),
            Answer("Brasilia", is_correct=True),
            Answer("Salvador"),
        ]
    ),
    Question(
        text="Which planet is known as the 'Red Planet'?",
        answers=[
            Answer("Mars", is_correct=True),
            Answer("Venus"),
            Answer("Jupiter"),
            Answer("Saturn"),
        ]
    ),
    Question(
        text="Who is the famous scientist who formulated the theory of relativity?",
        answers=[
            Answer("Isaac Newton"),
            Answer("Galileo Galilei"),
            Answer("Albert Einstein", is_correct=True),
            Answer("Stephen Hawking"),
        ]
    ),
    Question(
        text="In what year did the United States declare its independence?",
        answers=[
            Answer("1765"),
            Answer("1776", is_correct=True),
            Answer("1789"),
            Answer("1800"),
        ]
    ),
]

class QuizScene(Scene, state="quiz"):
    
    @on.message.enter()
    async def on_enter(self, message: Message, state: FSMContext, step: int | None = 0):
        if not step:
            await message.answer("Welcome to quiz!")

        try: 
            quiz = QUESTIONS[step]
        except IndexError:
            return await self.wizard.exit()
        
        markup = KeyboardBuilder()
        markup.add(*[KeyboardButton(text=answer.text) for answer in quiz.answers])

        if step > 0:
            markup.add(text="Back")
        markup.add(text="Exit")

        await state.update_data(step=step)
        return await message.answer(
            text=QUESTIONS[step].text, 
            reply_markup=markup.adjust(2).as_markup(resize_keyboard=True),
        )

quiz_router = Router(name=__name__)
quiz_router.message.register(QuizScene.as_handler(), Command("quiz"))

@quiz_router.message(Command("start"))
async def command_start(message: Message, scenes: ScenesManager):
    await scenes.close()
    await message.answer("Hi!", reply_markup=ReplyKeyboardRemove(),)

def create_dispatcher():
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation()
    )
    dispatcher.include_router(quiz_router)
    scene_register = SceneRegistry(dispatcher)
    scene_register.add(QuizScene)
    return dispatcher


async def main():
    dispatcher = create_dispatcher()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())