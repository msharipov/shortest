SRC_DIR := src
BIN_DIR := bin

CFLAGS := -Wall -Wpedantic -Werror
CPPFLAGS := -Isrc

$(BIN_DIR):
	mkdir -p $@

co_search: $(SRC_DIR)/co_search.cpp | $(BIN_DIR)
	g++ $(CPPFLAGS) $(CFLAGS) -O2 -o $(BIN_DIR)/$@ $<
