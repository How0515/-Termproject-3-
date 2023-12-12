import numpy as np

def read_obj(fileName):
    vertices, triangles, texture_uv, texture_map = [], [], [], []
    
    with open(fileName) as f:
        for line in f:
            data = line.split()
            
            if not data:
                continue
            
            if data[0] == "v":
                vertices.append(data[1:4] + [1, 1, 1])
            elif data[0] == "vt":
                texture_uv.append(data[1:3])
            elif data[0] == "f":
                face_data = [data[i].split("/") for i in range(1, len(data))]
                for i in range(len(face_data) - 2):
                    triangles.append([face_data[0][0], face_data[i + 1][0], face_data[i + 2][0]])
                    if len(face_data[0]) > 1 and len(face_data[i + 1]) > 1 and len(face_data[i + 2]) > 1:
                        texture_map.append([face_data[0][1], face_data[i + 1][1], face_data[i + 2][1]])
                
    vertices = np.array(vertices, dtype=float)
    triangles = np.array(triangles, dtype=int) - 1 

    textured = False
    if texture_uv and texture_map:
        textured = True
        texture_uv = np.array(texture_uv, dtype=float)
        texture_uv[:, 1] = 1 - texture_uv[:, 1]
        texture_map = np.array(texture_map, dtype=int) - 1
    
    return vertices, triangles, texture_uv, texture_map, textured
