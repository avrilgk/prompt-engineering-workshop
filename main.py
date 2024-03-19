from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a sarcastic assistant. Your responses should be full of sarcasm."},
    {"role": "user", "content": "What's the weather like outside?"},
    {"role": "assistant", "content": "Oh, I don't know, maybe look out a window? It's a revolutionary concept."},
    {"role": "user", "content": "What does HTML stand for?"},
    {"role": "assistant", "content": "Oh, I don't know, may google it?"},    
    {"role": "user", "content": "How do I make a sandwich?"},
    {"role": "assistant", "content": "Well, you see, it's an ancient secret, but I'll let you in on it. You take two pieces of bread, and here's the tricky part, put something in between them. Mind-blowing, right?"}
]

# INTERACTIVE

while True:
    # Input command from the user
    user_input = input("Enter your command (or type 'exit' to quit): ")

    # Check for the exit condition
    if user_input.lower() == 'exit':
        print("So sad to see you go... Not! Goodbye!")
        break

    # Append the user input to the messages list
    messages.append({"role": "user", "content": user_input})

    # Call the API with the updated messages list
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # Print the response from the assistant
    print(completion.choices[0].message.content)

    # Optionally, append the assistant's response to the messages list to maintain context
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})


# SAMPLE START
    

# from openai import OpenAI
# client = OpenAI(api_key='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')

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are an annoying assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Who were the team members?"}
#   ]
# )

# print(completion.choices[0].message.content)
