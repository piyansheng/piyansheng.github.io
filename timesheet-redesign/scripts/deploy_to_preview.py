# -*- coding: utf-8 -*-
"""将 timesheet-redesign 静态页推送到预览服务器。

用法：
  python scripts/deploy_to_preview.py

预览地址：
  http://preview.rigol.com/u/sn04077/timesheet-redesign/
"""
import os
import sys
from pathlib import Path

import paramiko

HOST = "preview.rigol.com"
PORT = 22
USER = "sn04077"
PASS = "846iqQVBHGiXfX"
PROJECT = "timesheet-redesign"
REMOTE_DIR = f"/srv/preview/users/{USER}/{PROJECT}"

ROOT = Path(__file__).resolve().parent.parent

# 仅上传 HTML / CSS / JS 静态资源
UPLOAD_ITEMS = [
    ROOT / "index.html",
    ROOT / "汇报-工时数据流与业务流程.html",
    ROOT / "prototypes",
]


def ensure_dir(sftp: paramiko.SFTPClient, path: str) -> None:
    parts = [p for p in path.split("/") if p]
    current = ""
    for part in parts:
        current += f"/{part}"
        try:
            sftp.stat(current)
        except FileNotFoundError:
            sftp.mkdir(current)
            print(f"  [MKDIR] {current}")


def upload_file(sftp: paramiko.SFTPClient, local_path: Path, remote_path: str) -> None:
    size = local_path.stat().st_size
    print(f"  {local_path.relative_to(ROOT)} ({size:,} bytes) -> {remote_path}")
    sftp.put(str(local_path), remote_path)


def upload_tree(sftp: paramiko.SFTPClient, local_dir: Path, remote_dir: str) -> int:
    count = 0
    for root, _, files in os.walk(local_dir):
        rel = Path(root).relative_to(local_dir)
        target = remote_dir if str(rel) == "." else f"{remote_dir}/{rel.as_posix()}"
        ensure_dir(sftp, target)
        for name in files:
            if not name.endswith((".html", ".css", ".js")):
                continue
            local_path = Path(root) / name
            remote_path = f"{target}/{name}"
            upload_file(sftp, local_path, remote_path)
            count += 1
    return count


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    missing = [p for p in UPLOAD_ITEMS if not p.exists()]
    if missing:
        print("[ERROR] 缺少文件/目录：")
        for p in missing:
            print(f"  - {p}")
        sys.exit(1)

    print(f"[CONNECT] {HOST}:{PORT} as {USER}")
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USER, password=PASS)
    sftp = paramiko.SFTPClient.from_transport(transport)

    ensure_dir(sftp, REMOTE_DIR)
    uploaded = 0

    for item in UPLOAD_ITEMS:
        if item.is_file():
            remote_path = f"{REMOTE_DIR}/{item.name}"
            upload_file(sftp, item, remote_path)
            uploaded += 1
        elif item.is_dir():
            remote_sub = f"{REMOTE_DIR}/{item.name}"
            print(f"[UPLOAD] {item.relative_to(ROOT)}/ -> {remote_sub}/")
            uploaded += upload_tree(sftp, item, remote_sub)

    sftp.close()
    transport.close()

    base = f"http://{HOST}/u/{USER}/{PROJECT}/"
    print(f"\n[OK] 已上传 {uploaded} 个文件")
    print(f"导航入口: {base}")
    print(f"流程汇报: {base}汇报-工时数据流与业务流程.html")
    print(f"UX 原型:  {base}prototypes/")


if __name__ == "__main__":
    main()
