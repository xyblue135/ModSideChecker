`以前玩mc的时候都是手动去过滤，相当麻烦，其实.jar是能解压打开的，观看META-INF里面的toml文件可以知道信息`

# 什么是 TOML？什么是json？
- **TOML** 是一种配置文件格式，全称是 "**Tom's Obvious, Minimal Language**"。
- 设计目标是简洁、易读且易于解析，常用来写程序配置文件。
- 格式类似 INI，但更严格、支持嵌套表格和数组，结构清晰。
-**JSON**（JavaScript Object Notation）是一种轻量级的数据交换格式。它基于JavaScript编程语言的一个子集，易于人类阅读和编写，同时也易于机器解析和生成。

# Forge
相关特征代码为META-INF/mods.toml
side = "BOTH"
side="CLIENT"s
## 参考示例1
```
modLoader = "javafml"
loaderVersion = "[35,)"
issueTrackerURL = "https://github.com/tasgon/observable/issues"
license = "MPL"

[[mods]]
modId = "observable"
version = "4.4.2"
displayName = "Observable"
authors = "tasgon"
displayURL = "https://github.com/tasgon/observable"
description = '''
See what's lagging your world.
'''
#logoFile = ""

[[dependencies.observable]]
modId = "forge"
mandatory = true
versionRange = "[40,)"
ordering = "NONE"
side = "BOTH"

[[dependencies.observable]]
modId = "minecraft"
mandatory = true
versionRange = "[1.18.2,)"
ordering = "NONE"
side = "BOTH"

[[dependencies.observable]]
modId = "architectury"
mandatory = true
versionRange = "[3.1.45,)"
ordering = "AFTER"
side = "BOTH"

# [[dependencies.observable]]
# modId = "kotlinforforge"
# mandatory = true
# versionRange = "[1.11.0,)"
# ordering = "AFTER"
# side = "BOTH"

```
# Neoforge
相关特征代码为META-INF/neoforge.mods.toml
side = "BOTH"
side="CLIENT"s
## 参考示例1
```
modLoader="javafml"
loaderVersion="[2,)"
issueTrackerURL="https://github.com/squeek502/AppleSkin"
license="The Unlicense"

[[mods]]
modId="appleskin"
version="${file.jarVersion}"
displayName="AppleSkin"
#updateJSONURL=""
displayURL="https://github.com/squeek502/AppleSkin"
logoFile="appleskin.png"
authors="squeek"
description="Adds various food-related HUD improvements"

[[dependencies.appleskin]]
    modId="neoforge"
    type="required"
    versionRange="[21.0.0-beta,)"
    ordering="NONE"
    side="CLIENT"s
```
## 参考示例2
```
modLoader = "javafml"
loaderVersion = "[3,)"
issueTrackerURL = "https://github.com/Nanite/AcceleratedDecay/issues"
license = "GPL3"

[[mods]]
modId = "accelerateddecay"
version = "21.0.0"
displayName = "Accelerated Decay"
authors = "ErrorMikey"
description = '''
Speeds up the decay of leaves
'''
#logoFile = ""

[[dependencies.accelerateddecay]]
modId = "neoforge"
required = true
versionRange = "[21.0,)"
ordering = "NONE"
side = "BOTH"

[[dependencies.accelerateddecay]]
modId = "minecraft"
required = true
versionRange = "[1.21,)"
ordering = "NONE"
side = "BOTH"

[[dependencies.accelerateddecay]]
modId = "architectury"
required = true
versionRange = "[13.0.0,)"
ordering = "AFTER"
side = "BOTH"

[[mixins]]
config = "accelerateddecay-common.mixins.json"

[[mixins]]
config = "accelerateddecay.mixins.json"

```
# Fabric
相关特征代码为fabric.mod.json
"client" → 仅客户端（如 UI 优化、光影、按键绑定等）
"server" → 仅服务端（如服务端管理插件）
```
"environment": "client"
"environment": "server"
"environment": "*"
```
`*`（或未指定） → 客户端和服务端都需要（如大多数内容模组）
## 参考示例
```
{
  "schemaVersion": 1,
  "id": "chunky",
  "version": "1.4.36",
  "name": "Chunky",
  "description": "Pre-generates chunks, quickly, efficiently, and safely",
  "authors": [
    "pop4959"
  ],
  "contact": {
    "website": "https://www.curseforge.com/minecraft/mc-mods/chunky-pregenerator",
    "homepage": "https://www.curseforge.com/minecraft/mc-mods/chunky-pregenerator",
    "repo": "https://github.com/pop4959/Chunky",
    "sources": "https://github.com/pop4959/Chunky",
    "issues": "https://github.com/pop4959/Chunky/issues"
  },
  "license": "GPLv3",
  "icon": "assets/chunky/icon.png",
  "environment": "*",
  "entrypoints": {
    "main": [
      "org.popcraft.chunky.ChunkyFabric"
    ]
  },
  "mixins": [
    "chunky.mixins.json"
  ],
  "depends": {
    "fabricloader": ">=0.16.10",
    "fabric": "*",
    "minecraft": ">=1.21.5",
    "java": ">=21"
  },
  "custom": {
    "modmenu": {
      "links": {
        "modmenu.discord": "https://discord.gg/ZwVJukcNQG"
      }
    }
  }
}

```

