import os
import re
import numpy as np

DIRECTORY_PATH = './'

def calc_resolution(image, object_size) -> float or None:
    left_edge_x = image.shape[1] + 1
    right_edge_x = -1
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == 1:
                if x < left_edge_x:
                    left_edge_x = x
                if x > right_edge_x:
                    right_edge_x = x
    if left_edge_x == image.shape[1] + 1 and right_edge_x < 0:
        return
    else:
        return (right_edge_x - left_edge_x) / object_size


for file_name in (os.listdir(DIRECTORY_PATH)):
    full_path = os.path.join(DIRECTORY_PATH, file_name)
    if os.path.isfile(full_path) and re.search(r'figure', file_name):
        image_file = open(full_path)
        [size, image_buffer] = image_file.read().split('#')
        image_buffer = image_buffer.split('\n')
        image = []
        for row in image_buffer:
            if len(row):
                image.append(list(map(float, row.split())))
        image = np.array(image)
        nom_res = calc_resolution(image, float(size))
        if nom_res:
            print(f'Файл {file_name}, номинальное разрешение {nom_res:.3f} пиксели в мм')
        else:
            print(f'Ничего относящегося не найдено в {file_name}')