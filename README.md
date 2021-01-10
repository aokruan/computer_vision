# Инструкция по настройке проекта по распознаванию номерных знаков транспортных средств

## Сайт номеров нет: https://nomeroff.net.ua/
```github:https://github.com/ria-com/nomeroff-net```

## Install python requirments
```python
pip3 install torch
pip3 install PyYAML==5.3
```

```python
// Если будут проблемы с установкой, то изменить кавычки
pip3 install "git+https://github.com/facebookresearch/detectron2.git"

pip3 install torchvision
pip3 install Cython
pip3 install numpy
pip3 install -r requirements.txt
```

## For Ubuntu and other Debian-like OS:
```bash
# ensure that you have installed gcc compiler
apt-get install gcc

# for opencv install
apt-get install -y libglib2.0
apt-get install -y libsm6
apt-get install -y libfontconfig1 libxrender1
apt-get install -y libxtst6

# for pycocotools install (Check the name of the dev-package for your python3)
apt-get install python3.6-dev
```

```python

pip install imutils
pip install contours

$ (env)> pip install pytesseract
$ (env)> pip install -U git+https://github.com/madmaze/pytesseract.git
pip install tesseract
pip install tesseract-ocr

```

Tesseract — свободная компьютерная программа для распознавания текстов, разрабатывавшаяся Hewlett-Packard.

tesseract is not installed or it's not in your PATH. See README file for more information."
* Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki 

* Note the tesseract path from the installation.Default installation path at the time the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

* pip install pytesseract

* Set the tesseract path in the script before calling image_to_string:

```python

// Add variable
pytesseract.pytesseract.tesseract_cmd = "D:\Program Files\Tesseract-OCR\\tesseract.exe"
```

WINDOWS PATH: `D:\Program Files\Tesseract-OCR`  
SYSTEM PATH: `D:\Program Files\Tesseract-OCR`

```bash
tesseract -v
```

## Определение номера

### Тест 1  
Фотография c масштабом во всю машину:  
<img width="400" height="280" src="https://user-images.githubusercontent.com/49877495/104123318-2b746d80-537d-11eb-9daa-a7b309ddb7eb.png">  

```text
А 799 рь 24.
—А792Рр21.
```
Фотография с капотом и номером:  
<img width="400" height="280" src="https://user-images.githubusercontent.com/49877495/104123364-6c6c8200-537d-11eb-98c6-9ffbbf2b830b.png">

```text
`А792Рр 21.
[some symbols]
```

Фотография с номером:  
<img width="400" height="280" src="https://user-images.githubusercontent.com/49877495/104123368-755d5380-537d-11eb-92fe-3d9e5fe4595c.png">

```text
`А792Рр 21.
[some symbols]
```
`Вывод`: с уменьшением масштаба увеличивается успех определения.
Для лучшего эффекта нобходимо определять номерную рамку и редактировать фотографию до размера номерной рамки.

### Тест 2  
Фотография c масштабом во всю машину:  
<img width="400" height="280" src="https://user-images.githubusercontent.com/49877495/104123489-12b88780-537e-11eb-93bf-c81cdddfacf8.png">  

```text
__ "И

-н 183 нр 24.
[some symbols]
```
Фотография с номером:  
<img width="400" height="280" src="https://user-images.githubusercontent.com/49877495/104123438-c1a89380-537d-11eb-986b-6e27c9d1c172.png">

```text
null
```
`Вывод`: нет вариантов почему так происходит.


