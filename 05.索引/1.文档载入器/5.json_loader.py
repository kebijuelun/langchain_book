import json
from pathlib import Path
from pprint import pprint

from langchain.document_loaders import JSONLoader

# file_path='./example_data/facebook_chat.json'
file_path = "/home/lwz/zwp_code/langchain-master/docs/extras/modules/data_connection/document_loaders/integrations/example_data/facebook_chat.json"

# data = json.loads(Path(file_path).read_text())

# pprint(data)
# -> {'image': {'creation_timestamp': 1675549016, 'uri': 'image_of_the_chat.jpg'},
# ->  'is_still_participant': True,
# ->  'joinable_mode': {'link': '', 'mode': 1},
# ->  'magic_words': [],
# ->  'messages': [{'content': 'Bye!',
# ->                'sender_name': 'User 2',
# ->                'timestamp_ms': 1675597571851},
# ->               ......
# ->               {'content': 'Hi! Im interested in your bag. Im offering $50. Let '
# ->                           'me know if you are interested. Thanks!',
# ->                'sender_name': 'User 1',
# ->                'timestamp_ms': 1675549022673}],
# ->  'participants': [{'name': 'User 1'}, {'name': 'User 2'}],
# ->  'thread_path': 'inbox/User 1 and User 2 chat',
# ->  'title': 'User 1 and User 2 chat'}

# print(file_path)
loader = JSONLoader(
    # file_path=file_path,
    file_path="/home/lwz/zwp_code/langchain-master/docs/extras/modules/data_connection/document_loaders/integrations/example_data/facebook_chat.json",
    text_content=False,
    jq_schema=".messages[].content",
)

data = loader.load()

pprint(data)
