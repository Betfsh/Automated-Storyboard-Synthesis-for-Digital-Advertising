from langchain.agents import AgentType, initialize_agent
from langchain.schema import SystemMessage
import logging
from tools import generate_image, change_image_size, insert_text_on_image, combine_images_to_create_frame
insert_text_on_image, combine_images_to_create_frame 

logging.basicConfig(level=logging.INFO)

with open("system_message.txt", "r") as file:
    system_message = file.read()

def get_agent_executor(model_name='gpt-4-1106-preview', temperature=0):
        try:
        agent_kwargs = {
        "system_message": SystemMessage(content=system_message),
        }