import os
import argparse
from shutil import copyfile

#######
# CelebA attributes:
# ------
# 5_o_Clock_Shadow 1
# Arched_Eyebrows 2
# Attractive 3
# Bags_Under_Eyes 4
# Bald 5
# Bangs 6
# Big_Lips 7
# Big_Nose 8
# Black_Hair 9
# Blond_Hair 10
# Blurry 11
# Brown_Hair 12
# Bushy_Eyebrows 13
# Chubby 14
# Double_Chin 15
# Eyeglasses 16
# Goatee 17
# Gray_Hair 18
# Heavy_Makeup 19
# High_Cheekbones 20
# Male 21
# Mouth_Slightly_Open 22
# Mustache 23
# Narrow_Eyes 24
# No_Beard 25
# Oval_Face 26
# Pale_Skin 27
# Pointy_Nose 28
# Receding_Hairline 29
# Rosy_Cheeks 30
# Sideburns 31
# Smiling 32
# Straight_Hair 33
# Wavy_Hair 34
# Wearing_Earrings 35
# Wearing_Hat 36
# Wearing_Lipstick 37
# Wearing_Necklace 38
# Wearing_Necktie 39
# Young 40
#######

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--celeba_root', default='')
    parser.add_argument('--celeba_attributes', default='')
    parser.add_argument('--dest', default='')
    parser.add_argument('--num_test_imgs', default='64')
    parser.add_argument('--configuration', default='eyeglasses')

    args = parser.parse_args()

    os.mkdir(args.dest)

    os.mkdir(os.path.join(args.dest, 'trainA'))
    os.mkdir(os.path.join(args.dest, 'trainB'))
    os.mkdir(os.path.join(args.dest, 'testA'))
    os.mkdir(os.path.join(args.dest, 'testB'))

    trainA = []
    trainB = []

    with open(args.celeba_attributes) as f:
        lines = f.readlines()

    # Eyeglasses
    if args.configuration == 'eyeglasses':
        for line in lines[2:]:
            line = line.split()
            if int(line[16]) == 1:
                trainA.append(line[0])
            elif int(line[16]) == -1:
                trainB.append(line[0])

    # Mouth slightly open
    if args.configuration == 'mouth':
        for line in lines[2:]:
            line = line.split()
            if int(line[22]) == 1:
                trainA.append(line[0])
            else:
                trainB.append(line[0])

    # Facial hair
    if args.configuration == 'beard':
        for line in lines[2:]:
            line = line.split()
            if int(line[21]) == 1 and int(line[1]) == -1 and (int(line[23]) == 1 or int(line[17]) == 1 or int(line[25]) == -1): # male AND (mustache OR goatee OR beard) AND (no shadow)
                trainA.append(line[0])
            elif int(line[21]) == 1 and int(line[25]) == 1 and int(line[1]) == -1:                                              # male AND (no beard, no shadow)
                trainB.append(line[0])

    testA = trainA[:args.num_test_imgs]
    testB = trainB[:args.num_test_imgs]
    trainA = trainA[args.num_test_imgs:]
    trainB = trainB[args.num_test_imgs:]

    all_imgs = os.listdir(args.celeba_root)

    for _img in testA:
        src = os.path.join(args.celeba_root, _img)
        dst = os.path.join(args.dest, 'testA', _img)
        copyfile(src, dst)

    for _img in testB:
        src = os.path.join(args.celeba_root, _img)
        dst = os.path.join(args.dest, 'testB', _img)
        copyfile(src, dst)

    for _img in trainA:
        src = os.path.join(args.celeba_root, _img)
        dst = os.path.join(args.dest, 'trainA', _img)
        copyfile(src, dst)

    for _img in trainB:
        src = os.path.join(args.celeba_root, _img)
        dst = os.path.join(args.dest, 'trainB', _img)
        copyfile(src, dst)
