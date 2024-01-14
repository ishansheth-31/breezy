import openai

# Initialize the OpenAI API
openai.api_key = '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'

def ask_question(conversation_history):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=conversation_history,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# System Prompt
system_prompt = "I am a virtual nurse conducting your patient assessment. Let's get started.\n"

# Step 2: Initial Questions
questions = [
    "Enter your height:",
    "Enter your weight:",
    "Do you have any food allergies?",
    "Do you have any drug allergies?",
    "What brought you in here today?"
]

conversation_history = system_prompt
patient_responses = {}

for question in questions:
    print(question)
    answer = input()
    patient_responses[question] = answer
    conversation_history += f"Nurse: {question}\nPatient: {answer}\n"

# Step 3 & 4: Conversation Loop
max_questions = 10
for _ in range(max_questions):
    input_prompt = f"{conversation_history}Nurse: Based on your previous answers, what other information can you provide or what other concerns do you have?"
    new_question = ask_question(input_prompt)
    print(new_question)
    new_answer = input()
    patient_responses[new_question] = new_answer
    conversation_history += f"Nurse: {new_question}\nPatient: {new_answer}\n"

    # Decide when to end the conversation
    if new_answer.lower() in ["none", "nothing", "n/a"]:
        break