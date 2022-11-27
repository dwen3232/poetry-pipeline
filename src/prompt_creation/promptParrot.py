import replicate
import os

#TODO: integrate this with pipeline so you dont have to manually set p and also make it return in 
#      a way that is usable to rest of pipeline!!!

#change this to the prompt
p = "dog sit hill watch star"

#API token
os.environ["REPLICATE_API_TOKEN"] = "bf7fbdd8144303e138d49a8a4caf32340a8c818d"

#setup stuff for prompt parrot
model = replicate.models.get("kyrick/prompt-parrot")
version = model.versions.get("7349c6ce7eb83fc9bc2e98e505a55ee28d7a8f4aa5fb6f711fad18724b4f2389")

#getting the cooler prompts B)
returnedPrompts = version.predict(prompt=p)

#making it into a list and removing the dash lines
output = returnedPrompts.split("\n------------------------------------------\n")

#printing returned prompts
for x in output:
    print(x)
    print()

