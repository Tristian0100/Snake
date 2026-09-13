#!/system/bin/sh
# AI Review Phone Control payload v1
# No recorder change in v1: preserve the currently running phone-local backup recorder.
CONTROL_DIR="/sdcard/Movies/AIReviewPhone/control"
LOG="/sdcard/Movies/AIReviewPhone/recorder.log"
mkdir -p "$CONTROL_DIR"
printf '%s | GitHub control payload v1 applied; existing recorder preserved.\n' "$(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG"
exit 0
