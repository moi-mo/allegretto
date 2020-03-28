# allegretto

可以用来记录本地下载的番剧追番进度，这样就不用打开浏览器去Bangumi站记录了（

当然如果没多少番剧的话其实没必要用~~因为这玩意儿是写着练的~~

目前的版本号是14<sub>~~（当然不是开发了14版）~~</sub>，后续应该会按照太鼓达人框体的版本号更新一些feature~~就是无聊而已~~

初步确定一个番剧class会有三个类变量：`name`、`episode`、`time`。均为str。

## 命令

#### `new`:新建一部未看过的番剧。格式有两种。

> new [name]

or

> new [name] [episode] [time]

其中前者会默认设置episode与time为`'null'`



#### `mark`:标记已新建的番剧某一个变量为新值。

> mark [name] [change_type] [new_val]



#### `allegretto`:同时更改一部番剧的episode与time。

**（其中allegretto可以缩写为al）**

> al [name] [eprisode] [time]



#### `check`:查看已有的番剧信息。

> check [name]


#### `check-all`:查看已有的全部番剧信息。

> check-all



#### ```delete```:删除已有的番剧条目。

> delete [name]



#### `version`:查看Bangumi Recorder的版本。

> version



#### `exit`:退出。

> exit

--------------------------------



## （计划了）还未实现的功能：

- 界面提示语自定义
- 一次性添加多部番剧
- 给class Bangumi添加一个类变量列表作为tag
- 标记是否看完
- 把~~没有灵魂的·~~“Hi~”改为早上/下午/晚上按时间问候。






--------------------------------------------------------------------

有好的feature欢迎在issue提出w



