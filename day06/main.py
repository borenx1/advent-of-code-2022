# https://adventofcode.com/2022/day/6
# --- Day 6: Tuning Trouble ---

with open('day06/input.txt', 'r') as f:
    datastream_buffer = f.read().strip()

previous_markers = []
previous_markers.append(datastream_buffer[0])
previous_markers.append(datastream_buffer[1])
previous_markers.append(datastream_buffer[2])

first_start_of_packet_marker_position = 0

for i in range(3, len(datastream_buffer)):
    marker = datastream_buffer[i]
    if len(set(previous_markers + [marker])) == 4:
        first_start_of_packet_marker_position = i + 1
        break
    previous_markers[0] = previous_markers[1]
    previous_markers[1] = previous_markers[2]
    previous_markers[2] = marker

print(f'{first_start_of_packet_marker_position = }')  # 1953


# --- Part Two ---

DISTINCT_CHAR_COUNT = 14

previous_markers_2 = []
for i in range(DISTINCT_CHAR_COUNT - 1):
    previous_markers_2.append(datastream_buffer[i])

first_start_of_message_marker_position = 0

for i in range(DISTINCT_CHAR_COUNT, len(datastream_buffer)):
    marker = datastream_buffer[i]
    if len(set(previous_markers_2 + [marker])) == DISTINCT_CHAR_COUNT:
        first_start_of_message_marker_position = i + 1
        break
    for j in range(DISTINCT_CHAR_COUNT - 2):
        previous_markers_2[j] = previous_markers_2[j + 1]
    previous_markers_2[DISTINCT_CHAR_COUNT - 2] = marker

print(f'{first_start_of_message_marker_position = }')  # 2301
