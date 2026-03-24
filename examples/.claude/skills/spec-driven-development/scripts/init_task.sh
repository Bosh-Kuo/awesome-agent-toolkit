#!/bin/bash

# Check if a task title was provided
if [ -z "$1" ]; then
  echo "Error: Task title is required."
  echo "Usage: $0 <task_title>"
  exit 1
fi

TASK_TITLE="$1"
BASE_DIR=".spec-driven-development-tasks"

# 1. Create the base directory
if [ ! -d "$BASE_DIR" ]; then
  mkdir -p "$BASE_DIR"
  echo "Created base directory: $BASE_DIR"
fi

# 2. Update .gitignore if needed
GITIGNORE_FILE=".gitignore"
if [ -f "$GITIGNORE_FILE" ]; then
  if ! grep -q "$BASE_DIR" "$GITIGNORE_FILE"; then
    echo "" >> "$GITIGNORE_FILE"
    echo "# Spec Driven Development Tasks" >> "$GITIGNORE_FILE"
    echo "$BASE_DIR/" >> "$GITIGNORE_FILE"
    echo "Added $BASE_DIR to $GITIGNORE_FILE"
  else
    echo "$BASE_DIR is already in $GITIGNORE_FILE"
  fi
else
  # If .gitignore doesn't exist, create it
  echo "# Spec Driven Development Tasks" > "$GITIGNORE_FILE"
  echo "$BASE_DIR/" >> "$GITIGNORE_FILE"
  echo "Created $GITIGNORE_FILE and added $BASE_DIR"
fi

# 3. Create the task directory
DATE_STR=$(date +%Y%m%d)
TASK_DIR_NAME="${DATE_STR}-${TASK_TITLE}"
TASK_DIR_PATH="$BASE_DIR/$TASK_DIR_NAME"

if [ -d "$TASK_DIR_PATH" ]; then
  echo "Warning: Directory $TASK_DIR_PATH already exists."
else
  mkdir -p "$TASK_DIR_PATH"
  echo "Created task directory: $TASK_DIR_PATH"
fi

# 4. Create the empty files
touch "$TASK_DIR_PATH/spec.md"
touch "$TASK_DIR_PATH/implementation.md"
touch "$TASK_DIR_PATH/task.md"
touch "$TASK_DIR_PATH/walk-through.md"

echo "Created empty files: spec.md, implementation.md, task.md, walk-through.md in $TASK_DIR_PATH"
echo "Initialization complete."
