from pyparsing import (
    Word, delimitedList, Optional, Group, alphas, alphanums, Forward, oneOf, quotedString, infixNotation, opAssoc, CaselessKeyword, ParserElement, pyparsing_common as ppc
)

ParserElement.enablePackrat()

# SQL statement forward declaration
sqlSelectStatement = Forward()

# SQL keywords
keywords = "select from where and or limit".split()
SELECT, FROM, WHERE, AND, OR, LIMIT = map(CaselessKeyword, keywords)

# Identifiers and names
identifier = Word(alphas, alphanums + "_$").setName("identifier")
columnName = delimitedList(identifier, ".", combine=True).setName("column name")
columnName.addParseAction(ppc.upcaseTokens)
columnList = Group(delimitedList(columnName).setName("column_list"))
tableName = delimitedList(identifier, ".", combine=True).setName("table name")
tableName.addParseAction(ppc.upcaseTokens)
tableList = Group(delimitedList(tableName).setName("table_list"))

# Binary operators
binaryOperator = oneOf("= != < > >= <= eq ne lt le gt ge", caseless=True).setName("binary_operator")
realNumber = ppc.real().setName("real number")
integerNumber = ppc.signed_integer()

# Column values
columnValue = (
    realNumber | integerNumber | quotedString | columnName
).setName("column_value")
whereCondition = Group(
    (columnName + binaryOperator + columnValue)
).setName("where_condition")

# Where expression
whereExpression = infixNotation(
    whereCondition,
    [
        (AND, 2, opAssoc.LEFT),
        (OR, 2, opAssoc.LEFT),
    ],
).setName("where_expression")

# Limit clause
limitClause = Group(LIMIT + integerNumber("limit"))

# SQL Select Statement structure
sqlSelectStatement <<= (
    SELECT
    + ("*" | columnList)("columns")
    + FROM
    + tableList("tables")
    + Optional(Group(WHERE + whereExpression), "")("where")
    + Optional(limitClause)("limit")
).setName("select_statement")

# Final parser definition
simpleSQLParser = sqlSelectStatement