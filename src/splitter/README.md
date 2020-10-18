# splitter.py
a tool to split an mp3 file into segments based on silence.

## installation
your mileage may vary depending on the environment. i'm too busy to provide support.

```bash
make install
```

## usage
edit `splitter.py` and point it at your target `mp3` file.

then run `make split` and your segments will be in the `output/` directory.

to delete the output files, you can run `make clean`
