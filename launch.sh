
export IMG_FILES="$(ls one_piece_all/extracted/*.jpg | head -n 100)"
#export IMG_FILES="$(ls one_piece_all/one_piece_T046/*.jpg | head -n 25)"
#export IMG_FILES="./1crayon.png"

#export CROP_SIZEX=1536
#export CROP_SIZEY=2401
export CROP_SIZEX=1920
export CROP_SIZEY=3005

export CROP_POSX=0
export CROP_POSY=0

export SHAPEX=10
export SHAPEY=10

export THIN_SIZEX=1920
export THIN_SIZEY=3005

python3 ./test.py ${CROP_SIZEY} ${CROP_SIZEX} ${CROP_POSY} ${CROP_POSX} ${SHAPEX} ${SHAPEY} ${THIN_SIZEX} ${THIN_SIZEY} ${IMG_FILES}
