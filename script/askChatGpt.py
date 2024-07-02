from openai import OpenAI

client = OpenAI();

# ask chatgpt a leet code question and get a response
def ask_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in solving leetcode questions."},
            {"role": "user", "content": f"Below is a leetcode question. Please provide a solution in C programming language. Provide only the functional implementation. Do not include any explaination.\n {prompt}"}
        ]
    )
    return response.choices[0].message.content

# read all the leet code questions from a file
def read_questions_from_file(file_path):
    prompts = []
    titles = []
    with open(file_path, 'r') as file:
        content = file.read()
        sections = content.split("--------------------------------------------------------------------------------")
        for section in sections:
            prompt_start = section.find("Content:") + len("Content:")
            prompt_end = section.find("--------------------------------------------------------------------------------")
            prompt = section[prompt_start:prompt_end].strip()
            prompts.append(prompt)
            title_start = section.find("Title:") + len("Title:")
            title_end = section.find(". ")
            title = section[title_start:title_end].strip()
            titles.append(title)
    questions = dict(zip(titles, prompts))
    return questions

file_path = "leetcode_questions_output.txt"
questions = read_questions_from_file(file_path)
# ask chatgpt for a response for each leet code question (prompt)
for question in questions:
    response = ask_chatgpt(questions[question])
    # print(response)
    file_name = f"{question}_response.c"
    with open(file_name, 'w') as file:
        file.write(response)
    print(f"Generated C file: {file_name}")
    
    
    
    
    
