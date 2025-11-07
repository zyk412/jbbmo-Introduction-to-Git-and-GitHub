#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

/* 自动机构成：有限状态集合、有限输入字母表、
   状态转换函数、唯一初始状态、可接受状态集合 
   自动机分类：确定型DFA、非确定型NFA */ 

// 种别码 (用来标识一个单词属于哪种语法范畴
#define KEYWORD 1
#define ID 2     // 字母开头，可包含数字
#define NUM 3    // 数字开头
#define OPERATOR 4
#define DELIMITER 5
#define END 0

// 关键字表
char* keywords[] = {
	"main", "if", "then", "else", "while", "do",
	"repeat", "until", "for", "from", "to", "step",
	"switch", "of", "case", "default", "return",
	"integer", "real", "char", "bool", "and", "or", "not", 
	"mod", "read", "write",
};

// 运算符表
char operator[] = "+-*/<>=!";

// 分隔符表
char delimiter[] = ",;:{}[]()";

// 自动机状态
typedef enum {
	START,
	IN_ID,
	IN_NUM,
	IN_OPERATOR,
	IN_DELIMITER,
	DONE
} State;

/* 判断 */

int is_keywords(char *str) {
	int count = sizeof(keywords) / sizeof(keywords[0]);

	for (int i = 0; i < count; i++) {
		if (strcmp(str, keywords[i]) == 0) {
			return 1;
		}
	}

	return 0;
}

int is_operator(char ch) {
	return strchr(ch, operator) != NULL;
}

int is_delimiter(char ch) {
	return strchr(ch, delimiter) != NULL;
}

// 获取 token 类型名称 
char* get_token_type(int type) {
	switch (type){
		case KEYWORD:return "KEYWORD";
		case ID:return "ID";
		case NUM:return "NUM";
		case OPERATOR:return "OPERATOR";
		case DELIMITER:return "DELIMITER";
		case END:return "END";
		default:return "UNKNOWN";
	}
}

// 词法分析
void analyzer(FILE *file) {
	State state = START;

	char ch;              // 当前的字符
	char token[100];      // 保存符合条件的当前字符的下一个字符
	int index = 0;        // char token[] 对应的索引
	int line = 1;

	printf("类型，对应值\n");

	while ((ch = fgetc(file))!= EOF) {
		switch (state) {
			/* 初始状态下判断其下一状态 */
			case START:
				if (ch == '\n') {
					line++;     // 忽略空白字符
				}
				continue;

				index = 0;

				if (isalpha(ch)) {
					state = IN_ID;
					token[index++] = ch;
				}
				else if (isdigit(ch)) {
					state = IN_NUM;
					token[index++] = ch;
				}
				else if (is_operator(ch)) {
					state = IN_OPERATOR;
					token[index++] = ch;
				}
				else if (is_delimiter(ch)) {
					state = IN_DELIMITER;
					token[index++] = ch;
				}
				break;
			
			/* 在当前字符为ID的状态下 */
			case IN_ID:
				if (isalnum(ch)) {
					token[index++] = ch;
				}
				else {
					token[index] = '\0';   

					fseek(file, -1, SEEK_CUR);   // 文件指针从当前位置向前移动1个字节

					if (is_keywords(token)) {
						printf("%s, %s", "KEYWORD", token);
					}
					else {
						printf("%s, %s", "ID", token);
					}

					state = START;
				}
				break;

			case IN_NUM:
				if (isdidit(ch)) {
					token[index++] = ch;
				}
				else {
					token[index] = '\0';
					fseek(file, -1, SEEK_CUR);

					printf("%s, %s", "NUM", token);

					state = START;
				}
				break;

			case IN_OPERATOR:
				token[index] = '\0';

				// 双字符运算符
				if ((ch == '=') &&
					(token[0] == '<' || token[0] == '>' || token[0] == '!')) {
					token[index++] = ch;
					token[index] = '\0';
				}
				else {
					fseek(file, -1, SEEK_CUR);
				}

				printf("%s, %s", "OPERATOR", token);

				state = START;
				break;

			case IN_DELIMITER:
				token[index] = '\0';
				fseek(file, -1, SEEK_CUR);
				printf("%s, %s", "DELIMITER", token);

				state = START;
				break;

			default:break;
		}
	}

	// 处理最后一个token
	if (state != START) {
		token[index] = '\0';

		switch (state) {
			case IN_ID:
				if (is_keywords(token)) {
					printf("%s, %s", "KEYWORD", token);
				}
				else {
					printf("%s, %s", "ID", token);
				}
				break;

			case IN_NUM:
				printf("%s, %s", "NUM", token);
				break;

			default:break;
		}
	}

	printf("%s", "END");
}

// 主函数
int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf("Please enter one file name in command line.");

		return 1;
	}

	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		printf("Invalid file.");

		return 1;
	}

	analyzer(file);

	fclose(file);

	return 0;
}