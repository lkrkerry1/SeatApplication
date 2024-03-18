from typing import *
from utils import constants

WHITELIST = 0
BLACKLIST = 1

class SeatingTable(): # Todo: finish document
    def __init__(self,
                table_path=constants.TABLE_FILE,
                name_path=constants.NAME_FILE,
                rule_path=constants.RULES_FILE,
                output_path=constants.OUTPUT_DIR):
        self.table_path = table_path
        self.name_path = name_path
        self.rule_path = rule_path
        self.output_path = output_path
        self.table = []
        self.names = []
        self.rules = ({},{})
        self.status = {}
        self.read_table()
        self.read_names()
        self.read_rules()

    def read_table(self) -> None:
        """Reads the table given
        """
        table = self.table
        table_num = {}
        with open(self.table_path) as f:
            for line in f.read().splitlines():
                key, value = line.split('=', 1)
                if key == "ColumnOfGroup":
                    table_num["ColumnOfGroup"] = [int(i) for i in value.split(",")]
                    continue
                table_num[key] = int(value)
        for i in range(table_num["GroupNum"]):
            table.append([])
            for j in range(table_num["ColumnOfGroup"][i]):
                table[i].append([])
                for _ in range(table_num["LineOfGroup"]):
                    table[i][j].append("")
        self.table = table

    def read_names(self) -> None:
        """Reads the names of the specified properties
        """
        with open(self.name_path) as f:
            self.names = f.read().splitlines()
        for i in self.names:
            self.status[i] = False

    def read_rules(self) -> None:
        """Reads the rules of the specified properties
        """
        rules = self.rules
        names = self.names
        with open(self.rule_path) as f:
            for line in f.read().splitlines():
                if "[WhiteList]" in line:
                    idx = 0
                    continue
                if "[BlackList]" in line:
                    idx = 1
                    continue
                key, value = line.split(':')
                if idx == WHITELIST and key in rules[idx]:
                    raise ValueError("Invalid whitesList rule with key '%s' and value '%s'"% key %value)
                if idx == BLACKLIST and key in rules[idx] and rules[idx][key] == value:
                    raise ValueError("Invalid blackList rule being multiple: key '%s' and value '%s'"% key %value)
                if key not in names:
                    raise ValueError("Invalid rule with '%s' which is not in names"%key)
                if value not in names:
                    raise ValueError("Invalid rule with '%s' which is not in names"%value)
                rules[idx][key] = value
        self.rules = rules

    def __str__(self) -> str:
        """Output the table
        """
        table = self.table
        output = ""
        for i in range(len(table)):
            for j in range(len(table[i])):
                for k in range(len(table[i][j])):
                    output += (table[i][j][k] + " ")
                output += "\n"
            output += "\n"
        return output
    
    def save(self) -> None: # finish document
        with open(self.output_path, 'w') as f:
            f.write(self.__str__)