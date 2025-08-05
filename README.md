# ASCII Image Converter
## Convert any image into ASCII art using Python.  

How It Works
1. Load an image using `PIL.Image.open()`
2. Resize and convert to grayscale
3. Map pixel brightness to characters from a custom ASCII set
4. Optional: Skip background based on user input (`white` or `black`)
5. Output formatted ASCII string to `ASCII_img.txt`

Image1 - 
<p align="center">
  <img src="https://github.com/user-attachments/assets/d8bb602b-f47f-4632-a4e1-96ea4abc4ce9" height=500 width=500 />
  <img src="https://github.com/user-attachments/assets/b6d8ade4-060b-480f-aa0a-369a9b789a4e" height=500 width=300 />
</p>

Image2 - 
<p align="center">
  <img src="https://github.com/user-attachments/assets/b98c031d-8fff-4e9f-9c96-5bc506d81699" height=500 width=500 />
  <img src="https://github.com/user-attachments/assets/d69e61ee-4d7d-44f6-8975-c72cab5f753e" height=500 width=300 />
</p>

Features
- Converts `.jpg`, `.png`, and other image formats
- Optional background filtering (white or black)
- Accurate aspect ratio fix for terminal display
- Outputs clean `.txt` ASCII file
- Easily customizable width and ASCII characters

Requirements
- Python 3.x
- Pillow





