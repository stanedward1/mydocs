<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [vagrant box基本命令](#vagrant-box%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4)
  - [列出本地环境中所有的box](#%E5%88%97%E5%87%BA%E6%9C%AC%E5%9C%B0%E7%8E%AF%E5%A2%83%E4%B8%AD%E6%89%80%E6%9C%89%E7%9A%84box)
  - [添加box到本地vagrant环境](#%E6%B7%BB%E5%8A%A0box%E5%88%B0%E6%9C%AC%E5%9C%B0vagrant%E7%8E%AF%E5%A2%83)
  - [更新本地环境中指定的box](#%E6%9B%B4%E6%96%B0%E6%9C%AC%E5%9C%B0%E7%8E%AF%E5%A2%83%E4%B8%AD%E6%8C%87%E5%AE%9A%E7%9A%84box)
  - [删除本地环境中指定的box](#%E5%88%A0%E9%99%A4%E6%9C%AC%E5%9C%B0%E7%8E%AF%E5%A2%83%E4%B8%AD%E6%8C%87%E5%AE%9A%E7%9A%84box)
  - [重新打包本地环境中指定的box](#%E9%87%8D%E6%96%B0%E6%89%93%E5%8C%85%E6%9C%AC%E5%9C%B0%E7%8E%AF%E5%A2%83%E4%B8%AD%E6%8C%87%E5%AE%9A%E7%9A%84box)
  - [在线查找需要的box](#%E5%9C%A8%E7%BA%BF%E6%9F%A5%E6%89%BE%E9%9C%80%E8%A6%81%E7%9A%84box)
- [vagrant基本命令](#vagrant%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4)
  - [在空文件夹初始化虚拟机](#%E5%9C%A8%E7%A9%BA%E6%96%87%E4%BB%B6%E5%A4%B9%E5%88%9D%E5%A7%8B%E5%8C%96%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [在初始化完的文件夹内启动虚拟机](#%E5%9C%A8%E5%88%9D%E5%A7%8B%E5%8C%96%E5%AE%8C%E7%9A%84%E6%96%87%E4%BB%B6%E5%A4%B9%E5%86%85%E5%90%AF%E5%8A%A8%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [ssh登录启动的虚拟机](#ssh%E7%99%BB%E5%BD%95%E5%90%AF%E5%8A%A8%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [挂起启动的虚拟机](#%E6%8C%82%E8%B5%B7%E5%90%AF%E5%8A%A8%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [重启虚拟机](#%E9%87%8D%E5%90%AF%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [关闭虚拟机](#%E5%85%B3%E9%97%AD%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [查找虚拟机的运行状态](#%E6%9F%A5%E6%89%BE%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%9A%84%E8%BF%90%E8%A1%8C%E7%8A%B6%E6%80%81)
  - [销毁当前虚拟机](#%E9%94%80%E6%AF%81%E5%BD%93%E5%89%8D%E8%99%9A%E6%8B%9F%E6%9C%BA)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# vagrant box基本命令

## 列出本地环境中所有的box

```shell
vagrant box list
```

## 添加box到本地vagrant环境

```shell
vagrant box add box-name(box-url)
```

## 更新本地环境中指定的box

```shell
vagrant box update box-name
```

## 删除本地环境中指定的box

```shell
vagrant box remove box-name
```

## 重新打包本地环境中指定的box

```shell
vagrant box repackage box-name
```

## 在线查找需要的box

官方网址：https://app.vagrantup.com/boxes/search

# vagrant基本命令

## 在空文件夹初始化虚拟机

```shell
vagrant init [box-name]
```

## 在初始化完的文件夹内启动虚拟机

```shell
vagrant up
```

## ssh登录启动的虚拟机

```shell
vagrant ssh
```

## 挂起启动的虚拟机

```shell
vagrant suspend
```

## 重启虚拟机

```shell
vagrant reload
```

## 关闭虚拟机

```shell
vagrant halt
```

## 查找虚拟机的运行状态

```shell
vagrant status
```

## 销毁当前虚拟机

```shell
vagrant destroy
```

[官方文档](https://www.vagrantup.com/docs)