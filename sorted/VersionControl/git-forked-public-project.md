# Contribute to Public Project

1. 克隆远程仓库

> 添加或修改代码

```
git clone <public-project-url>
...work
git commit
...work
git commit
```

2. 添加新的远程仓库作为本地仓库的远端

```
git remote add myfork <your-remote-url> 
```
推送内容到新远端

```shell
git push -u myfork featureA
```

3. 告诉维护人员你所做工作想要维护人员merge

```
git request-pull origin/master myfork
```
