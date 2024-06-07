####################################################################
# Get the api key from the secret.py folder.
# Other solutions include adding the key as an environment variable
# IMPORTANT: The key should NOT be uploaded to github or made public
####################################################################
import secret
key = secret.key
print( key)




####################################################################
# Imports the openai API
# Adds the api key so that I can make requests
####################################################################
import openai
openai.api_key = key

####################################################################
# Get Respons does a request to open ai to get answer to our prompt
# The prompt argument is what we are asking the AI to do or answer
# Model referes to what AI model we are asking, we could ask 
# ChatGPT-3.5 for standard LLM use but also ask DALL-E for images
# In messages there is a list, we could expand the list to for 
# example take on a role as a dataconverter, and then feed data through
# the prompt variable.
# Documentation: https://platform.openai.com/docs/quickstart
####################################################################
def get_respons(prompt):
    respons = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user", "content":prompt}
        ]
    )
    return respons


####################################################################
# Main fuction
# asks for user_prompt as an input we give, we can redefine what the
# user_prompt is such that it can give different kind of prompt, for
# example file data.
####################################################################
if __name__ == "__main__":
    while True:
        user_prompt = input("Enter your prompt: ")
        if user_prompt.lower() in ["exit", "quit"]:
            break
        respons = get_respons(user_prompt)
        print("AI Respons:", respons.choices[0].message.content)

####################################################################
# Expansion ideas
# Get the AI to work with dataframes, or with excell
# There is a option to force answers to be JSON, there might be a
# use for this
# 
####################################################################