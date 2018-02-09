Colorizing Black And White Photos(Still In Development)
====
We tried to implement a [Github Project](https://github.com/emilwallner/Coloring-greyscale-images-in-Keras) in a different way

To make it run faster on CPU, we redesigned the model:
<br><img src="files/model.png" max-width="500px" /><br>
Input is black & white photo, output is colorized photo, there are 20 train samples in total

Following is the result we obtained:
<table>
<tr><th>input</th><th>output</th></tr>	
<tr><td><img src="files/Predict/group2/chengmei.png" /></td>
<td><img src="files/output/chengmei.png" /></td></tr>
<tr><td><img src="files/Predict/group2/leifeng.png" /></td>
<td><img src="files/output/leifeng.png" /></td></tr>
<tr><td><img src="files/Predict/group2/marie_curie.png" /></td>
<td><img src="files/output/marie_curie.png" /></td></tr>
<tr><td><img src="files/Predict/group2/turing.png" /></td>
<td><img src="files/output/turing.png" /></td></tr>
<!--
<tr><td><img src="files/Predict/group1/0fAtAB.jpg" /></td>
<td><img src="files/output/0fAtAB.png" /></td></tr>
<tr><td><img src="files/Predict/group1/1QejlL.jpg" /></td>
<td><img src="files/output/1QejlL.png" /></td></tr>
<tr><td><img src="files/Predict/group1/6v14hm.jpg" /></td>
<td><img src="files/output/6v14hm.png" /></td></tr>
<tr><td><img src="files/Predict/group1/7Vizcm.jpg" /></td>
<td><img src="files/output/7Vizcm.png" /></td></tr>
-->
</table>

Result using 179 train samples + residual learning + deconvolution:
<table>
<tr><th>input</th><th>output</th></tr>	
<tr><td><img src="files/Predict/64/chengmei.png" width="256px" /></td>
<td><img src="files/output/chengmei.png" width="256px" /></td></tr>
<tr><td><img src="files/Predict/64/leifeng.png" width="256px" /></td>
<td><img src="files/output/leifeng.png" width="256px" /></td></tr>
<tr><td><img src="files/Predict/64/marie_curie.png" width="256px" /></td>
<td><img src="files/output/marie_curie.png" width="256px" /></td></tr>
<tr><td><img src="files/Predict/64/turing.png" width="256px" /></td>
<td><img src="files/output/turing.png" width="256px" /></td></tr>
</table>

Reference
----
* [https://github.com/richzhang/colorization/tree/master/colorization](https://github.com/richzhang/colorization/tree/master/colorization)
* [https://github.com/phillipi/pix2pix](https://github.com/phillipi/pix2pix)

[Github Link](https://github.com/microic/niy/tree/master/examples/colorizing_photos)