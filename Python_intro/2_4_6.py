dir = "./python_stepik"
import os

with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk(f"{dir}/main"):
        if list(filter(lambda x: x.endswith('.py'), files)):
            f.write('{}\n'.format(current_dir))

with open('result.txt', 'r') as f:
