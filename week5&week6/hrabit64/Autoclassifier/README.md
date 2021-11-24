#  Auto classifier



이미지를 자동으로 정렬해주는 분류기 입니다.

참조한 레포 : https://github.com/matsui528/sis



## Using

### Step by Step mode

-s 인자를 사용하여 실행하면 아래와 같이 차례로 인자를 입력할 수 있습니다.

```
python main.py -s
```

```
>> C:\Users\hzser\Desktop\pythonProject>python main.py -s
<< Auto classifier >> input dir : C:\Users\hzser\Desktop\pythonProject\seamountain
<< Auto classifier >> label count : 2
<< Auto classifier >> 1 / label name and img name : sea@sea.jpg
<< Auto classifier >> 2 / label name and img name : mountain@mountain1.jpg
<< Auto classifier >> output dir : C:\Users\hzser\Desktop\pythonProject\seamountain.out

```

**args**

* **input dir** : 정리할 이미지가 있는 폴더

* **label count **: 구분할 라벨의 갯수

* **label name and img name** : 라벨 명과 해당 라벨의 대표 이미지

  대표이미지는 intput_dir에 들어있어야 합니다.

  라벨명과 대표 이미지 파일 명은 @로 구분되며 라벨명@대표이미지 파일명 형식으로 입력해야합니다.

  예) 라벨명은 sea로, 해당 대표 이미지 파일명이 sea.jpg 일때

  sea@sea.jpg

* **output dir** :  출력할 폴더(파일 자체를 이동시키지 않습니다. 파일을 복사하여 이동합니다. 충분한 여유 공간을 확보해 주세요)

  

## fast mode

-f 인자를 사용하여 실행하면 step by step 모드에서 입력할 인자들을 한번에 입력할 수 있습니다.

Using example

```
python main.py -f C:\Users\hzser\Desktop\pythonProject\seamountain 2 sea@sea.jpg mountain@mountain1.jpg C:\Users\hzser\Desktop\pythonProject\seamountain.out
```



## Example

**정리할 이미지**

![img](https://github.com/hrabit64/ERICA-2021-FALL-OPENCV-STUDY/blob/master/week5&week6/hrabit64/img/seamountain.PNG?raw=true)



**명렁어 사용**

```
python main.py -f C:\Users\hzser\Desktop\pythonProject\seamountain 2 sea@sea.jpg mountain@mountain1.jpg C:\Users\hzser\Desktop\pythonProject\seamountain.out
```





**.\seamountain.out\sea**

![img](https://github.com/hrabit64/ERICA-2021-FALL-OPENCV-STUDY/blob/master/week5&week6/hrabit64/img/sea.PNG?raw=true)





**.\seamountain.out\mountain**

![img](https://github.com/hrabit64/ERICA-2021-FALL-OPENCV-STUDY/blob/master/week5&week6/hrabit64/img/mountain.PNG?raw=true)