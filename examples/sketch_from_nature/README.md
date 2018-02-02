Training An Artificial Neural Network To Sketch From Nature
====

An artificial neural network can help artists design artworks. This example shows one method

First, select a nature image to sketch
<br><img src="files/peach_blossom.jpg" height="240px" /><br>

Then, define a model for the artificial neural network
<br><img src="files/model.png" /><br>

Each time we feed the artificial neural network with one randomly selected pixel, take the coordinate(x, y) of each pixel as input and 
the color(r, g, b) of each pixel as output

The artificial neural network will "sketch" gradually

After a few minutes, you will get the following picture
<br><img src="files/_img_start.png" height="240px" /><br>
After about 2 hours, you will get the following picture
<br><img src="files/_img.png" height="240px" /><br>
<br>

Go chess player can learn from AlphaGo, artists can learn to draw from machine too!

[Github Link](https://github.com/microic/niy/tree/master/examples/sketch_from_nature)