if [ $PYTHONPATH ]; then
    if [[ ":$PYTHONPATH:" == *":/usr/lib/root:"* ]]; then
        return 0;
    else
        export PYTHONPATH=$PYTHONPATH:/usr/lib/root;
    fi
else
    export PYTHONPATH=/usr/lib/root;
fi
