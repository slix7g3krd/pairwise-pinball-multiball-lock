# pairwise-pinball-multiball-lock

## 领域

游戏、图形与多媒体

## 主题

弹珠台多球与锁定

## 说明

球池独立句柄、边沿触发与碰撞去重。

初始状态下 `gameplay/pinball_multiball.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
