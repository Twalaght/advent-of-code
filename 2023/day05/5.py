#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

seeds = [int(x) for x in data.pop(0).split(": ")[-1].split(" ")]
data.pop(0)

translation_layers = []
while data:
    data.pop(0)
    translations = []

    while data:
        if not (line := data.pop(0)): break
        dest_start, source_start, run_len = [int(x) for x in line.split(" ")]
        translations.append((source_start, source_start + run_len, dest_start - source_start))
    
    translation_layers.append(translations)

silver, gold = [], []
for i in range(len(seeds)):
    silver.append((seeds[i], seeds[i]))
    if i % 2 == 0: gold.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

def range_resolver(in_start: int, in_end: int, trans_layer: list) -> list:
    outputs = []
    for layer in trans_layer:
        layer_range = range(layer[0], layer[1] + 1)
        new_start, new_end = in_start, in_end

        if in_start not in layer_range and in_end not in layer_range: continue

        if new_start not in layer_range:
            new_start = layer[0]
            outputs += range_resolver(layer[0], new_end, trans_layer)

        if new_end not in layer_range:
            new_end = layer[1]
            outputs += range_resolver(new_start, layer[1], trans_layer)

        new_start += layer[2]
        new_end += layer[2]
        outputs.append((new_start, new_end))

    return outputs or [(in_start, in_end)]

for translation_layer in translation_layers:
    new_silver, new_gold = [], []

    for start, end in silver: new_silver += range_resolver(start, end, translation_layer)
    for start, end in gold: new_gold += range_resolver(start, end, translation_layer)
    
    silver, gold = new_silver, new_gold

print(f"Silver: {min([x[0] for x in silver])}\nGold: {min([x[0] for x in gold])}")
