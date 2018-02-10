export PATH=$PATH:"/c/Program Files (x86)/Graphviz2.38/bin"

# dot.exe -T png -o model.png ./model.gv
# dot.exe -Kfdp -Gsplines=true -Tpng -o model-conv-short.png ./model-conv-short.gv

dot.exe -Kfdp -Gsplines=true -Tpng -o model-conv-deconv.png ./model-conv-deconv.gv