#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

translation_layers = []
seeds = [int(x) for x in data.pop(0).split(": ")[-1].split(" ")]
original_seeds = seeds.copy()
data.pop(0)

def make_trans_layer(line: str) -> tuple[int, int, int]:
    d_start, s_start, r_len = [int(x) for x in line.split(" ")]
    change = d_start - s_start
    return (s_start, s_start + r_len, change)

while data:
    data.pop(0)
    tmp = []

    while True:
        if not data: break
        if not (line := data.pop(0)): break
        tmp.append(make_trans_layer(line))
    
    translation_layers.append(tmp)

for translation_layer in translation_layers:
    for index in range(len(seeds)):
        for translation in translation_layer:
            if seeds[index] in range(translation[0], translation[1] + 1):
                seeds[index] += translation[2]
                break

def range_resolver(in_start: int, in_end: int, trans_layer: list) -> list:
    outputs = []

    for layer in trans_layer:
        layer_range = range(layer[0], layer[1] + 1)
        new_start = in_start
        new_end = in_end


        if in_start not in layer_range and in_end not in layer_range: continue

        if new_start not in layer_range:
            new_start = layer[0]
            outputs += range_resolver(new_start, new_end, trans_layer)

        if new_end not in layer_range:
            new_end = layer[1]
            outputs += range_resolver(new_start, new_end, trans_layer)

        new_start += layer[2]
        new_end += layer[2]

        outputs.append((new_start, new_end))

    if not outputs:
        outputs = [(in_start, in_end)]

    return outputs

seed_ranges = []
for i in range(len(original_seeds)):
    if i % 2 == 0:
        seed_ranges.append((original_seeds[i], original_seeds[i] + original_seeds[i + 1] - 1))

for translation_layer in translation_layers:
    new_seed_ranges = []

    for start, end in seed_ranges:
        new_seed_ranges += range_resolver(start, end, translation_layer)
    
    seed_ranges = new_seed_ranges.copy()

gold = min([x[0] for x in seed_ranges])
print(f"Silver: {min(seeds)}\nGold: {gold}")
