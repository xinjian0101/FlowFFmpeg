# FlowFFmpeg

把声明式 JSON 媒体工作流编译为可检查、可执行的 FFmpeg 命令。

## MVP

- 裁剪、缩放、帧率、音量、字幕、编码节点
- 默认只显示命令，不直接执行
- 使用 `--run` 才调用本机 FFmpeg
- 对未知节点立即报错

## 运行

```bash
python main.py examples/workflow.json
python main.py examples/workflow.json --run
```

## 测试

```bash
python -m unittest -v
```

## License

MIT
