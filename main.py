from __future__ import annotations

import argparse
import json
import shlex
from pathlib import Path


def compile_workflow(workflow: dict) -> list[str]:
    source = workflow.get("input")
    output = workflow.get("output")
    if not source or not output:
        raise ValueError("workflow requires input and output")

    command = ["ffmpeg", "-y", "-i", str(source)]
    video_filters: list[str] = []
    audio_filter: str | None = None

    for node in workflow.get("nodes", []):
        node_type = node.get("type")
        if node_type == "trim":
            if "start" in node:
                command[1:1] = ["-ss", str(node["start"])]
            if "duration" in node:
                command[1:1] = ["-t", str(node["duration"])]
        elif node_type == "scale":
            width = int(node.get("width", -2))
            height = int(node.get("height", 1080))
            video_filters.append(f"scale={width}:{height}")
        elif node_type == "fps":
            video_filters.append(f"fps={float(node.get('value', 30)):g}")
        elif node_type == "volume":
            audio_filter = f"volume={float(node.get('value', 1.0)):g}"
        elif node_type == "codec":
            command.extend(["-c:v", node.get("video", "libx264"), "-c:a", node.get("audio", "aac")])
        else:
            raise ValueError(f"Unsupported node type: {node_type}")

    if video_filters:
        command.extend(["-vf", ",".join(video_filters)])
    if audio_filter:
        command.extend(["-af", audio_filter])
    command.append(str(output))
    return command


def display_command(command: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile a JSON workflow into an FFmpeg command.")
    parser.add_argument("workflow")
    args = parser.parse_args()
    workflow = json.loads(Path(args.workflow).read_text(encoding="utf-8"))
    print(display_command(compile_workflow(workflow)))


if __name__ == "__main__":
    main()
