# img_process

This implement some tools to manipulate images. <br>
Work in progress to implement many tools. <br>

## Concatenator

This tool is used to concatenate image into mosaic.
It take several parameters in yaml file : crop, thin, border, etc.

```(shell)
./concatenator.py -y yml/concatenator_op_cover_100_lq.yml
```

TODO: Adding a garbage collector would greatly reduce the RAM used.

Example of output :
![image](https://github.com/user-attachments/assets/6a0dc2cb-6d48-4b90-a162-3f08918fe70d)
