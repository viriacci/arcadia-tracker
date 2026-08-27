# -*- coding: utf-8 -*-
"""
MC Zlecenia Tracker
Aplikacja do śledzenia zleceń (kart) z blokami/itemami do zebrania w Minecraft.
Dark + gold glassmorphism, PySide6.
"""
import sys
import json
import os
import uuid

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QLineEdit, QSpinBox, QScrollArea, QFrame, QDialog,
    QFormLayout, QDialogButtonBox, QCompleter, QMessageBox, QSizePolicy,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QToolButton
)

from items_data import get_stack_size, known_item_names

APP_TITLE = "MC Zlecenia Tracker"
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "orders.json")
ICONS_DIR = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "icons")

GOLD = "#D4AF37"
GOLD_SOFT = "#E9C25D"
BG_DARK = "#14141c"

QSS = f"""
QMainWindow {{
    background-color: {BG_DARK};
}}
QWidget {{
    color: #f0e6c8;
    font-family: "Segoe UI", "Cantarell", sans-serif;
    font-size: 13px;
}}
QScrollArea {{
    border: none;
    background: transparent;
}}
QFrame#card {{
    background-color: rgba(255, 255, 255, 18);
    border: 1px solid rgba(212, 175, 55, 120);
    border-radius: 14px;
}}
QLabel#cardTitle {{
    color: {GOLD};
    font-size: 17px;
    font-weight: 600;
}}
QLabel#header {{
    color: {GOLD};
    font-size: 22px;
    font-weight: 700;
}}
QPushButton {{
    background-color: rgba(212, 175, 55, 40);
    border: 1px solid {GOLD};
    border-radius: 8px;
    padding: 6px 12px;
    color: {GOLD_SOFT};
    font-weight: 600;
}}
QPushButton:hover {{
    background-color: rgba(212, 175, 55, 90);
    color: #14141c;
}}
QPushButton:pressed {{
    background-color: {GOLD};
    color: #14141c;
}}
QToolButton {{
    background-color: rgba(255, 60, 60, 30);
    border: 1px solid rgba(255, 90, 90, 150);
    border-radius: 6px;
    color: #ffb3b3;
    padding: 3px 8px;
}}
QToolButton:hover {{
    background-color: rgba(255, 60, 60, 90);
    color: white;
}}
QLineEdit, QSpinBox {{
    background-color: rgba(0, 0, 0, 90);
    border: 1px solid rgba(212, 175, 55, 100);
    border-radius: 6px;
    padding: 4px 6px;
    color: #f0e6c8;
}}
QTableWidget {{
    background-color: rgba(0, 0, 0, 60);
    border: 1px solid rgba(212, 175, 55, 60);
    border-radius: 8px;
    gridline-color: rgba(212, 175, 55, 40);
}}
QHeaderView::section {{
    background-color: rgba(212, 175, 55, 35);
    color: {GOLD};
    border: none;
    padding: 4px;
    font-weight: 600;
}}
QTableWidget::item {{
    padding: 2px;
}}
"""


def fmt_stacks(qty: int, stack_size: int) -> str:
    stacks, rest = divmod(qty, stack_size)
    if stacks and rest:
        return f"{stacks} st. + {rest}"
    if stacks:
        return f"{stacks} st."
    return f"{rest}"


class AddItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dodaj przedmiot")
        self.setMinimumWidth(320)

        self.name_edit = QLineEdit()
        completer = QCompleter(known_item_names(), self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.name_edit.setCompleter(completer)
        self.name_edit.textChanged.connect(self._autofill_stack)

        self.stack_spin = QSpinBox()
        self.stack_spin.setRange(1, 64)
        self.stack_spin.setValue(64)

        self.target_spin = QSpinBox()
        self.target_spin.setRange(1, 999999)
        self.target_spin.setValue(64)

        form = QFormLayout()
        form.addRow("Nazwa przedmiotu:", self.name_edit)
        form.addRow("Wielkość stacku:", self.stack_spin)
        form.addRow("Cel (ilość):", self.target_spin)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def _autofill_stack(self, text):
        self.stack_spin.setValue(get_stack_size(text))

    def get_data(self):
        return {
            "name": self.name_edit.text().strip() or "Bez nazwy",
            "stack_size": self.stack_spin.value(),
            "target": self.target_spin.value(),
            "collected": 0,
        }


class OrderCard(QFrame):
    def __init__(self, order_data, on_delete, on_change):
        super().__init__()
        self.setObjectName("card")
        self.order_data = order_data
        self.on_delete = on_delete
        self.on_change = on_change

        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 14, 16, 14)
        outer.setSpacing(8)

        top = QHBoxLayout()
        self.title_edit = QLineEdit(order_data.get("title", "Zlecenie"))
        self.title_edit.setObjectName("cardTitle")
        self.title_edit.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.title_edit.setStyleSheet(f"border:none; background:transparent; color:{GOLD}; font-size:16px; font-weight:700;")
        self.title_edit.textChanged.connect(self._title_changed)

        del_btn = QToolButton()
        del_btn.setText("Usuń zlecenie ✕")
        del_btn.clicked.connect(lambda: self.on_delete(self))

        top.addWidget(self.title_edit, 1)
        top.addWidget(del_btn)
        outer.addLayout(top)

        self.table = QTableWidget(0, 9)
        self.table.setHorizontalHeaderLabels([
            "Przedmiot", "Stack", "Cel (szt.)", "Cel (stacki)",
            "Zebrano (szt.)", "+ dodaj", "Pozostało (szt.)", "Pozostało (stacki)", ""
        ])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setMinimumHeight(120)
        outer.addWidget(self.table)

        add_row = QHBoxLayout()
        add_item_btn = QPushButton("+ Dodaj przedmiot")
        add_item_btn.clicked.connect(self.add_item_dialog)
        add_row.addWidget(add_item_btn)
        add_row.addStretch()
        outer.addLayout(add_row)

        self.refresh_table()

    def _title_changed(self, text):
        self.order_data["title"] = text
        self.on_change()

    def add_item_dialog(self):
        dlg = AddItemDialog(self)
        if dlg.exec() == QDialog.Accepted:
            self.order_data["items"].append(dlg.get_data())
            self.refresh_table()
            self.on_change()

    def remove_item(self, idx):
        del self.order_data["items"][idx]
        self.refresh_table()
        self.on_change()

    def add_collected(self, idx, spin):
        amount = spin.value()
        if amount <= 0:
            return
        self.order_data["items"][idx]["collected"] += amount
        spin.setValue(0)
        self.refresh_table()
        self.on_change()

    def refresh_table(self):
        items = self.order_data["items"]
        self.table.setRowCount(len(items))
        for row, item in enumerate(items):
            stack = item["stack_size"]
            target = item["target"]
            collected = item["collected"]
            remaining = max(0, target - collected)

            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(str(stack)))
            self.table.setItem(row, 2, QTableWidgetItem(str(target)))
            self.table.setItem(row, 3, QTableWidgetItem(fmt_stacks(target, stack)))

            collected_item = QTableWidgetItem(str(collected))
            if collected >= target:
                collected_item.setForeground(Qt.green)
            self.table.setItem(row, 4, collected_item)

            # + dodaj: spinbox + button w jednej komórce
            cell = QWidget()
            cell_layout = QHBoxLayout(cell)
            cell_layout.setContentsMargins(2, 2, 2, 2)
            spin = QSpinBox()
            spin.setRange(0, 999999)
            btn = QPushButton("Dodaj")
            btn.setFixedWidth(55)
            cell_layout.addWidget(spin)
            cell_layout.addWidget(btn)
            self.table.setCellWidget(row, 5, cell)
            btn.clicked.connect(lambda _, i=row, s=spin: self.add_collected(i, s))

            rem_item = QTableWidgetItem(str(remaining))
            if remaining == 0:
                rem_item.setForeground(Qt.green)
            self.table.setItem(row, 6, rem_item)
            self.table.setItem(row, 7, QTableWidgetItem(fmt_stacks(remaining, stack)))

            del_cell = QToolButton()
            del_cell.setText("✕")
            del_cell.clicked.connect(lambda _, i=row: self.remove_item(i))
            self.table.setCellWidget(row, 8, del_cell)
        self.table.setColumnWidth(5, 130)
        self.table.setColumnWidth(8, 36)
        self.table.resizeRowsToContents()
        total_h = self.table.horizontalHeader().height() + sum(
            self.table.rowHeight(r) for r in range(self.table.rowCount())
        ) + 10
        self.table.setFixedHeight(max(60, total_h))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.resize(1100, 750)

        self.orders = self.load_orders()

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)

        header_row = QHBoxLayout()
        header = QLabel("⛏ MC Zlecenia Tracker")
        header.setObjectName("header")
        add_order_btn = QPushButton("+ Nowe zlecenie")
        add_order_btn.clicked.connect(self.add_order)
        header_row.addWidget(header)
        header_row.addStretch()
        header_row.addWidget(add_order_btn)
        main_layout.addLayout(header_row)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self.cards_container)
        self.cards_layout.setSpacing(14)
        self.cards_layout.addStretch()
        self.scroll.setWidget(self.cards_container)
        main_layout.addWidget(self.scroll)

        self.card_widgets = []
        for order in self.orders:
            self._add_card_widget(order)

    def _add_card_widget(self, order_data):
        card = OrderCard(order_data, self.delete_order, self.save_orders)
        self.cards_layout.insertWidget(self.cards_layout.count() - 1, card)
        self.card_widgets.append(card)

    def add_order(self):
        order = {"id": str(uuid.uuid4()), "title": "Nowe zlecenie", "items": []}
        self.orders.append(order)
        self._add_card_widget(order)
        self.save_orders()

    def delete_order(self, card):
        reply = QMessageBox.question(
            self, "Usuń zlecenie", "Na pewno usunąć to zlecenie?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return
        self.orders.remove(card.order_data)
        self.card_widgets.remove(card)
        card.setParent(None)
        card.deleteLater()
        self.save_orders()

    def load_orders(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_orders(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.orders, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("Błąd zapisu:", e)

    def closeEvent(self, event):
        self.save_orders()
        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
