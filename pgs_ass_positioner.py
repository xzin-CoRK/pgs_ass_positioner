### CHANGE VALUES HERE
ass_file_path = 'C:\\Remuxes\\YourRemux\\english.ass'
xml_file_path = 'C:\\Remuxes\\YourRemux\\dbsup2sub_output\\en_sdh.xml'

x_offset = 0  # Offset all subtitles by the specified amount.  Positive values move the text right, negative values move it left.
y_offset = 0  # Offset all subtitles by the specified amount.  Positive values move the text down, negative values move it up.

### STOP CHANGING VALUES

import xml.etree.ElementTree as ET
import os
import math

def read_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    coordinates = []
    
    for event in root.findall('.//Event'):
        graphic = event.find('Graphic')
        if graphic is not None:
            x = graphic.get('X')
            y = graphic.get('Y')
            width = graphic.get('Width')
            height = graphic.get('Height')
            if x is not None and y is not None and width is not None and height is not None:
                x = int(x) + x_offset
                y = math.floor(float(y) + (float(height) * 0.5)) + y_offset
                coordinates.append((x, y))
    
    return coordinates

def read_ass(ass_path):
    with open(ass_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    events_index = next((i for i, line in enumerate(lines) if line.strip() == "[Events]"), None)
    if events_index is None:
        raise ValueError("No [Events] section found in the ASS file.")
    
    headers = lines[events_index + 1].strip().split(',')
    event_lines = lines[events_index + 2:]
    
    return headers, event_lines, lines[:events_index + 2]

def write_ass(new_ass_path, headers, event_lines, pre_event_lines):
    with open(new_ass_path, 'w', encoding='utf-8') as file:
        file.writelines(pre_event_lines)
        file.write(','.join(headers) + '\n')
        file.writelines(event_lines)

def inject_positions(headers, event_lines, coordinates):
    dialogue_index = headers.index(' Text')
    
    for i, (x, y) in enumerate(coordinates):
        if i < len(event_lines):
            line_parts = event_lines[i].strip().split(',')
            existing_text = line_parts[dialogue_index]
            new_text = f"{{\\pos({x},{y})}}{existing_text}"
            line_parts[dialogue_index] = new_text
            event_lines[i] = ','.join(line_parts) + '\n'
    
    return event_lines

def process_files(ass_path, xml_path):
    coordinates = read_xml(xml_path)
    headers, event_lines, pre_event_lines = read_ass(ass_path)
    modified_event_lines = inject_positions(headers, event_lines, coordinates)
    
    # Create new filename by appending '_positioned' before the file extension
    base, ext = os.path.splitext(ass_path)
    new_ass_path = f"{base}_positioned{ext}"
    
    write_ass(new_ass_path, headers, modified_event_lines, pre_event_lines)




process_files(ass_file_path, xml_file_path)
