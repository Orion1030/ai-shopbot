#
# AI E-Commerce Assistant

## Project Overview

The **AI E-Commerce Assistant** (named **ShopBot**) is a Python application designed to demonstrate the use of OpenAI's Assistant API, specifically leveraging the **gpt-4o** model with function calling capabilities. This assistant helps users interact with a mock e-commerce product catalog, answering queries about product details and availability. The project showcases proficiency in API integration, function calling, and interactive user experiences using OpenAI's tools.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Product Catalog](#product-catalog)
- [Functionality](#functionality)
- [Additional Features](#additional-features)
- [Example Conversation](#example-conversation)
- [License](#license)


## Features

- **AI-powered product inquiry:** Users can ask about products, and ShopBot will provide detailed information.
- **Function calling:** Uses OpenAI's function calling to interact with product data.
- **Real-time stock checking:** The assistant can verify if a product is available in stock.
- **Conversation management:** Allows clearing chat history or deleting the last message.(Bonus Feature)

---

## Tech Stack

- **Python** (v3.9+)
- **OpenAI API** (using `gpt-4o` model)
- **JSON** (for the mock product catalog)
- **dotenv** (for environment variable management)

---

## Project Structure

```plaintext
.
├── main.py
├── .env
├── product_catalog.json
├── README.md
└── requirements.txt
```

- **main.py** The core script to run the AI assistant.
- **.env** Stores sensitive information like the OpenAI API key.
- **product_catalog.json** Contains mock product data.
- **functions_schema.json** Defines function calling schema for the assistant.
- **requirements.txt** Lists required Python packages.

## Installation

Clone the repository:

```plaintext
git clone https://github.com/Orion1030/ai-shopbot.git
cd ai-shopbot
```

Create a virtual environment (optional but recommended):

```plaintext
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:


```plaintext
pip install -r requirements.txt
```
Set up your OpenAI API Key:

Create a .env file in the project root:
bash
```plaintext
OPENAI_API_KEY=your-openai-api-key
```
## Usage
Run the application:


```plaintext
python main.py
```
Interact with ShopBot:

- Type your product-related queries in the console.
- Type exit or quit to end the conversation.

## Product Catalog
The product catalog is stored in product_catalog.json. Here’s an example structure:


```plaintext
[
  {
    "id": 1,
    "name": "EcoFriendly Water Bottle",
    "description": "A sustainable water bottle made from recycled materials.",
    "price": 15.99,
    "stock": 20
  },
  {
    "id": 2,
    "name": "Bluetooth Headphones",
    "description": "Wireless headphones with noise-canceling features.",
    "price": 59.99,
    "stock": 5
  }
]
```
Feel free to edit this file to add more products or modify existing ones.

## Functionality
### Available Functions
The assistant can call the following functions:

1. `getProductInfo(productName)`

    - Retrieves product details such as ID, name, description, price, and stock.

2. `checkStock(productName)`
    - Checks if a product is currently in stock.
3. `Conversation Management (Bonus Feature)`
    - clearCache(scope): Resets the conversation history.
        - `scope="all"` clears all history.
        - `scope="lastOne"` deletes only the last message.
### How Function Calling Works
The function schemas are defined in main.py:


```plaintext
[
  {
    "name": "getProductInfo",
    "parameters": {
      "type": "object",
      "properties": {
        "productName": {"type": "string"}
      }
    }
  },
  {
    "name": "checkStock",
    "parameters": {
      "type": "object",
      "properties": {
        "productName": {"type": "string"}
      }
    }
  }
]
```
### Additional Features
- Error Handling: Automatically resets the conversation in case of an API error.
- Conversation Continuity: Maintains chat history for a seamless user experience.
### Example Conversation

```plaintext
Welcome to the e-commerce assistant! Type 'exit' to end the conversation.

ShopBot: Hello! How can I assist you today?

User: Tell me about the "Bluetooth Headphones".
ShopBot: The Bluetooth Headphones are wireless headphones with noise-canceling features, priced at $59.99. We currently have 5 units in stock.

User: Are they available?
ShopBot: Yes, the Bluetooth Headphones are available.

User: Clear the last message.
ShopBot: Previous message has been removed successfully. Ready for our next conversation!

User: exit
Thank you for using ShopBot. Goodbye!
```
### License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute as per the license.

#

## Author
- Kevin Ricardo Ramirez Cadavid
## Acknowledgements
- Special thanks to OpenAI for providing the API resources and documentation.
