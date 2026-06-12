from autogen import ConversableAgent, GroupChat, GroupChatManager

llm_config = {"config_list": [{"model": "gpt-4", "api_key": "your_keyy"}]}

patient_agent = ConversableAgent(name="patient", system_message="You describe symptoms and ask for medical help", llm_config=llm_config)
diagnosis_agent = ConversableAgent(name="diagnoser", system_message="You analyze symptoms and provide a possible diagnosis", llm_config=llm_config)
pharmacy_agent = ConversableAgent(name="pharmacist", system_message="You are a pharmacist you recommend medications", llm_config=llm_config)
consultantion_agent = ConversableAgent(name="consultant", system_message="you consult with people", llm_config=llm_config)

groupchat = GroupChat(
    agents = [patient_agent, diagnosis_agent, pharmacy_agent, consultantion_agent]
    messages = []
    max_round=5,
    speaker_selection_method="round_robin"
)
print("welcome to the AI healthcare consultant please describe xx")

manager = GroupChatManager(name="manager", groupchat=groupchat)

symptoms = input("input symptoms")

response = patient_agent.initiate_chat(
    manager,
    message=f"I am feeling f{symptoms}. Can you help?"
)