# from matplotlib import pyplot as plt
# from matplotlib import patches
from PIL import Image
# from os import listdir
from mtcnn.mtcnn import MTCNN
import numpy as np
from io import BytesIO
from queue import Queue
import threading


"""
accepts raw image content as bytes
"""
def extract_faces(image):
    img1 = Image.open(BytesIO(image))
    img1 = img1.convert('RGB')
    pixels = np.asarray(img1)
    detector = MTCNN()
    
    f = detector.detect_faces(pixels)

    return f
    # print(f)


"""
accepts raw image content as bytes
"""
def extract_faces_multi(image, q):
    img1 = Image.open(BytesIO(image))
    img1 = img1.convert('RGB')
    pixels = np.asarray(img1)
    detector = MTCNN()
    
    f = detector.detect_faces(pixels)

    q.put(f)


# def extract_faces(images):
#     q = Queue()
#     threads = []
#     for image in images:
#         t = threading.Thread(target=extract_faces, args=(url, q))
#         t.start()
#         threads.append(t)

#     faces = []
#     for i in range(len(urls)):
#         images.append(q.get())

#     for t in threads:
#         t.join()

#     return faces
    



# # %%
# plt.imshow(pixels)

# # %%

# # %%
# fig, ax = plt.subplots()
# faces = []
# ax.imshow(pixels)
# for face in f:
#     x, y, w, h = face['box']
#     faces.append(pixels[y:y+h, x:x+h])
#     rect = patches.Rectangle((x,y), w, h, linewidth=1, edgecolor='r', facecolor='none')
#     ax.add_patch(rect)

# # %%
# fig, ax = plt.subplots(len(faces))

# for i, face in enumerate(faces):
#     ax[i].imshow(face)
# fig.show()

# # %%
# faces_resized = [Image.fromarray(x) for x in faces]
# faces_resized = [x.resize((160, 160)) for x in faces_resized]
# faces_resized = [np.asarray(x) for x in faces_resized]
# fig, ax = plt.subplots(1, 6)
# for i, face in enumerate(faces_resized):
#     ax[i].imshow(face)
# fig.show()

# # %%



