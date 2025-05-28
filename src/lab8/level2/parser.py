import csv

class Parser:
    def __init__(self):
        self.farms = []
        self.shops = []
        self.roads = []
        self.nodes = set()

    def parse_roads_csv(self, filepath):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)

            farms_line = next(reader)
            self.farms = [farm.strip() for farm in farms_line]
            self.nodes.update(self.farms)

            shops_line = next(reader)
            self.shops = [shop.strip() for shop in shops_line]
            self.nodes.update(self.shops)


            for row in reader:
                u, v, capacity_str = row
                u = u.strip()
                v = v.strip()
                capacity = int(capacity_str.strip())

                self.roads.append((u, v, capacity))
                self.nodes.add(u)
                self.nodes.add(v)

        return (self.farms, self.shops, self.roads, sorted(self.nodes))
