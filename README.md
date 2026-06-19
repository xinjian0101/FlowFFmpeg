# FlowFFmpeg

把声明式 JSON 媒体工作流编译为可检查的 FFmpeg 命令。

## MVP

- 支持裁剪、缩放、帧率、音量和编码节点
- 只生成命令，不自动执行外部程序
- 所有参数以数组形式构建，便于检查和二次集成
- 对未知节点立即报错

## 运行

```bash
python main.py examples/workflow.json
```

程序会输出完整命令。确认输入、输出和滤镜参数后，再由用户自行执行。

## 测试

```bash
python tests.py
```

## License

MIT
