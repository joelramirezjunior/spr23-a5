CC=gcc  # compiler to use
CFLAGS=-g -Wall # compiler flags

TARGET=calculator # the build target executable

OBJS = main.o addition.o subtraction.o multiplication.o division.o

%.o: %.c operations.h
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS)

clean:
	$(RM) $(TARGET) $(OBJS)
