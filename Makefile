CC ?= cc
CFLAGS ?= -std=c17 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic -Wconversion -Wshadow
BUILD := build
EXAMPLES := examples/process-id/process-id.c

.PHONY: all check clean
all: $(BUILD)/process-id
$(BUILD):
	mkdir -p $(BUILD)
$(BUILD)/process-id: $(EXAMPLES) | $(BUILD)
	$(CC) $(CFLAGS) $< -o $@
check: all
	./$(BUILD)/process-id
clean:
	rm -rf $(BUILD)
