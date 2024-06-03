import os
import pickle
from typing import *
import pickle

import time
from utils import constants

WHITELIST = 0
BLACKLIST = 1


class SeatingTable:
    def __init__(
        self,
        table_path=constants.TABLE_FILE,
        name_path=constants.NAME_FILE,
        rule_path=constants.RULES_FILE,
        output_path=constants.OUTPUT_DIR,
    ):
        self.table_path = table_path
        self.name_path = name_path
        self.rule_path = rule_path
        self.output_path = output_path
        self.prob = []
        self.table = []
        self.names = {"other": []}
        self.rules = ({}, {})
        self.status = {}
        self.table_num = {}
        self.read_table()
        self.read_names()
        self.read_rules()

    def read_table(self) -> None:
        """Reads the table given"""
        table = self.table
        with open(self.table_path) as f:
            for line in f.read().splitlines():
                key, value = line.split("=", 1)
                if key == "ColumnOfGroup":
                    self.table_num["ColumnOfGroup"] = [int(i) for i in value.split(",")]
                    continue
                self.table_num[key] = int(value)
        for i in range(self.table_num["GroupNum"]):
            table.append([])
            for j in range(self.table_num["ColumnOfGroup"][i]):
                table[i].append([])
                for _ in range(self.table_num["LineOfGroup"]):
                    table[i][j].append("")
        self.table = table

    def read_names(self) -> None:
        """Reads the names of the specified properties"""
        idx = "other"
        with open(self.name_path) as f:
            for line in f.read().splitlines():
                if line[0] == "[" and line[-1] == "]":
                    idx = line[1:-1]
                    self.names[idx] = []
                    continue
                self.names[idx].append(line)
                self.status[line] = False
                # self.prob[line] = [
                #     [constants.START_PROBABILITY] * self.table_num["ColumnOfGroup"][i]
                #     for i in range(self.table_num["GroupNum"])
                # ]

    def read_rules(self) -> None:
        """Reads the rules of the specified properties"""
        rules = self.rules
        with open(self.rule_path) as f:
            for line in f.read().splitlines():
                if "[WhiteList]" in line:
                    idx = 0
                    continue
                if "[BlackList]" in line:
                    idx = 1
                    continue
                key, value = line.split(":")
                if key in rules[idx]:
                    rules[idx][key].append(value)
                else:
                    rules[idx][key] = [value]
                if value in rules[idx]:
                    rules[idx][value].append(key)
                else:
                    rules[idx][value] = [key]
        self.rules = rules
        self.check()

    def check(self) -> None:
        """Check if the rules fits the given"""
        names = self.status.keys()
        # White List
        for k, v in self.rules[WHITELIST].items():
            if k not in names:
                raise ValueError("Invalid rule with '%s' which is not in names" % k)
            for vn in v:
                if vn not in names:
                    raise ValueError(
                        "Invalid rule with '%s' which is not in names" % vn
                    )
                if (
                    vn in self.rules[BLACKLIST] and k in self.rules[BLACKLIST][vn]
                ):  # White list is same as blacklist
                    raise ValueError(
                        "Invalid rule with {} and {} in both white and black lists".format(
                            vn, k
                        )
                    )
                if len(v) > 1:
                    raise ValueError("Name {} appeared mutiple times".format(k))
                if v.count(vn) > 1:
                    raise ValueError(
                        "Name {} appeared mutiple times in key {}".format(vn, k)
                    )
        # Black List
        for k, v in self.rules[BLACKLIST].items():
            if k not in names:
                raise ValueError("Invalid rule with '%s' which is not in names" % k)
            for vn in v:
                if vn not in names:
                    raise ValueError(
                        "Invalid rule with '%s' which is not in names" % vn
                    )
                if v.count(vn) > 1:
                    raise ValueError(
                        "Name {} appeared mutiple times in key {}".format(vn, k)
                    )

    def __str__(self) -> str:
        """Output the table"""
        table = self.table
        output = ""
        for i in range(len(table)):
            for j in range(len(table[i])):
                for k in range(len(table[i][j])):
                    output += table[i][j][k] + " "
                output += "\n"
            output += "\n"
        return output

    def save(self) -> None:  # finish document
        """Save the table into txt and dat"""
        filename = os.path.join(self.output_path, str(time.time()))
        with open("{}.txt".format(filename), "w") as f:
            f.write(self.__str__())
        with open("{}.dat".format(filename), "wb") as f:
            pickle.dump(self.table, f)
