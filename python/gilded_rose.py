# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GeneralItemStrategy:
    def update(self, item):
        item.sell_in -= 1
        decrement = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - decrement)


class AgedBrieStrategy:
    def update(self, item):
        item.sell_in -= 1
        increment = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + increment)


class SulfurasStrategy:
    def update(self, item):
        item.quality = 80


class BackstagePassStrategy:
    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in <= 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

        item.sell_in -= 1


class ConjuredStrategy:
    def update(self, item):
        item.sell_in -= 1
        decrement = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - decrement)


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Conjured Mana Cake": ConjuredStrategy()
        }

    def get_strategy(self, item_name):
        """Retrieve the strategy for a given item name."""
        return self.strategies.get(item_name, DefaultStrategy())

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item.name)
            strategy.update(item)