CC ?= cc
CFLAGS ?= -std=c17 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic -Wconversion -Wshadow
BUILD := build
EXAMPLES := examples/getpid/getpid.c

.PHONY: all check validate clean
all: $(BUILD)/getpid
$(BUILD):
	mkdir -p $(BUILD)
$(BUILD)/getpid: $(EXAMPLES) | $(BUILD)
	$(CC) $(CFLAGS) $< -o $@
check: all validate
	./$(BUILD)/getpid
clean:
	rm -rf $(BUILD)

validate:
	python3 tools/validate.py
