# RxWidgets

UI interface library redefined based on Qt5, for ICTFE/ISAE used only.

本项目将会作为ICTFE v2.0 / ISAE 的界面库, 致力于提供简洁现代化的Qt界面样式.

## RxAnimatedWidget

提供动画展开和收起窗口.

默认动画时间为`700ms`

使用时只需要传入是否为水平展开, 折叠时的长度, 展开时的长度即可.

需要展开或者折叠`widget`时, 只需要调用`widget->doFold()`.

`doFold()`函数同时是一个槽. 你可以将按钮点击事件连接到这个槽上.
