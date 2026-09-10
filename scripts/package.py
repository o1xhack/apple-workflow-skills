"""构建仅含单入口 skill 的安装 ZIP，包括许可；不修改已安装目录。"""
import argparse
from pathlib import Path
import sys
import zipfile

from validate import SKILL, validate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    errors = validate()
    if errors:
        sys.exit("\n".join(errors))
    output = Path(args.output).resolve()
    if output.is_relative_to(SKILL.resolve()):
        sys.exit("输出不能放在安装包内部")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                info = zipfile.ZipInfo(str(path.relative_to(SKILL.parent)),
                                       date_time=(2026, 9, 10, 0, 0, 0))
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
    print(output)


if __name__ == "__main__":
    main()
