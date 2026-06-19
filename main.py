from __future__ import annotations

import argparse
import json
import math
import shlex
from pathlib import Path


def number(value: object, field: str) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not math.isfinite(result):
        raise ValueError(f"{field} must be finite")
    return result


def validate_workflow(workflow: dict) -> None:
    if not isinstance(workflow, dict):
        raise ValueError("Workflow must be an object")
    source = workflow.get("input")
    output = workflow.get("output")
    if not isinstance(source, str) or not source.strip():
        raise ValueError("workflow requires input")
    if not isinstance(output, str) or not output.strip():
        raise ValueError("workflow requires output")
    if Path(source) == Path(output):
        raise ValueError("input and output must be different")
    nodes = workflow.get("nodes", [])
    if not isinstance(nodes, list):
        raise ValueError("nodes must be a list")
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            raise ValueError(f"node {index} must be an object")
        node_type = node.get("type")
        if node_type == "trim":
            if "start" in node and number(node["start"], "trim.start") < 0:
                raise ValueError("trim.start must be non-negative")
            if "duration" in node and number(node["duration"], "trim.duration") <= 0:
                raise ValueError("trim.duration must be positive")
        elif node_type == "scale":
            width = int(number(node.get("width", -2), "scale.width"))
            height = int(number(node.get("height", 1080), "scale.height"))
            if width == 0 or width < -2 or height == 0 or height < -2:
                raise ValueError("scale dimensions must be positive, -1, or -2")
        elif node_type == "fps":
            if number(node.get("value", 30), "fps.value") <= 0:
                raise ValueError("fps.value must be positive")
        elif node_type == "volume":
            if number(node.get("value", 1.0), "volume.value") < 0:
                raise ValueError("volume.value must be non-negative")
        elif node_type == "codec":
            continue
        else:
            raise ValueError(f"Unsupported node type: {node_type}")


def compile_workflow(workflow: dict) -> list[str]:
    validate_workflow(workflow)
    source = str(workflow["input"])
    output = str(workflow["output"])
    input_options: list[str] = []
    output_options: list[str] = []
    video_filters: list[str] = []
    audio_filters: list[str] = []

    for node in workflow.get("nodes", []):
        node_type = node["type"]
        if node_type == "trim":
            if "start" in node:
                input_options.extend(["-ss", f"{float(node['start']):g}"])
            if "duration" in node:
                input_options.extend(["-t", f"{float(node['duration']):g}"])
        elif node_type == "scale":
            video_filters.append(f"scale={int(node.get('width', -2))}:{int(node.get('height', 1080))}")
        elif node_type == "fps":
            video_filters.append(f"fps={float(node.get('value', 30)):g}")
        elif node_type == "volume":
            audio_filters.append(f"volume={float(node.get('value', 1.0)):g}")
        elif node_type == "codec":
            output_options.extend(["-c:v", node.get("video", "libx264"), "-c:a", node.get("audio", "aac")])

    command = ["ffmpeg", "-y", *input_options, "-i", source]
    if video_filters:
        command.extend(["-vf", ",".join(video_filters)])
    if audio_filters:
        command.extend(["-af", ",".join(audio_filters)])
    command.extend(output_options)
    command.append(output)
    return command


def display_command(command: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile a JSON workflow into an FFmpeg command.")
    parser.add_argument("workflow")
    parser.add_argument("--format", choices=("shell", "json"), default="shell")
    args = parser.parse_args()
    workflow = json.loads(Path(args.workflow).read_text(encoding="utf-8"))
    command = compile_workflow(workflow)
    print(json.dumps(command, ensure_ascii=False) if args.format == "json" else display_command(command))


if __name__ == "__main__":
    main()
