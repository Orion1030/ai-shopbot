import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


openai.api_key = OPENAI_API_KEY

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, "product_catalog.json"), "r") as file:
    product_catalog = json.load(file)
FUNCTIONS = [  
    {  
        "name": "getProductInfo",  
        "description": "Retrieve comprehensive details about a specified product, including its features, specifications, price, and availability. This function is useful for retrieving product information for e-commerce websites or inventory management systems.",  
        "parameters": {  
            "type": "object",  
            "properties": {  
                "productName": {  
                    "type": "string",  
                    "description": "The exact name of the product the user wishs to look up."
                }  
            },  
            "required": ["productName"]  
        }  
    },  
    {  
        "name": "checkStock",  
        "description": "Determine the current stock status of a specified product. This function helps retailers or e-commerce platforms quickly check whether a product is available for sale, which is crucial for managing customer expectations and inventory levels.",  
        "parameters": {  
            "type": "object",  
            "properties": {  
                "productName": {  
                    "type": "string",  
                    "description": "The name of the product whose stock the user wants to verify."  
                }  
            },  
            "required": ["productName"]  
        }  
    },
    {  
        "name": "clearCache",  
        "description": "Efficiently manages and clears the system cache to optimize performance. This function handles cache invalidation, removes temporary data, and ensures smooth operation of the e-commerce platform. Use this when system performance needs optimization or when implementing updates that require fresh cache states. Returns confirmation of successful cache clearance along with memory space recovered.",
        "parameters": {  
            "type": "object",  
            "properties": {
                "scope": {
                    "type": "string",
                    "enum": ["all", "lastOne"],
                    "description": "Specifies the cache scope to be cleared - 'all': for whole system cache, 'lastOne': targets the most recent conversation history."
                }
            }, 
            "required": ["scope"]  
        }  
    }  
]

class ChatBot:
    def __init__(self):  
        self.messages = []
    def initialize(self):
        try:
            self.messages = [
                {"role": "system", "content": "You are ShopBot, an AI assistant for our e-commerce platform. Help users with product details and availability. For functions, use more friendly descirptions. And must remember you are a shop bot. Avoid any non-related responses."},
                {"role": "user", "content": "Hi there."},
            ]
            response = openai.ChatCompletion.create(
                    model="gpt-4o",
                    messages=self.messages,
                )
            message =  response.choices[0].message._previous
            self.messages.append(message)

            return message['content']
        except Exception as e:
            print(e)
            return "Error: " + str(e)

    def delectLastHist(self):
        while (self.messages[-1]["role"] != "user"):
            self.messages.pop()
        self.messages.pop()
        return "Previous message has been removed successfully. Ready for our next conversation!"

    def chatWithAssistant(self, user_input):
        try:
            self.messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=self.messages,
                functions=FUNCTIONS,
                function_call="auto"
            )

            message = response.choices[0].message._previous
            self.messages.append(message)

            if message.get("function_call"):
                function_name = message["function_call"]["name"]
                function_args = json.loads(message["function_call"]["arguments"])
                return self.processFunctionCallResponse(function_name, function_args)

            return message['content']
        except Exception as e:
            self.initialize()

    def processFunctionCallResponse(self, function_name, function_args):
        if function_name == "clearCache":
            if function_args["scope"] == "all":
                return self.initialize()
            elif function_args["scope"] == "lastOne":
                return self.delectLastHist()
            else:
                return "Please provide a valid input to continue our conversation!"
        else:
            if function_name == "getProductInfo":
                result = getProductInfo(**function_args)
            elif function_name == "checkStock":
                result = checkStock(**function_args)
            self.messages.append({"role": "function", "name": function_name, "content": json.dumps(result)})

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=self.messages,
        )
        message =  response.choices[0].message._previous
        self.messages.append(message)

        return message['content']

def getProductInfo(productName):
    for product in product_catalog:
        if product['name'].lower() == productName.lower():
            return {
                "product_id": product["id"],
                "name": product["name"],
                "description": product["description"],
                "price": product["price"],
                "stock": product["stock"]
            }
    return None


def checkStock(productName):
    for product in product_catalog:
        if product['name'].lower() == productName.lower():
            return product["stock"] > 0
    return None

def main():
    
    chat_bot = ChatBot()
    print("Welcome to the e-commerce assistant! Type 'exit' to end the conversation.\n")
    print(f"ShopBot: {chat_bot.initialize()}")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Thank you for using ShopBot. Goodbye!")
            break

        response = chat_bot.chatWithAssistant(user_input)
        print(f"ShopBot: {response}")

if __name__ == "__main__":
    main()