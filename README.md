# img_process

This implement some tools to manipulate images. <br>
Work in progress to implement many tools. <br>

TODO : 
- use pydantic to get environment variables
- use mkdocs and build http page accessible via github
- write some test with pytest and run it through github action
- use uv for dependency management
- use ruff as code formatter
- use ty for type checking
- use a pre-commit to run code formatter and type checking automatically
- use python @dataclass
- use fastAPI for modules API

## Concatenator

This tool is used to concatenate image into mosaic. <br>
It take several parameters in yaml file : crop, thin, border, etc. <br>

```(shell)
./concatenator.py -y yml/concatenator_op_cover_100_lq.yml
```

Example of output : <br>
![image](https://github.com/user-attachments/assets/6a0dc2cb-6d48-4b90-a162-3f08918fe70d)
