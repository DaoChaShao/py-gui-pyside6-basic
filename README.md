<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
This repository demonstrates how to utilise the basic knowledge of PySide6 and PySide6 Designer to create a UI
interface.

**QUICK START**
---

1. If your network is capable, install NiceGUI with the command:
    ```bash
    pip install pyside6
    ```
2. If you are in domestic area, run the command:
    ```bash
    pip install -i https://mirrors.aliyun.com/pypi/simple/ pyside6
    ```

**PYSIDE6 DESIGNER USAGE**
---

1. Normally, you can code in Pycharm or VSCode while using PySide6. Of course, you can also use `PySide6 Designer` to
   design the UI interface and check the attributes of the widgets by running the command:
    ```bash
    pyside6-designer
    ```
2. After designing the UI interface, you can save the file as a `.ui` file and convert it to a Python file by running
   the command:
    ```bash
    pyside6-uic your_ui_file.ui -o your_python_file.py
    ```
3. Use the **static load method** to build the connection between the UI and the backend logic in your Python code.  
   **Method I**: `Composition`(**Recommended**):
   ```python
   from your_python_file import Ui_Form
   from PySide6.QtWidgets import QMainWindow

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           self.ui = Ui_Form()
           self.ui.setupUi(self)
   ```
   **Method II**: `Inheritance`:
   ```python
   from your_python_file import Ui_Form
   from PySide6.QtWidgets import QMainWindow

   class MainWindow(QMainWindow, Ui_Form):
       def __init__(self):
           super().__init__()
           self.setupUi(self)
   ```
4. Use the **dynamic load method** to build the connection between the UI and the backend logic in your Python code.
   ```python
   from PySide6.QtUiTools import QUiLoader
   from PySide6.QtWidgets import QMainWindow
   from PySide6.QtCore import QFile

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           ui_file = QFile("your_ui_file.ui")
           ui_file.open(QFile.Permission.ReadOnly)
   
           loader = QUiLoader()
           self.ui = loader.load(ui_file, self)
           ui_file.close()
   ```

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

**LICENCE**
---
This application is licensed under the [BSD-3-Clause Licence](LICENCE). You can click the link to read the licence.

**CHANGELOG**
---
This guide outlines the steps to automatically generate and maintain a project changelog using git-changelog.

1. Install the required dependencies with the command:
    ```bash
    pip install git-changelog
    ```
2. Run the command
    ```bahs
    pip show git-changelog
    ```
   or
    ```bash
    pip show git-changelog | grep Version
    ```
   to check whether the changelog package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command
    ```bash
    git-changelog --output CHANGELOG.md
    ```
   to commit the changes and updating the changelog.
6. Push the changes to the remote repository with the command
    ```bash
    git push origin main
    ```
   or using the UI interface button named `Git -> Push`.