### Commit 规范

> 本节主要参考自 [`angular`](https://github.com/angular/angular/blob/main/CONTRIBUTING.md) 。
> 更宽松地要求可以参见 [How to Write a Git Commit Message](https://cbea.ms/git-commit/) ，这里给出一些最基本的要求。 感谢 @derecknowayback 的分享。

每一个 Git commit message 由 **header** 和 **body** 组成。

```
<header>
<BLANK LINE>
<body>
```

#### **header**

header 是必须的，格式如下：

```
<type>(<scope>): <short summary>
  │       │     │     │
  │       │     │     └─⫸ 原则上使用英文；使用动词原形开头，首字母不需要大写，句尾不需要句号（整句尽量不超过60词）
  │       │     │ 
  │       │     └─⫸ 冒号后面需要一个半角空格
  │       │ 
  │       └─⫸ Commit Scope: 特定范围（对于本仓库而言一般为空）
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test|style|chore|revert
```

##### Commit Type

* **build**: 影响构建系统或者外部依赖的更改，例如修改 `pom.xml`, `Dockerfile`, `docker-compose.yml` 的更改
* **ci**: 影响到 CI 配置或脚本的更改，例如修改 `gitlab-ci.yml`, Github Actions 的配置文件等
* **docs**: 只修改了文档的更改
* **feat**: 增加新功能的更改
* **fix**: 修复 bug  的更改
* **perf**: 提高了程序性能的更改
* **refactor**: 既没有修复 bug 也没有增加新功能的更改（比如重构代码）
* **test**: 增加或改正测试代码
* **style**: 不改变代码含义的修改（比如格式化代码）
* **chore**: 其他不改变 `src` 或测试代码的修改
* **revert**: 撤回之前的 `commit`

#### scope

commit 所属的范围，例如 `frontend`、`backend` 等。

如果 commit 不属于特定范围，则不用加 scope 。
#### body

body 是可选的，与 header 一样，需要使用动词原形。body 中可以书写比 header 中更详细的信息，比如：

- 为什么做了这个更改
- 受到了什么启发
- 与之前版本的区别
- 功能的详细说明
- ……

#### 样例

```
fix: address an issue where return value can be null

if an incorrect request body is sent to the server, method xxx may respond with a empty body due to xxx
this issue is fixed by improving error handling in the request parser
```