if [ -z $1 ]; then
    printf -- 'init_py.sh [type] [number] [question title]';
    exit;
fi

CUR=${PWD}

case $1 in
    uva)
        VOL=$2
        VOL_PREFIX=${VOL:0:${#VOL}-2}
        git checkout -b "uva-p${VOL}"
        if [ ! -d "$CUR/uva/v$VOL_PREFIX/" ]; then
            mkdir "$CUR/uva/v$VOL_PREFIX/"
        fi
        touch "$CUR/uva/v$VOL_PREFIX/p$2-$3.py"
        echo "Create source file uva/v$VOL_PREFIX/p$2-$3.py"
        touch "$CUR/uva/v$VOL_PREFIX/p$2-$3.in"
        echo "Create input file uva/v$VOL_PREFIX/p$2-$3.in"
        touch "$CUR/uva/v$VOL_PREFIX/p$2-$3.out"
        echo "Create output file uva/v$VOL_PREFIX/p$2-$3.out"
        ;;
esac
