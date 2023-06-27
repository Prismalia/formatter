#!/usr/bin/env bash

test_formatter() {
  PAIR_DIR="$(pwd)/pairs"
  echo "PAIR_DIR: $PAIR_DIR"

  to_format="$PAIR_DIR/1_file.py"
  expected="$PAIR_DIR/1_expected.py"

  echo "to_format: $to_format"
  pformat $to_format

  assert "$(diff -q $to_format $expected)" \
    "Formatted output matches the expected format"
}