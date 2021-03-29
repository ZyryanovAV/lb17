#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from typing import List

class IllegalTimeError(Exception):

    def __init__(self, time, message="Illegal time (ЧЧ:ММ)"):
        self.time = time
        self.message = message
        super(IllegalTimeError, self).__init__(message)

    def __str__(self):
        return f"{self.time} -> {self.message}"


class UnknownCommandError(Exception):

    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


@dataclass(frozen=True)
class train:
    name: str
    num: int
    time: str


@dataclass
class Staff:
    trains: List[train] = field(default_factory=lambda: [])

    def add(self, name, num, time):

        if ":" not in time:
            raise IllegalTimeError(time)

        self.trains.append(
            train(
                name=name,
                num=num,
                time=time
            )
        )

        self.trains.sort(key=lambda train: train.name)

    def __str__(self):
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        table.append(line)

        for idx, train in enumerate(self.trains, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                    idx,
                    train.name,
                    train.num,
                    train.time
                )
            )

        table.append(line)

        return '\n'.join(table)

    def select(self, numbers):
        parts = command.split(' ', maxsplit=2)
        numbers = int(parts[1])
        result = []

        for train in self.trains:
            if train.num == numbers:
                result.append(train)

        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.trains = []

        for train_element in tree:
            name, num, time = None, None, None

            for element in train_element:
                if element.tag == 'name':
                    name = element.text
                elif element.tag == 'num':
                    num = int(element.text)
                elif element.tag == 'time':
                    time = element.text

                if name is not None and num is not None \
                        and time is not None:
                    self.trains.append(
                        train(
                            name=name,
                            num=num,
                            time=time
                        )
                    )

    def save(self, filename):
        root = ET.Element('trains')
        for train in self.trains:
            train_element = ET.Element('train')

            name_element = ET.SubElement(train_element, 'name')
            name_element.text = train.name

            num_element = ET.SubElement(train_element, 'num')
            num_element.text = train.num

            time_element = ET.SubElement(train_element, 'time')
            time_element.text = str(train.time)

            root.append(train_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)