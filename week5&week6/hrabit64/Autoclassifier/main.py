import os
import sys
from classification.classifier import classifier

# https://github.com/matsui528/sis
# python main.py -f C:\Users\hzser\Desktop\pythonProject\seamountain 2 sea@sea.jpg mountain@mountain1.jpg C:\Users\hzser\Desktop\pythonProject\seamountain.out

if __name__ == "__main__":

    if (str(sys.argv[1]) == '-s'):

        input_dir = input("<< Auto classifier >> input dir : ")

        if not os.path.exists(input_dir):

            print(f"<< Auto classifier >> Error! {input_dir} doesn't exist")
            raise FileExistsError

        if os.listdir(input_dir) is None:

            print(f"<< Auto classifier >> Error! {input_dir} is empty")
            raise FileExistsError

        label_count = int(input("<< Auto classifier >> label count : "))

        if not (0 < label_count or label_count < 100 or label_count is int):
            print(f"<< Auto classifier >> label count must be 0 < x < 100 and integer")
            raise ValueError

        rep_img = []

        for i in range(label_count):

            label_name,img_name = tuple(map(str,input(f"<< Auto classifier >> {i + 1} / label name and img name : ").split("@")))

            if not os.path.isfile(os.path.join(input_dir,img_name)):

                print(f"<< Auto classifier >> Error! {os.path.join(input_dir,img_name)} doesn't exist")
                raise FileExistsError

            rep_img.append((label_name,img_name))

        output_dir = input("<< Auto classifier >> output dir : ")

        if not os.path.exists(output_dir):

            print(f"<< Auto classifier >> Warning! {output_dir} doesn't exist. A directory was created automatically.")
            os.makedirs(output_dir)

        classifier(input_dir = input_dir,output_dir = output_dir,rep_img = rep_img)

    elif (str(sys.argv[1]) == '-f'):

        input_dir = str(sys.argv[2])

        if not os.path.exists(input_dir):
            print(f"<< Auto classifier >> Error! {input_dir} doesn't exist")
            raise FileExistsError

        if os.listdir(input_dir) is None:
            print(f"<< Auto classifier >> Error! {input_dir} is empty")
            raise FileExistsError

        label_count = int(sys.argv[3])

        if not (0 < label_count or label_count < 100 or label_count is int):
            print(f"<< Auto classifier >> label count must be 0 < x < 100 and integer")
            raise ValueError

        idx = 4
        rep_img = []

        for i in range(label_count):

            label_name, img_name = tuple(map(str, sys.argv[idx].split("@")))

            if not os.path.isfile(os.path.join(input_dir, img_name)):
                print(f"<< Auto classifier >> Error! {os.path.join(input_dir, img_name)} doesn't exist")
                raise FileExistsError

            rep_img.append((label_name, img_name))
            idx += 1

        output_dir = sys.argv[idx]

        if not os.path.exists(output_dir):
            print(f"<< Auto classifier >> Warning! {output_dir} doesn't exist. A directory was created automatically.")
            os.makedirs(output_dir)

        classifier(input_dir=input_dir, output_dir=output_dir, rep_img=rep_img)

    else:
        print(f"<< Auto classifier >> /' {sys.argv[1]} /' is an unknown args. \n"
              f"fast mode : -f\n"
              f"step by step mode : -s")
