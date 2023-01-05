from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!', 'hi', 'how are you?', 'I am good.', 'that is good to hear.', 'thank you', 'you are welcome.', 'bye', 'goodbye', 'see you later']

math_talk_1 = ['pythagorean theorem', 'a squared plus b squared equals c squared', 'what is the Pythagorean theorem?', 'a squared plus b squared equals c squared']

math_talk_2 = ['law of cosines', 'c squared equals a squared plus b squared minus two a b cosine of C', 'what is the law of cosines?', 'c squared equals a squared plus b squared minus two a b cosine of C']

list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)