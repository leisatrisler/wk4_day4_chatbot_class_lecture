from fuzzywuzzy import fuzz
import re

class ChatBot:
    def _init_(self):
        self.name = "Sky Net"
        self.user_name = "User"
    
    def save_user_name(self, user_name):
        self.save_user_name = user_name

    def get_user_info(self):
        print("What is your name? ")
        name=input(f"{self.user_name}: ")
        self.save_user_name(name)
        print(f"Welcome{name}")
    
    def get_response(self, user_imput):
        fuzzy_match_threshold = 70 #can change this if needed

        #Define our imput phrases with their answers
        predefined_inputs = {
            "Hello": f"Hi {self.user_name}!",
            "How are you?": "I'm am super awesome. Thanks for asking!",
            "Who are you?":f"I'm a chatbot me name is {self.name}",
            "How do you convince people?": "I'm going make them an offer they can't refuse",
            "What is your favorite food": "Oranges and olive oil",
            "What us the answer to life Universe and Everything": 42
        }

        #Tokenize the user input
        user_input_tokens = re.findall(r'\w+',user_input.lower())

        best_match = None
        best_match_ratio = 0

        for imput_phrase in predefined_inputs:
            # Tokenize the predefined input keys
            input_phrase_tokenss = re.findall(r'\w+',input_phrase.lower())
            match_ratio = fuzz.partial_ratio(user_input_tokens, input_phrase_tokenss)

            if match_ratio > best_match_ratio:
                best_match = input_phrase
                best_match_ratio = match_ratio

        #Generate our response based on the best match
        if best_match and best_match_ratio > fuzzy_match_threshold:
            return predefined_inputs[best_match]
        else:
            return "English? Do you speak it"
        
    def start_chat(self):
        print(f"Welcome! I'm {self.name}")
        self.get_user_info()
        print("What can I do for you today?")
        
