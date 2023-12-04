SRCS = header.cpp

OBJ = ${SRCS:.cpp=.o}

CFLAGS = -Wall -Wextra -Werror -std=c++11
CC = c++
RM = rm -f

NAME = headerchecker

all: ${NAME}

${NAME}: ${OBJ}
	${CC} ${CFLAGS} ${OBJ} -o ${NAME}

%.o: %.cpp
	${CC} ${CFLAGS} -c $< -o $@

clean:
	${RM} ${OBJ}

fclean: clean
	${RM} ${NAME}

re: fclean all

.PHONY:clean all fclean re