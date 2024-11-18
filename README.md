# Wire_PNG
Electrical Wire Color Codes Into PNG





**How to Use This Code**


Step 1: Set Up a Python Virtual Environment

```
python3 -m venv mycolur

source mycolur/bin/activate
```


Step 2: Clone My GitHub Repository

```
git clone "https://github.com/Tpj-root/Wire_PNG.git"
```



Step 3: Install the Required Dependencies

```
pip install -r requirements.txt
```



Step 4: Edit your code

```
    createwire('navy')         # Creates a red.png file
    createwire('red', 'black') # Creates a red_black.png file
    create_image('navy')         # Creates a red.png file
    create_image('red', 'black') # Creates a red_black.png file
```



**createwire**

Creates a png file for 80x40 size looks like a wire


| Number | Color | Output  |
| --- |  --- | --- |
| 1 |  navy | <img src="color_png/wire_navy.png" width="80" height="40"> <p>navy</p> |
| 2 |  red black | <img src="color_png/wire_navy.png" width="80" height="40"> <p>red_black</p> |


**create_image**

Creates a png file for 20x20 size looks like a square


| Number | Color | Output  |
| --- |  --- | --- |
| 1 |  navy | <img src="color_png/square_navy.png" width="20" height="20"> <p>navy</p> |
| 2 |  red black | <img src="color_png/square_red_black.png" width="40" height="20"> <p>red_black</p> |



Step 5: Run the Code

```
python3 main.py
```

