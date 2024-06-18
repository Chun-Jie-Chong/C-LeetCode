# Define the compiler
CC = gcc

# Define the compiler flags
CFLAGS = -Wall

# Define the source files
SOURCES = $(wildcard *.c)

# Define the object files
OBJECTS = $(SOURCES:.c=.o)

# Define the executable name
EXEC = my_program

# The target to build the executable
$(EXEC): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

# Rule to build object files
%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

# Clean up build files
clean:
	rm -f $(EXEC) $(OBJECTS)
