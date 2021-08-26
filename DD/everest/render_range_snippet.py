import sys
DEST_IMAGE_DIR="/path_to_output_image_directory"
DATA_DIR= "/path_to_input_data"
DATA_FILES = []

total_steps = 300
for i in range(0, total_steps):
	temp_name = "%s/data_step_%04d.vtu" % (DATA_DIR, i)
	DATA_FILES.append(temp_name)

start_frame=int(sys.argv[1])
num_frames=int(sys.argv[2])

renderView1 = CreateView('RenderView')
## set other view parameters

ugrid_data = XMLUnstructuredGridReader(FileName= DATA_FILES[start_frame])

## Set up all of your filters and rendering parameters

## Now loop over the given set of frames, and write out an image for each
for i in range(start_frame, start_frame+num_frames):
    ugrid_data.FileName=DATA_FILES[i]
    IMAGE_FILE_NAME="%s/frame_%04d.png" % (DEST_IMAGE_DIR, i)
    print ("Save: ", IMAGE_FILE_NAME)
    WriteImage(IMAGE_FILE_NAME)
