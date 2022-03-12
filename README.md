# stormworks-translate-chn

**翻译维护较为随缘，欢迎提交pr**

Stormworks: Build and Rescue中文汉化项目  
创意工坊地址: [简体中文翻译 Simplified Chinese](https://steamcommunity.com/sharedfiles/filedetails/?id=2019972792)  
欢迎PR，会定期审核并推到创意工坊  
自建交流QQ群：665246787

## 手动更新

订阅创意工坊  
下载`SimplifiedChinese.tsv`文件，替换掉路径  
`steam安装目录\steamapps\workshop\content\573090\2019972792`下的`language.tsv`即可

## 翻译文件

 `SimplifiedChinese.tsv` 即为翻译文件，其中结构样例如下

|id |description|en|local|
:-:|:-:|:-:|:-:
|def_giga_prop_node_0_label| |Power|动力|

其中`id`与`description`字段不用管，也有很大概率为空，只需要将`en`翻译到`local`就可以了

> 注意一定以`utf-8`编码保存

官方给的翻译API非常非常屎，包括现在文件里也有些结构上出错的地方，欢迎纠正！

## 辅助脚本

原生`python 3`  
同目录下执行即可查看缺翻项与缺翻个数  
~~本来有个机翻脚本被我给整丢了也懒得再写了,shit~~
