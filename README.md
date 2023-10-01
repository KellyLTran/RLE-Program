# RLE-Program

Functionality
A user-friendly menu is presented with various options of loading an image, reading RLE strings, and displaying the image. 
Images are structured as lists of numbers, starting with the width and height of the image. 
Pixel colors are numerically represented, and runs of similar pixels are capped at 15 consecutive instances.

Project Structure
The program uses RLE to compress data where similar consecutive elements, such as pixel colors, are represented.
Images are inherently stored in an uncompressed/unencoded format. The program works with this data in terms of lists.
The program offers multiple methods of data input, including loading from a file, inputting RLE data manually, and handling hex string data.
Data visualization options include displaying the original image, its RLE representation, the RLE in hexadecimal, and the uncompressed data in hexadecimal.

Credits
The UF CISE Department provided the objectives for this project to complete.
