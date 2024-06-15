# SeatApplication

#### 介绍

模块化设计的自动排座位，支持自定义规则和特效（暂时只制作了cli）

#### 画饼区
1. [x] 内核部分制作
2. [x] CLI部分制作
3. [x] GUI部分制作完善（制作中）
4. [ ] 动态概率以及历史存储访问

#### 编译安装教程

1.  安装virtualenv

```bash
python -m pip install virtualenv
```

2.  安装环境

```bash
python -m pip install requirements.txt -r
```

3.  开始使用！

#### 使用说明

1.  下载发布版后先解压！
2.  相关的配置文件在./assets/settings
3.  ./assets/settings/name.txt 存储所有名称
4.  ./assets/settings/rules.txt 存储所有用户自定义规则（格式见样例）
5.  ./assets/settings/table.txt 存储大组数（GroupNum），每组的列数（暂时只支持2），依次每组的行数（ColumnOfGroup），具体见样例
6.  ./assets/history/ 存储输出
7.  ./assets/audio/ 存储用到的多媒体

#### 参与贡献

1.  Fork 本仓库（或者下载）
2.  新建 Feat_xxx 分支，如果为修复，新建Fix_xxx
3.  提交代码
4.  新建 Pull Request合并到dev！
5.  等待代码合并

