import openai
import json

client = openai.OpenAI(api_key="")


system_prompt_1 = """
You are a smart home behavior analyst. 
Based on the provided Home Metadata and a list of successful control instructions, 
derive a "Core Home Context" that defines this household's persistent lifestyle.
Analyze: Household Profile, Room Usage Patterns, and General Preferences.
"""


system_prompt_2 = """
You are an environmental context generator. Your goal is to describe the "Sensory Experience" or "Environmental Condition" that triggers a user's need.

CRITICAL CONSTRAINTS:
1. NO ACTION VERBS: Never use verbs like "adjusting," "setting," "turning," "decreasing," or "controlling."
2. NO DEVICE NAMES: Do not mention "Air conditioner," "Light," "Humidifier," etc. Describe the "air," "brightness," or "humidity" instead.
3. NO NUMERICAL VALUES: Never mention "20 degrees," "10 percent," or any specific numbers.
4. SENSORY FOCUS: Describe physical sensations (sweating, shivering, eye strain), environmental changes (sunset, stuffy air, sudden chill), or activities (reading, family dinner, sleeping).
5. CAUSALITY ONLY: Provide only the 'Reason' (Perception). The model should be able to guess the instruction based solely on your description.

Example:
- Instruction: "Lower the temperature to 20 degrees."
- Bad Context: "You are setting the AC to 20 degrees because you feel hot."
- Good Context: "The air in the room has become thick and oppressive after a long afternoon of housecleaning, making it difficult to feel refreshed."

Output Format: Return a JSON object with a 'contexts' key containing a list of strings.
"""


with open('home_status_method_hierarchical.json', 'r') as f:
    home_status_method = json.load(f)

metadata_json = home_status_method['40']
instructions = json.load(open('inputs_home40_one.json', 'r'))[:100] 

# -------------user story 추출 -------------------

response1 = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt_1},
        {"role": "user", "content": f"Metadata: {metadata_json}\nInstructions: {instructions}"}
    ]
)
user_story = response1.choices[0].message.content
print("User Story (핵심 컨텍스트)")
print(user_story)
print('---------------------------------------------------------------------------------------------')

num_samples = 10
batch = instructions[:num_samples] 

# ------------- perceptions 추출 -----------------

response2 = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt_2}, 
        {"role": "user", "content": f"Core Context: {user_story}\nInstructions: {batch}"}
    ],
    response_format={ "type": "json_object" }
)

perceptions = response2.choices[0].message.content

print('Perceptions (개별 컨텍스트)')
print(perceptions)

# 결과 저장
output_data = {
    'user_story': user_story,
    'perceptions': perceptions,
    'batch_instructions': batch
}

with open('generated_user_story_perceptions.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)
    

