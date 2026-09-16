"""Command-line tools for flegmmtx."""

from __future__ import annotations

import argparse
import shutil
import sysconfig
from pathlib import Path


DOC_FILENAMES = ("README.md", "USES.md", "SYNTAX.md")


def _docs_source() -> Path:
	"""Locate docs in a source checkout or a normal installation."""
	source_docs = Path(__file__).resolve().parents[2] / "docs"
	if source_docs.is_dir():
		return source_docs
	return Path(sysconfig.get_path("data")) / "flegmmtx-docs"


def copy_docs(destination: Path, force: bool = False) -> list[Path]:
	"""Copy the packaged documentation into ``destination``."""
	source = _docs_source()
	if not source.is_dir():
		raise FileNotFoundError("the installed documentation files are missing")

	destination.mkdir(parents=True, exist_ok=True)
	copied_files = []
	for filename in DOC_FILENAMES:
		source_file = source / filename
		if not source_file.is_file():
			raise FileNotFoundError(f"missing documentation file: {filename}")
		destination_file = destination / filename
		if destination_file.exists() and not force:
			raise FileExistsError(
				f"{destination_file} already exists; use --force to overwrite it"
			)
		shutil.copy2(source_file, destination_file)
		copied_files.append(destination_file)
	return copied_files


def main() -> int:
	parser = argparse.ArgumentParser(
		prog="flegmmtx",
		description="Utilities for the flegmmtx matrix library.",
	)
	parser.add_argument(
		"--docs",
		nargs="?",
		const=".",
		metavar="FOLDER",
		help="copy README.md, USES.md, and SYNTAX.md into FOLDER (default: current directory)",
	)
	parser.add_argument(
		"--version",
		action="version",
		version="flegmmtx 0.1.0",
	)
	parser.add_argument(
		"--force",
		action="store_true",
		help="overwrite documentation files that already exist",
	)
	args = parser.parse_args()

	if args.docs is None:
		parser.print_help()
		return 0

	try:
		copied_files = copy_docs(Path(args.docs).resolve(), force=args.force)
	except (FileNotFoundError, OSError) as error:
		parser.error(str(error))

	for copied_file in copied_files:
		print(f"Copied {copied_file}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
