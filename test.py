# # This file is used to verify your http server acts as expected
# # Run it with `python3 test.py``

# import requests

# model_inputs = {'prompt': 'My favorite part about working with AI is'}

# res = requests.post('http://localhost:8000/', json = model_inputs)

# print(res.json())
import banana_dev as client
from io import BytesIO
from PIL import Image
import time

# Localhost test
my_model = client.Client(
    api_key="",
    model_key="",
    url="http://localhost:8000",
)

inputs = {
    "prompt": "Tell me about AI.",
    "max_new_tokens": 128
}

# Call your model's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first
# method argument ("/")to specify a
# different route.
t1 = time.time()
result, meta = my_model.call("/", inputs)
t2 = time.time()
print("Time to run: ", t2 - t1)
print(result)
