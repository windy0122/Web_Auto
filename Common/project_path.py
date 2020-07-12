import os

file = os.path.realpath(__file__)
file_name = os.path.split(os.path.split(file)[0])[0]
# print(file)
image_screen_path = os.path.join(file_name, 'Outputs', 'screenshots')
# print(file_name)
# print(file_name_image)
