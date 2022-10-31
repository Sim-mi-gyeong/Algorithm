class Box:
    def __init__(self, box_id, weight):
        self.box_id = box_id
        self.weight = weight
        self.prev_box = None
        self.next_box = None

    def set_prev(self, prev_box):
        self.prev_box = prev_box

    def set_next(self, next_box):
        self.next_box = next_box

    def cut_prev(self):
        if self.prev_box == None:
            return
        self.prev_box.next_box = None
        self.prev_box = None

    def cut_next(self):
        if self.next_box == None:
            return
        self.next_box.prev_box = None
        self.next_box = None

    def take_out(self):
        if self.next_box:
            self.next_box.prev_box = self.prev_box
        if self.prev_box:
            self.prev_box.next_box = self.next_box

        self.next_box = None
        self.prev_box = None


class Belt:
    def __init__(self):
        self.first_box = None
        self.last_box = None
        self.box_dict = dict()
        self.broken = False

    def add_box(self, this_box):

        self.box_dict[this_box.box_id] = this_box

        if not self.first_box:
            self.first_box = this_box

        if self.last_box:
            self.last_box.set_next(this_box)
            this_box.set_prev(self.last_box)

        self.last_box = this_box

    def pop_box(self):

        box_to_pop = self.first_box
        self.first_box = box_to_pop.next_box
        if self.first_box:
            self.first_box.cut_prev()
        else:
            self.last_box = None

        del self.box_dict[box_to_pop.box_id]

        return box_to_pop


class Factory:
    def __init__(self, args):
        N, M, *presents = args
        print("N: ", N, " M : ", M, " presents : ", presents)
        counts = N // M
        self.belts = [Belt() for _ in range(M)]
        print("self.belts : ", self.belts)

        for idx, belt in enumerate(self.belts):
            for num in range(idx * counts, (idx + 1) * counts):
                belt.add_box(Box(presents[num], presents[num + N]))
            print("belt : ", belt)

    def unload(self, max_weight):
        result = 0

        for belt in self.belts:
            if belt.first_box:
                popped_box = belt.pop_box()
                if popped_box.weight <= max_weight:
                    result += popped_box.weight
                else:
                    belt.add_box(popped_box)

        return result

    def remove(self, remove_id):
        result = -1

        for belt in self.belts:
            print("belt.box_dic : ", belt.box_dict)
            if remove_id in belt.box_dict:
                removed_box = belt.box_dict[remove_id]
                if belt.first_box == removed_box:
                    belt.first_box = removed_box.next_box
                if belt.last_box == removed_box:
                    belt.last_box = removed_box.prev_box

                removed_box.take_out()
                result = removed_box.box_id
                del belt.box_dict[removed_box.box_id]
                break

        return result

    def find(self, find_id):
        result = -1

        for belt_id, belt in enumerate(self.belts):
            if find_id in belt.box_dict:
                found_box = belt.box_dict[find_id]

                if belt.first_box != found_box:
                    belt.first_box.set_prev(belt.last_box)
                    belt.last_box.set_next(belt.first_box)
                    belt.first_box = found_box
                    belt.last_box = found_box.prev_box
                    found_box.cut_prev()

                result = belt_id + 1
                break

        return result

    def die(self, belt_id):
        result = -1
        belt_id -= 1

        if self.belts[belt_id].broken == False:
            result = belt_id + 1
            broken_belt = self.belts[belt_id]
            broken_belt.broken = True

            if len(broken_belt.box_dict):
                for idx in range(belt_id, belt_id + len(self.belts)):
                    if self.belts[idx % len(self.belts)].broken == False:
                        found_belt = self.belts[idx % len(self.belts)]

                        print("고장난 벨트의 상자 : ", broken_belt.box_dict)
                        print("옮겨갈 벨트의 상자 : ", found_belt.box_dict)
                        found_belt.box_dict.update(broken_belt.box_dict)
                        broken_belt.box_dict = {}
                        print("옮긴 후 벨트의 상자 : ", found_belt.box_dict)

                        found_belt.add_box(broken_belt.first_box)
                        found_belt.last_box = broken_belt.last_box
                        broken_belt.first_box = broken_belt.last_box = None
                        break

        return result


if __name__ == "__main__":

    Q = int(input().strip())

    query, *args = map(int, input().split())
    factory = Factory(args)

    queries = {
        200: factory.unload,
        300: factory.remove,
        400: factory.find,
        500: factory.die,
    }

    for _ in range(Q - 1):

        query, arg = map(int, input().split())
        print(queries[query](arg))

        # for belt in factory.belts:
        #     print(len(belt.box_dict), belt.first_box.box_id if belt.first_box else -1, belt.last_box.box_id if belt.last_box else -1)
