# User Experience Guidelines

Accounting for user experience (UX) is handling how users interact with your napari package.
It is important to keep in mind that what you have designed for is not necessarily how users will try to interact with your package.
Achieving a good user experience will facilatate ease of use of your package and user efficiency, improving the overall perception of your package.
This page includes some overall considerations related to achieving a smooth UX in addtion to specific napari tips.

## Design considerations

Keeping the UX in mind throughout the software design process is very valuable, but it is never too late to start.
Some important design considerations are:

1. **Who** is your target user?
2. **What** problems are you solving or enabling the user to do, what is the user outcome?
3. **Wow** factor that makes your solution unique and impactful to your users, what sets your package apart from other similar packages?

### Further considerations

- Where might users get confused or break something?
- Does our plugin description or tutorial include all necessary information?
- Have we chosen the best GUI to help users best understand the plugin functionality?
- What other use cases might our plugin have?

### Getting user feedback

An important step in addition to assessing the user journey in using your package to overcome challenges, is to show your package to users and iterate with their feedback. See the CZI workshop for more information.

## napari Widget design considerations

A well designed widget enables your users to take full advantage of your widget functionality.
In addition to following the general design considerations above, there are specific considerations in creating a widget that can be helpful.

### Group similar actions together in your widget
Following the [Gestalt principles](https://www.toptal.com/designers/ui/gestalt-principles-of-design#:~:text=There%20are%20six%20individual%20principles,order%20(also%20called%20pr%C3%A4gnanz).), we naturally perceive nearby objects to be similar.
As such, grouping similar actions together enables a natural interation.
Containers and tabs can used to further group actions together and lessen clutter.
Keep in mind that the napari viewer is configurable. Users can float (or popout) your widget windows, move them around, organise them into containers with tabs etc. So try to keep pieces of functionality well grouped together.

This is achievable in both `magicgui` and `Qt`, in different manners.
For `magicgui` the primary method is to create multiple [containers](https://pyapp-kit.github.io/magicgui/usage/_autosummary/magicgui.widgets.Container.html#magicgui.widgets.Container) representing the grouped actions, and then combine these subcontainers together in one main widget container.
In `Qt`, there are multiple options, but [tabbed widgets](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html?highlight=qtabwidget) and [boxed wigets](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGroupBox.html?highlight=qgroupbox) are two great options.

```{note}
If the behaviour of the groups of actions in a single widget are independent from eachother, then creating multiple widgets instead is generally prefable over creating a single widget with grouped actions.
```

### Grouped widget example

````{tabbed} magicgui

```Python
from magicgui.widgets import Container, PushButton, FileEdit, FloatSlider

class MagicWidgetWithContainers(Container):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # 1. Setup container
        file_select = FileEdit(name="file_select", label="Input file", mode="r")
        setup_container = Container(name="setup", label="Setup", widgets=[file_select])

        # 2. Analysis container
        sigma_slider = FloatSlider(label="sigma")
        phi_slider = FloatSlider(label="phi")
        analysis_container = Container(
            label="Parameters", widgets=[sigma_slider, phi_slider]
        )

        # 3. Run container
        save_button = PushButton(name="save", label="Save parameters")
        run_button = PushButton(name="run", label="Run analysis")
        run_container = Container(
            widgets=[save_button, run_button], layout="horizontal", labels=False
        )

        # Add the subcontainers to main container and link functionality
        self.extend((setup_container, analysis_container, run_container))
        run_button.clicked.connect(
            lambda: print(f"Running on {self['setup']['file_select'].value}")
        )

if __name__ == "__main__":
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(
        MagicWidgetWithContainers(labels=True), name="Example Groups"
    )
    viewer.show(block=True)
```
````

````{tabbed} pyqt

```Python
from qtpy.QtWidgets import (
    QWidget,
    QLabel,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QHBoxLayout,
    QFormLayout,
    QDoubleSpinBox,
    QGroupBox,
)

class MyGroupedQWidget(QWidget):
    def __init__(self, use_tabs: bool = True, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setLayout(QVBoxLayout())

        # 1. Setup page
        setup_page = QWidget(self) if use_tabs else QGroupBox("Setup", self)
        setup_page.setLayout(QHBoxLayout())
        setup_page.layout().addWidget(QLabel("Select file to load"))
        self._file_select_text = QLineEdit(self)
        setup_page.layout().addWidget(self._file_select_text)
        self._browse_button = QPushButton("Browse")
        setup_page.layout().addWidget(self._browse_button)
        self._browse_button.clicked.connect(self.browse)

        # 2. Analysis page
        analysis_page = QWidget(self) if use_tabs else QGroupBox("Parameters", self)
        analysis_page.setLayout(QFormLayout())
        analysis_page.layout().addRow("sigma", QDoubleSpinBox(self))
        analysis_page.layout().addRow("phi", QDoubleSpinBox(self))

        # Add setup and analysis pages
        if use_tabs:
            tab = QTabWidget(self)
            tab.addTab(setup_page, "Setup")
            tab.addTab(analysis_page, "Parameters")
            self.layout().addWidget(tab)
        else:
            self.layout().addWidget(setup_page)
            self.layout().addWidget(analysis_page)

        # 3. Add run box
        run_box = QWidget(self)
        run_box.setLayout(QHBoxLayout())
        run_box.layout().addWidget(QPushButton("Save"))
        self._run_button = QPushButton("Run")
        self._run_button.clicked.connect(self.run)
        run_box.layout().addWidget(self._run_button)
        self.layout().addWidget(run_box)

    def run(self):
        print(f"Running on {self._file_select_text.text()}")

    def browse(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose a file to run on")
        if filename != "":
            self._file_select_text.setText(filename)

if __name__ == "__main__":
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(MyGroupedQWidget(), name="Example tabs", tabify=True)
    viewer.window.add_dock_widget(
        MyGroupedQWidget(use_tabs=False), name="Example boxes", tabify=True
    )
    viewer.show(block=True)
```
````

### Add tooltips to widget items

Adding tooltips to explain paramters allows users to find the information if they need it, but it won't take up unnecessary space.
TODO

### Choose the correct UI element

Not sure on this one, but e.g. a check box for 2 or 3 items, radio button for multiple options (maybe max 4) and a drop down list otherwise.

## Related workshops

- [CZI workshop](https://chanzuckerberg.github.io/napari-plugin-accel-workshops/workshops/february.html)
Related [workshop Lia slides](https://docs.google.com/presentation/d/10pxnwvBBb1rYV-LEWgmn5b2n9CK93-Qc_U_CEKUD5jI/edit#slide=id.g1197662a91c_0_66) and [isabela slides](https://docs.google.com/presentation/d/1JeDCvSYxXXDBMGdtC32rQSi5TJawiZEFW-A1wqHRHhU/edit#slide=id.g11d41ea185c_0_459). example with magicgui and QWdiget ready.

<!-- ## Plugin modifiable sections

If UI elements become modifiable by plugins (e.g. layer list or bottom bar), this could be a space to desribe the UI sectionsand what we might expect could modify each of these.

If the command palette is added the list expands etc. -->