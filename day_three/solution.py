# import pandas as pd
import numpy as np  
import copy

_input = open("day_three/input.txt")
_input = [x for x in _input.read().splitlines()]
wire1, wire2 = _input[0].split(','), _input[1].split(',')

# position = [x, y]
# segment = [ [x_init, y_init], [x_final, y_final] ]
def generate_segment(pos, path):
    new_pos = copy.deepcopy(pos)

    if path[0] == "R":
        new_pos[0] += int(path[1:])

    if path[0] == "L":
        new_pos[0] -= int(path[1:])

    if path[0] == "U":
        new_pos[1] += int(path[1:])

    if path[0] == "D":
        new_pos[1] -= int(path[1:])

    return [pos, new_pos]

def get_steps_to_point(segment, point, wire_segments):
    def get_non_zero(arr):
        result = np.trim_zeros(arr)
        if result:
            return abs(int(result))
        else:
            return 0

    segments_before = wire_segments[:wire_segments.index(segment)]
    dist = 0
    for seg in segments_before:
        dist += get_non_zero(np.subtract(seg[1], seg[0]))
    
    dist += get_non_zero(np.subtract(segment[0], point))
    return dist
    

# segment 1 must be horizontal
def check_intersection(segment1, segment2): 
    # standardise terms such that for a horizontal line going from (x1, y) to (x2, y),
    # we define x1 < x2 and likewise for a vertical 
    # direction does not matter in this case
    seg1_x1, seg1_x2 = min(segment1[0][0], segment1[1][0]), max(segment1[0][0], segment1[1][0])
    seg1_y = segment1[0][1]
    seg2_x = segment2[0][0]
    seg2_y1, seg2_y2 = min(segment2[0][1], segment2[1][1]), max(segment2[0][1], segment2[1][1])
    
    return ((seg1_x1 <= seg2_x <= seg1_x2) and (seg2_y1 <= seg1_y <= seg2_y2)), [seg2_x, seg1_y]
                
def calculate_distance(point, hori_seg=None, hori_wire=None, vert_seg=None, vert_wire=None):
    # distance calculation is different depending on which part of the problem we are answering
    part = 2

    if part == 1:
        return abs(point[0]) + abs(point[1])
    if part == 2:
        hori_dist = get_steps_to_point(hori_seg, point, hori_wire)
        vert_dist = get_steps_to_point(vert_seg, point, vert_wire)
        return hori_dist + vert_dist


def split_wire_segments(paths):
    curpos = [0, 0]
    hori_paths = []
    vert_paths = []
    complete_paths = []
    for path in paths:
        segment = generate_segment(curpos, path)
        curpos = segment[1]
        complete_paths.append(segment)
        # tmp.append(segment)
        if path[0] == "R" or path[0] == "L":
            hori_paths.append(segment)
        else:
            vert_paths.append(segment)

    return hori_paths, vert_paths, complete_paths

def main():
    wire1_hori, wire1_vert, wire1_complete = split_wire_segments(wire1)
    wire2_hori, wire2_vert, wire2_complete = split_wire_segments(wire2)

    intersections = []
    # check for parallel intersections
    for horizontal_wire in wire1_hori:
        for vertical_wire in wire2_vert:
            intersect, point = check_intersection(horizontal_wire, vertical_wire)
            if intersect:
                intersections.append(calculate_distance(point, horizontal_wire, wire1_complete, vertical_wire, wire2_complete))

    for horizontal_wire in wire2_hori:
        for vertical_wire in wire1_vert:
            intersect, point = check_intersection(horizontal_wire, vertical_wire)
            if intersect:
                intersections.append(calculate_distance(point, horizontal_wire, wire2_complete, vertical_wire, wire1_complete))

    intersections = [n for n in sorted(intersections) if n != 0]
    print("Solution:", intersections[0])

main()