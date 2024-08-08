from PIL import Image
from pwn import xor


"""
We are unable to get the "flag" image alone. So the best result 
we can get is by xoring both encrypted images. This way:
(lemur ^ key) ^ (flag ^ key) == (lemur ^ flag).
Converting the resulting bytes to image gives us a "mix" of 
both images, still revealing the flag.
"""
def solve():
    img_lemur = Image.open("lemur.png")
    img_flag = Image.open("flag.png")

    bLemur = img_lemur.tobytes()
    bFlag = img_flag.tobytes()

    mixed = xor(bLemur, bFlag)
    flag = Image.frombytes(img_flag.mode, img_flag.size, mixed)
    flag.save("answer.png")


if __name__ == '__main__':
    solve()