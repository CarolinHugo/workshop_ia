import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

rock_dir = os.path.join('./chifoumi_ia_2/rps/rock')
paper_dir = os.path.join('./chifoumi_ia_2/rps/paper')
scissors_dir = os.path.join('./chifoumi_ia_2/rps/scissors')

rock_files = os.listdir(rock_dir)
paper_files = os.listdir(paper_dir)
scissors_files = os.listdir(scissors_dir)

pic_index = 2

next_rock = [os.path.join(rock_dir, fname) for fname in rock_files[pic_index-2:pic_index]]
next_paper = [os.path.join(paper_dir, fname) for fname in paper_files[pic_index-2:pic_index]]
next_scissors = [os.path.join(scissors_dir, fname) for fname in scissors_files[pic_index-2:pic_index]]

fig, axes = plt.subplots(3, 2, figsize=(8, 8))

for ax, img_path in zip(axes[0], next_rock):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.set_title('Rock')
    ax.axis('off')

for ax, img_path in zip(axes[1], next_paper):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.set_title('Paper')
    ax.axis('off')

for ax, img_path in zip(axes[2], next_scissors):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.set_title('Scissors')
    ax.axis('off')

plt.tight_layout()
plt.show()
