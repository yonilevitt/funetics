# from moviepy.editor import VideoFileClip
# import os
# my_path = os.path.dirname(__file__)
# # Load the MP4 video
# video = VideoFileClip(os.path.join(my_path,"kika.mp4"))

# # Convert the video to a GIF
# output_gif = os.path.join(my_path,"kika.gif")
# video.write_gif(output_gif)

# # Close the video object
# video.close()


import imageio,os
from tkinter import *
from PIL import Image, ImageTk

path  =os.path.join(os.path.dirname(__file__),"kika.gif")
path2 = os.path.join(os.path.dirname(__file__),"kika.gif")
#gif = imageio.mimread(path)
#imageio.mimsave(path2,gif,"gif")

# Create a new Toplevel window
popup_window = Toplevel()

gif = imageio.get_reader(path,'.gif',mode="I")
frameCnt = gif.get_length()
frames = [imageio.imsave(path2.replace(".gif",f'.{idx}.gif'),im,"gif") for idx,im in enumerate(iter(gif))]
    

    # Function to update the displayed frame
def update_frame(frame_idx=0):
        # Load the GIF image and update the label with the new frame
        frame_idx = frame_idx%frameCnt
        frame = ImageTk.PhotoImage(file = path2.replace(".gif",f'.{frame_idx}.gif'))
        gif_label.configure(image=frame)
        gif_label.image = frame
        
        # Increase the frame index and schedule the next frame update
        frame_idx += 1
        popup_window.after(100, update_frame, frame_idx)
    # Load the first frame and start the frame update process
gif_label = Label(popup_window)
gif_label.pack()
update_frame(0)

# Stall the method until the popup window is closed
popup_window.mainloop()