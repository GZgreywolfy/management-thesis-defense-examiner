#!/usr/bin/env python3
"""
replace_authors.py — 批量替换 Markdown 文件中的占位作者名

功能：
  1. --check        扫描并列出所有 Markdown 文件中的占位作者名
  2. --replace NAME 将所有占位作者名替换为指定的真实姓名
  3. --file PATH    指定要处理的单个文件路径（默认扫描整个项目目录）
  4. --output-dir   将替换后的文件输出到指定目录（不修改原文件）

示例：
  python replace_authors.py --check
  python replace_authors.py --replace "张明"
  python replace_authors.py --replace "李四" --file examples/sample-dialogue.md
  python replace_authors.py --replace "王五" --output-dir ./output
"""

import argparse
import glob
import os
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# 占位作者名列表
# ---------------------------------------------------------------------------
PLACEHOLDER_NAMES = [
    "张三", "李四", "王五", "赵六",
    "刘七", "陈八", "周九", "吴十",
    "郑十一", "冯十二",
]

# 已知的误匹配场景：占位名出现在更长词语中（如 "张三丰"）
# 这些场景中的占位名不应被替换
_KNOWN_COMPOUNDS = {
    "张三": ["张三丰"],       # 历史人物
    "李四": ["李四光"],       # 地质学家
}


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------
def _find_md_files(root_dir: str, single_file: str | None = None) -> list[Path]:
    """递归获取所有 .md 文件，或返回单个文件路径。"""
    if single_file:
        path = Path(single_file)
        if not path.exists():
            print(f"错误：文件不存在 — {single_file}", file=sys.stderr)
            sys.exit(1)
        return [path]

    root = Path(root_dir)
    if not root.is_dir():
        print(f"错误：目录不存在 — {root_dir}", file=sys.stderr)
        sys.exit(1)

    return sorted(Path(p) for p in glob.glob(str(root / "**/*.md"), recursive=True))


def _read_file(path: Path) -> str:
    """以 UTF-8 读取文件内容。"""
    return path.read_text(encoding="utf-8")


def _write_file(path: Path, content: str) -> None:
    """以 UTF-8 写入文件内容。"""
    path.write_text(content, encoding="utf-8")


def _find_valid_positions(content: str, name: str) -> list[tuple[int, int]]:
    """查找 `name` 在 `content` 中所有有效出现位置（排除已知复合词场景）。"""
    compounds = _KNOWN_COMPOUNDS.get(name, [])
    positions = []
    start = 0
    while True:
        pos = content.find(name, start)
        if pos == -1:
            break
        end = pos + len(name)
        # 检查是否属于某个已知复合词
        is_compound = False
        for compound in compounds:
            if content[pos:pos + len(compound)] == compound:
                is_compound = True
                break
        if not is_compound:
            positions.append((pos, end))
        start = pos + 1  # 从下一个字符继续搜索
    return positions


def _scan_placeholders(content: str) -> dict[str, int]:
    """扫描内容中出现的占位作者名，返回 {name: count}。"""
    result: dict[str, int] = {}
    for name in PLACEHOLDER_NAMES:
        count = len(_find_valid_positions(content, name))
        if count > 0:
            result[name] = count
    return result


def _replace_placeholders(content: str, target_name: str) -> str:
    """将内容中所有占位作者名替换为目标姓名。"""
    # 按名称长度降序处理，避免短名覆盖长名（例如先处理 "郑十一" 再处理 "吴十"）
    for name in sorted(PLACEHOLDER_NAMES, key=len, reverse=True):
        positions = _find_valid_positions(content, name)
        if not positions:
            continue
        # 从后往前替换，避免位置偏移
        result = list(content)
        for pos, end in reversed(positions):
            result[pos:end] = target_name
        content = "".join(result)
    return content


# ---------------------------------------------------------------------------
# 命令处理器
# ---------------------------------------------------------------------------
def cmd_check(args: argparse.Namespace) -> None:
    """--check：扫描并报告占位作者名出现情况。"""
    files = _find_md_files(args.project_root, args.file)
    total_placeholders = 0
    found_any = False

    for filepath in files:
        content = _read_file(filepath)
        matches = _scan_placeholders(content)
        if not matches:
            continue

        found_any = True
        rel_path = filepath.relative_to(args.project_root) if filepath.is_relative_to(args.project_root) else filepath
        placeholder_list = ", ".join(f"{name}×{cnt}" for name, cnt in sorted(matches.items()))
        file_count = sum(matches.values())
        total_placeholders += file_count
        print(f"  {rel_path}  —  {file_count} 处: {placeholder_list}")

    if not found_any:
        print("未发现任何占位作者名。")
    else:
        print(f"\n总计发现 {total_placeholders} 处占位作者名。")


def cmd_replace(args: argparse.Namespace) -> None:
    """--replace：替换占位作者名。"""
    files = _find_md_files(args.project_root, args.file)
    output_dir = Path(args.output_dir) if args.output_dir else None

    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    total_replaced = 0
    total_files = 0

    for filepath in files:
        content = _read_file(filepath)
        matches = _scan_placeholders(content)
        if not matches:
            continue

        new_content = _replace_placeholders(content, args.replace)
        file_count = sum(matches.values())
        total_replaced += file_count
        total_files += 1

        if output_dir:
            # 保持相对目录结构
            try:
                rel_path = filepath.relative_to(args.project_root)
            except ValueError:
                rel_path = filepath.name
            out_path = output_dir / rel_path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            _write_file(out_path, new_content)
            print(f"  已写入: {out_path}  ({file_count} 处替换)")
        else:
            _write_file(filepath, new_content)
            print(f"  已修改: {filepath}  ({file_count} 处替换)")

    if total_files == 0:
        print("未发现需要替换的占位作者名。")
    else:
        print(f"\n完成！共处理 {total_files} 个文件，替换 {total_replaced} 处占位作者名。")


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="批量替换 Markdown 文件中的占位作者名（张三、李四等）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "示例:\n"
            "  %(prog)s --check\n"
            "  %(prog)s --replace \"张明\"\n"
            "  %(prog)s --replace \"李四\" --file examples/sample-dialogue.md\n"
            "  %(prog)s --replace \"王五\" --output-dir ./output\n"
        ),
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="扫描并列出所有 Markdown 文件中的占位作者名",
    )
    parser.add_argument(
        "--replace",
        metavar="NAME",
        default=None,
        help="将所有占位作者名替换为指定的真实姓名",
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        default=None,
        help="指定要处理的单个文件路径（默认扫描整个项目目录）",
    )
    parser.add_argument(
        "--output-dir",
        metavar="PATH",
        default=None,
        help="将替换后的文件输出到指定目录（不修改原文件）",
    )
    parser.add_argument(
        "--project-root",
        metavar="PATH",
        default=None,
        help="项目根目录（默认自动检测为脚本所在目录的父目录）",
    )

    args = parser.parse_args()

    # 自动检测项目根目录：脚本所在目录即项目根目录
    if args.project_root is None:
        args.project_root = os.path.dirname(os.path.abspath(__file__))

    # 校验参数
    if not args.check and args.replace is None:
        parser.print_help()
        print("\n错误：请使用 --check 或 --replace 参数。", file=sys.stderr)
        sys.exit(1)

    if args.check:
        cmd_check(args)
    else:
        cmd_replace(args)


if __name__ == "__main__":
    main()