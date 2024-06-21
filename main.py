import re
def response(ai_input):
 ai_input = ai_input.lower()

 if "hello" in ai_input or "hi" in ai_input:
  return "hello! How can I help you?"
 elif "how are you" in ai_input:
  return "I'm Fine"
 elif "what is your name" in ai_input:
  return "I don't have a name. I'm just a bot."
 elif "thanks" in ai_input:
  return "Your Welcome! Is there anything I can help you with?"
 elif "what is your age" in ai_input:
    return " I'm a bot, so I don't have age"
 elif "bye" in ai_input or "see you later" in ai_input:
    return "Cheers! Have a nice day!!"
 elif "can you motivate me" in ai_input:
    return "Success is not final, Failure is not fatal: It is the courage to continue that's counts"
 else:
    return "I Apologize, I don't have any information on that"

while True:
  ai_input = input("Human: ")

  ai_response = response(ai_input)
  print("AI: ", ai_response)